import os
import sys
import re
import time
import logging
import subprocess
import tempfile
import threading
from typing import List, Dict, Any, Tuple

# Third-party imports
import requests
import pandas as pd
import qrcode
from PIL import Image
from geopy.distance import geodesic
import sounddevice as sd
import soundfile as sf
import whisper

# 1. Environment & Path Setup
# Ensure common macOS Homebrew paths are in environment PATH (needed for ffmpeg)
for path in ["/opt/homebrew/bin", "/usr/local/bin"]:
    if path not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + path

# Setup folder structure
ASSIGNMENT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(ASSIGNMENT_DIR, "voice_assistant.log")

# 2. Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("VoiceAssistant")

# Global variables
whisper_model = None

# 3. Cross-platform Text-to-Speech (TTS)
def speak(text: str) -> None:
    """Verbally announce text using the system's text-to-speech engine."""
    logger.info(f"Speaking: {text}")
    print(f"🔊 Assistant: {text}")

    if sys.platform == "darwin":
        # Native macOS speech synthesizer
        try:
            subprocess.run(["say", text], check=True)
        except Exception as e:
            logger.warning(f"macOS TTS failed: {e}")
    elif sys.platform.startswith("win"):
        # Windows PowerShell speech API
        try:
            escaped_text = text.replace("'", "''")
            cmd = f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{escaped_text}');\""
            subprocess.run(cmd, shell=True, check=True)
        except Exception as e:
            logger.warning(f"Windows TTS failed: {e}")
    else:
        # Linux fallback (espeak)
        try:
            subprocess.run(["espeak", text], check=True)
        except Exception as e:
            logger.warning(f"Linux espeak failed: {e}")

# 4. Geolocation helpers
def get_current_location() -> Tuple[float, float, str]:
    """Attempt to get current latitude, longitude, and city name using IP geolocation.
    
    Returns:
        Tuple[float, float, str]: (latitude, longitude, location_label)
    """
    url = "https://ipapi.co/json/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) VoiceAssistant/1.0"}
    try:
        logger.info("Attempting automatic IP-based geolocation...")
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            lat = data.get("latitude")
            lon = data.get("longitude")
            city = data.get("city", "Unknown City")
            country = data.get("country_name", "Unknown Country")
            if lat is not None and lon is not None:
                loc_label = f"{city}, {country}"
                logger.info(f"Auto-detected location: {loc_label} ({lat}, {lon})")
                return float(lat), float(lon), loc_label
    except Exception as e:
        logger.warning(f"IP geolocation failed: {e}")
    
    # Default coordinates (e.g., Toronto, Canada) if IP lookup fails
    default_lat, default_lon = 43.6532, -79.3832
    logger.info(f"Using default coordinates: Toronto, Canada ({default_lat}, {default_lon})")
    return default_lat, default_lon, "Toronto, Canada (Default)"

# 5. Command Handlers
def handle_hospital_search() -> None:
    """Searches for hospitals nearby the detected or default location."""
    lat, lon, location_name = get_current_location()
    radius_km = 5.0  # Search within 5 kilometers
    
    speak(f"Searching for hospitals near {location_name} within a {radius_km} kilometer radius...")
    
    # Calculate approximate bounding box for Nominatim query filtering
    delta = radius_km / 111.0  # 1 degree of latitude is roughly 111km
    viewbox = f"{lon-delta},{lat+delta},{lon+delta},{lat-delta}"
    
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": "hospital",
        "format": "json",
        "limit": 30,
        "viewbox": viewbox,
        "bounded": 1
    }
    headers = {
        "User-Agent": "AI-Engineering-Voice-Assistant/1.0 (faixanpervaix@github.com)"
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        error_msg = f"Failed to fetch data from OpenStreetMap. Error: {e}"
        logger.error(error_msg)
        speak("I encountered an error querying the map service. Please try again.")
        return

    # Format and filter results by exact distance using geodesic
    results = []
    for place in data:
        try:
            place_lat = float(place["lat"])
            place_lon = float(place["lon"])
            distance = geodesic((lat, lon), (place_lat, place_lon)).km
            
            if distance <= radius_km:
                results.append({
                    "Name": place.get("display_name", "Unknown Hospital").split(",")[0],
                    "Address": place.get("display_name", "Unknown Address"),
                    "Latitude": place_lat,
                    "Longitude": place_lon,
                    "Distance (km)": round(distance, 2)
                })
        except (ValueError, KeyError):
            continue

    if not results:
        msg = f"I could not find any hospitals within {radius_km} kilometers of {location_name}."
        logger.info(msg)
        speak(msg)
        return

    # Sort results by distance (closest first)
    results = sorted(results, key=lambda x: x["Distance (km)"])
    
    # Create DataFrame and print as a formatted table
    df = pd.DataFrame(results)
    print("\n" + "="*80)
    print(df[["Name", "Distance (km)", "Address"]].to_string(index=False))
    print("="*80 + "\n")

    # Export to Excel
    export_path = os.path.join(ASSIGNMENT_DIR, "nominatim_places.xlsx")
    try:
        df.to_excel(export_path, index=False)
        logger.info(f"Exported places to {export_path}")
    except Exception as e:
        logger.error(f"Failed to export search results to Excel: {e}")

    closest_hospital = results[0]["Name"]
    closest_distance = results[0]["Distance (km)"]
    speak(f"Search complete. I found {len(results)} hospitals nearby. The closest is {closest_hospital}, located {closest_distance} kilometers away. The full list has been saved to nominatim_places.xlsx.")

def handle_qr_generation(text: str) -> None:
    """Generates a premium-styled QR code for the given text/URL.
    
    Args:
        text (str): The text or URL to generate a QR code for.
    """
    if not text:
        speak("I cannot generate a QR code with empty content.")
        return
        
    speak(f"Generating QR code for: {text}...")
    
    # Clean text to create a safe filename
    safe_filename = re.sub(r'[^a-zA-Z0-9_\-]', '_', text)[:30]
    if not safe_filename:
        safe_filename = "qrcode"
    qr_filename = os.path.join(ASSIGNMENT_DIR, f"qr_{safe_filename}.png")
    
    try:
        # Initialize QRCode with custom specifications
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4
        )
        qr.add_data(text)
        qr.make(fit=True)
        
        # Style the QR code using premium colors (Dark Slate and Off-White)
        img = qr.make_image(fill_color="#1E293B", back_color="#F8FAFC").convert("RGB")
        img.save(qr_filename)
        
        logger.info(f"Successfully generated and saved QR code: {qr_filename}")
        speak("QR code has been generated successfully.")
        print(f"🖼️ Saved to: {qr_filename}")
    except Exception as e:
        error_msg = f"Failed to generate QR code. Error: {e}"
        logger.error(error_msg)
        speak("I was unable to generate the QR code due to an internal error.")

def handle_speak(text: str) -> None:
    """Speaks the provided text directly.
    
    Args:
        text (str): The text to read aloud.
    """
    speak(text)

# 6. Audio recording & Whisper integration
def lazy_load_whisper() -> whisper.Whisper:
    """Lazy load the Whisper model once to conserve memory and reduce start-up lag."""
    global whisper_model
    if whisper_model is None:
        logger.info("Loading Whisper transcription model (tiny)...")
        # Suppress FP16 CPU performance warning by specifying fp16=False later during transcribe
        whisper_model = whisper.load_model("tiny")
        logger.info("Whisper model loaded successfully.")
    return whisper_model

def record_audio(duration: int = 5, samplerate: int = 16000) -> str:
    """Record audio from the default input device (microphone) and save it to a temporary WAV file.
    
    Args:
        duration (int): Duration of recording in seconds.
        samplerate (int): Sample rate of recording. Whisper operates natively at 16kHz.
        
    Returns:
        str: Path to the recorded temporary wav file.
    """
    # Verify input device availability
    devices = sd.query_devices()
    has_input = False
    for device in devices:
        if device["max_input_channels"] > 0:
            has_input = True
            break
            
    if not has_input:
        raise OSError("No audio input devices (microphone) detected on this system.")

    temp_file = tempfile.mktemp(suffix=".wav", dir=ASSIGNMENT_DIR)
    
    # Sound recording feedback timer
    def countdown():
        for i in range(duration, 0, -1):
            sys.stdout.write(f"\r🎤 Recording... {i}s remaining ")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r🎤 Processing recording...       \n")
        sys.stdout.flush()

    timer_thread = threading.Thread(target=countdown)
    timer_thread.start()
    
    try:
        # Record mono channel
        audio_data = sd.rec(
            int(duration * samplerate), 
            samplerate=samplerate, 
            channels=1, 
            dtype='int16'
        )
        sd.wait()  # Wait for recording completion
        timer_thread.join()
        
        # Save audio file
        sf.write(file=temp_file, data=audio_data, samplerate=samplerate)
        logger.info(f"Recorded audio saved to: {temp_file}")
        return temp_file
    except Exception as e:
        if timer_thread.is_alive():
            timer_thread.join()
        if os.path.exists(temp_file):
            os.remove(temp_file)
        raise OSError(f"Audio recording failed: {e}")

def get_voice_command(duration: int = 5) -> str:
    """Triggers voice recording and transcribes it using Whisper.
    
    Returns:
        str: Transcribed text from audio.
    """
    audio_path = None
    try:
        # 1. Record
        audio_path = record_audio(duration=duration)
        
        # 2. Transcribe
        model = lazy_load_whisper()
        result = model.transcribe(audio_path, fp16=False)
        transcribed_text = result.get("text", "").strip()
        logger.info(f"Whisper Transcript: '{transcribed_text}'")
        return transcribed_text
    finally:
        # Clean up temporary audio file
        if audio_path and os.path.exists(audio_path):
            try:
                os.remove(audio_path)
            except Exception as e:
                logger.warning(f"Failed to delete temporary audio file {audio_path}: {e}")

# 7. Main Command Dispatcher
def process_command(raw_command: str) -> bool:
    """Parses the input command and routes it to the correct handler.
    
    Args:
        raw_command (str): The command string to process.
        
    Returns:
        bool: True to continue, False if exit is requested.
    """
    clean_command = raw_command.strip().lower()
    
    if not clean_command:
        return True
        
    logger.info(f"Received Command: '{raw_command}'")
    
    # Check for exit commands
    if clean_command in ["exit", "quit", "bye", "goodbye"]:
        speak("Goodbye! Have a great day.")
        return False
        
    # Command 1: Search nearby hospitals
    # Matches variations: "search nearby hospitals", "search hospitals", "find nearby hospitals", "hospital search"
    if "hospital" in clean_command and ("search" in clean_command or "find" in clean_command or "nearby" in clean_command):
        handle_hospital_search()
        
    # Command 2: Generate QR code for <text>
    # Matches: "generate qr code for <text>", "create qr code for <text>"
    elif "qr code" in clean_command:
        # Extract text after 'for' or 'code'
        match = re.search(r"qr\s+code\s+(?:for\s+)?(.+)", raw_command, re.IGNORECASE)
        if match:
            text_to_encode = match.group(1).strip()
            handle_qr_generation(text_to_encode)
        else:
            speak("What text or URL would you like me to generate the QR code for?")
            # Allow keyboard input for specifying the target
            text_to_encode = input("Enter text/URL: ").strip()
            handle_qr_generation(text_to_encode)
            
    # Command 3: Speak <any text>
    # Matches: "speak hello how are you", "say hello how are you"
    elif clean_command.startswith("speak ") or clean_command.startswith("say "):
        # Extract the rest of the text after speak/say
        match = re.search(r"^(?:speak|say)\s+(.+)", raw_command, re.IGNORECASE)
        if match:
            text_to_speak = match.group(1).strip()
            handle_speak(text_to_speak)
        else:
            speak("What would you like me to say?")
            
    else:
        speak("Sorry, I didn't recognize that command.")
        print("\n💡 Available Commands:")
        print("1. 'search nearby hospitals'")
        print("2. 'generate qr code for <text>'")
        print("3. 'speak <any text>'")
        print("4. 'exit' / 'quit'\n")
        
    return True

# 8. Interactive CLI Loop
def main():
    print("==================================================")
    print("🎤   Welcome to the Voice Command Utility System   🎤")
    print("==================================================")
    print(f"📄 Logs will be written to: {LOG_FILE}")
    print("--------------------------------------------------")
    
    speak("Hello! How can I help you today?")
    
    # Main loop
    running = True
    while running:
        print("\n⌨️  Enter a text command directly OR press [Enter] to speak via microphone (or type 'exit' to quit):")
        try:
            user_input = input(">> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n")
            user_input = "exit"
            
        if user_input == "":
            # Execute Voice recording & transcription
            print("🎤 Preparing microphone...")
            try:
                # Record voice input (defaults to 5 seconds)
                voice_command = get_voice_command(duration=5)
                if voice_command:
                    print(f"👂 Captured voice input: \"{voice_command}\"")
                    running = process_command(voice_command)
                else:
                    print("⚠️ No audio detected. Please try again.")
            except Exception as e:
                # Catch permission or hardware errors gracefully and offer text input
                logger.warning(f"Voice capture failed: {e}")
                print(f"⚠️ Voice capture failed: {e}")
                print("📝 Falling back to direct keyboard input.")
        else:
            # Process direct keyboard input
            running = process_command(user_input)

if __name__ == "__main__":
    main()
