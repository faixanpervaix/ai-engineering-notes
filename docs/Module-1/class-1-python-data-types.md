# Python Data Types

## What is a Variable?

A variable is a named container that stores a value in memory. In Python, variables are created the moment you assign a value to them — no explicit declaration needed.

```python
message = "Hello, Python!"
age = 25
pi = 3.14159
is_active = True
```

## Variable Naming Rules

- Must start with a letter (a-z, A-Z) or underscore `_`
- Remaining characters can be letters, digits (0-9), or underscores
- Case-sensitive (`name` and `Name` are different)
- Cannot use Python [reserved keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)

```python
# Valid
name = "Alice"
user_name = "Bob"
_user_id = 42
camelCase = "OK"      # not conventional in Python

# Invalid
# 1st_name = "X"     # starts with digit
# my-var = 1          # contains hyphen
# class = "math"      # reserved keyword
```

### Naming Conventions (PEP 8)

| Style | Convention | Example |
|-------|-----------|---------|
| Variables | `snake_case` | `first_name`, `total_count` |
| Constants | `UPPER_SNAKE` | `MAX_SIZE`, `PI` |
| Private | Leading underscore | `_internal` |
| Dunder | Double underscores | `__init__` |

## Dynamic Typing

Python is **dynamically typed** — a variable can hold any type, and its type can change at runtime.

```python
x = 10        # x is int
x = "hello"   # now x is str
x = [1, 2, 3] # now x is list
```

Use `type()` to check the type:

```python
print(type(42))        # <class 'int'>
print(type("hello"))   # <class 'str'>
print(type(3.14))      # <class 'float'>
```

## Basic Data Types

### 1. `int` — Integer

Whole numbers, positive or negative, with unlimited precision.

```python
a = 42
b = -100
c = 0
d = 1_000_000      # underscores for readability (Python 3.6+)
e = 0x1A           # hexadecimal (26 in decimal)
f = 0b1010         # binary (10 in decimal)

print(a + b)       # -58
print(10 // 3)     # 3 (floor division)
print(10 % 3)      # 1 (modulo)
print(2 ** 10)     # 1024 (exponentiation)
```

### 2. `float` — Floating-Point Number

Numbers with decimal points, represented as 64-bit double-precision IEEE 754 values.

```python
x = 3.14
y = -0.001
z = 1.0
w = 1.5e10         # scientific notation: 1.5 × 10^10 = 15000000000.0
inf = float('inf')
nan = float('nan')

print(0.1 + 0.2)                   # 0.30000000000000004 (floating-point precision!)
print(round(0.1 + 0.2, 1))         # 0.3
print(isinstance(3.0, float))      # True
```

### 3. `str` — String

Immutable sequence of Unicode characters, enclosed in single quotes, double quotes, triple single quotes, or triple double quotes.

```python
s1 = 'single quotes'
s2 = "double quotes"
s3 = '''triple
quotes for
multi-line'''
s4 = """also multi-line"""

# String operations
first = "Hello"
last = "World"
print(first + " " + last)        # "Hello World" (concatenation)
print("Na" * 3)                  # "NaNaNa" (repetition)

# Indexing and slicing
text = "Python"
print(text[0])      # 'P'
print(text[-1])     # 'n'
print(text[1:4])    # 'yth'  (start:stop, stop exclusive)
print(text[:3])     # 'Pyt'
print(text[::-1])   # 'nohtyP' (reverse)

# String methods
msg = "  hello, WORLD!  "
print(msg.strip())             # "hello, WORLD!"
print(msg.lower())             # "  hello, world!  "
print(msg.upper())             # "  HELLO, WORLD!  "
print(msg.replace("WORLD", "Python"))  # "  hello, Python!  "
print(msg.split(","))          # ['  hello', ' WORLD!  ']
print(", ".join(["a", "b", "c"]))  # "a, b, c"
print("hello" in msg)          # True
print(msg.startswith("  he"))  # True

# f-strings (Python 3.6+)
name = "Alice"
age = 30
print(f"{name} is {age} years old")  # "Alice is 30 years old"
print(f"{age:04d}")                  # "0030" (zero-padded)
print(f"{3.14159:.2f}")             # "3.14"

# Escape sequences
print("tab\there")
print("new\nline")
print("backslash: \\")
print('it\'s okay')
```

### 4. `bool` — Boolean

Represents `True` or `False`. Internally, `True` is `1` and `False` is `0`.

```python
is_sunny = True
is_raining = False

print(is_sunny and is_raining)   # False
print(is_sunny or is_raining)    # True
print(not is_sunny)              # False

# Truthy / Falsy values
print(bool(1))         # True
print(bool(0))         # False
print(bool("hello"))   # True
print(bool(""))        # False
print(bool([]))        # False
print(bool(None))      # False
```

### 5. `NoneType` — `None`

Represents the absence of a value. Only one possible value: `None`.

```python
result = None
print(result)          # None
print(result is None)  # True

# Common use: placeholder or function return with no value
def find_user(id):
    return None if id <= 0 else {"id": id, "name": "Alice"}
```

## Type Conversion

Explicitly convert between types using built-in functions:

```python
# int conversions
print(int(3.14))        # 3 (truncates decimal)
print(int("42"))        # 42
print(int(True))        # 1

# float conversions
print(float(3))         # 3.0
print(float("3.14"))    # 3.14

# str conversions
print(str(42))          # "42"
print(str(3.14))        # "3.14"
print(str(True))        # "True"

# bool conversions
print(bool(1))          # True
print(bool(0))          # False
print(bool(""))         # False
print(bool("text"))     # True

# Dangerous conversion
# int("hello")          # ValueError!
```

## Mutable vs Immutable

| Type | Mutable? | Notes |
|------|----------|-------|
| `int` | No | Every operation creates a new object |
| `float` | No | |
| `str` | No | Any "modification" returns a new string |
| `bool` | No | |
| `None` | No | |
| `list` | Yes | |
| `dict` | Yes | |
| `set` | Yes | |

```python
# Immutable — original stays unchanged
s = "hello"
s.upper()
print(s)               # "hello" (unchanged)
s = s.upper()          # reassign to capture the new string
print(s)               # "HELLO"

# id() shows object identity
x = 10
print(id(x))           # some memory address
x = x + 1
print(id(x))           # different address (new object)
```

## The `del` Statement

Remove a variable reference:

```python
x = 42
print(x)    # 42
del x
# print(x)  # NameError: name 'x' is not defined
```

## Multiple Assignment

Python supports assigning to multiple variables in one line:

```python
# Same value
a = b = c = 0

# Different values
x, y, z = 1, 2, 3

# Swapping (no temporary variable needed!)
a, b = 10, 20
a, b = b, a
print(a, b)            # 20 10
```

## `is` vs `==`

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True — same value
print(a is b)    # False — different objects in memory
print(a is c)    # True — same object
```

---

## Practice Test

### Question 1

```python
x = 10
y = 3
print(x / y)
print(x // y)
print(x % y)
print(x ** y)
```

What is the output?

<details>
<summary>Solution</summary>

```
3.3333333333333335
3
1
1000
```

| Operator | Name | Returns | Example | Result |
|----------|------|---------|---------|--------|
| `/` | Division | `float` | `10 / 3` | `3.333...` |
| `//` | Floor division | `int` | `10 // 3` | `3` |
| `%` | Modulo | `int` | `10 % 3` | `1` |
| `**` | Exponentiation | `int`/`float` | `10 ** 3` | `1000` |

</details>

---

### Question 2

What is the type of `result` after each line executes?

```python
result = 42 // 5          # ?
result = 42 / 5           # ?
result = "42" + str(5)    # ?
result = bool(0)          # ?
result = None             # ?
```

<details>
<summary>Solution</summary>

- `42 // 5` → `int` (8)
- `42 / 5` → `float` (8.4)
- `"42" + str(5)` → `str` ("425")
- `bool(0)` → `bool` (False)
- `None` → `NoneType`

</details>

---

### Question 3

```python
name = "Python"
print(name[0] + name[-1])
print(name[1:4])
print(name[::-1])
```

What is the output?

<details>
<summary>Solution</summary>

```
Pn
yth
nohtyP
```

- `name[0]` is `'P'`, `name[-1]` is `'n'`.
- `name[1:4]` slices from index 1 up to (but not including) index 4 → `'yth'`.
- `[::-1]` reverses the string.

</details>

---

### Question 4

```python
a, b = 5, 10
a, b = b, a + b
print(a, b)
```

What is printed?

<details>
<summary>Solution</summary>

```
10 15
```

Right-hand side is evaluated first: `(10, 5 + 10)` → `(10, 15)`, then unpacked into `a` and `b`.

</details>

---

### Question 5

Identify the errors in the following code:

```python
1st_number = 10
my-name = "Alice"
class = "Math"
print(MY-NAME)
```

<details>
<summary>Solution</summary>

- `1st_number` — variable name starts with a digit.
- `my-name` — hyphen is not allowed in identifiers.
- `class` — reserved keyword.
- `print(MY-NAME)` — variable was defined as `my-name` (which is already invalid), and `MY-NAME` is not defined.

</details>

---

### Question 6

```python
text = "Data Science"
print(text.upper())
print(text.replace("Science", "Analytics"))
print(text.find("Sci"))
print("data" in text)
```

What is the output?

<details>
<summary>Solution</summary>

```
DATA SCIENCE
Data Analytics
5
False
```

- `.upper()` returns a new uppercase string (original unchanged).
- `.replace()` returns a new string with the substring replaced.
- `.find("Sci")` returns the starting index of `"Sci"` (index 5).
- `"data" in text` is `False` because strings are case-sensitive.

</details>

---

### Question 7

```python
x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(x + y)
print(x * 10)
```

What is the output?

<details>
<summary>Solution</summary>

```
False
True
False
1
10
```

Booleans are subclasses of `int` (`True` = 1, `False` = 0), so arithmetic operations work on them.

</details>

---

### Question 8

What is the value of `z` at the end?

```python
x = 3.14159
y = int(x)
z = float(y)
```

<details>
<summary>Solution</summary>

```
3.0
```

`int(3.14159)` truncates the decimal → `3`. `float(3)` → `3.0`.

</details>

---

### Question 9

```python
print(type(10))
print(type(10.0))
print(type(10 // 3))
print(type(10 / 3))
print(type("10"))
```

Write down the output of each `print`.

<details>
<summary>Solution</summary>

```
<class 'int'>
<class 'float'>
<class 'int'>
<class 'float'>
<class 'str'>
```

- `10` is an integer literal.
- `10.0` is a float literal.
- `10 // 3` is integer division → `int`.
- `10 / 3` always returns `float`.
- `"10"` is a string literal.

</details>

---

### Question 10 (Challenge)

```python
a = 256
b = 256
print(a is b)    # True or False?

x = 257
y = 257
print(x is y)    # True or False?

print(a == b)    # True or False?
print(x == y)    # True or False?
```

<details>
<summary>Solution</summary>

```
True
False
True
True
```

Python caches small integers in the range [-5, 256] for performance. `a is b` is `True` because both point to the same cached object. `x is y` is `False` because 257 is outside the cache, so two separate objects are created. `==` compares value, so both are `True`.

**Moral**: Always use `==` for value comparison; use `is` only for `None` checks.

</details>

---

## Collection Types Comparison

| Feature | `list` | `tuple` | `set` | `dict` |
|---------|--------|---------|-------|--------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` | `{"a": 1}` |
| Ordered | Yes | Yes | No | Yes (3.7+) |
| Mutable | Yes | No | Yes | Yes |
| Indexed | Yes | Yes | No | By key |
| Duplicates | Allowed | Allowed | Not allowed | Unique keys |
| Use case | Ordered sequence | Fixed collection | Unique items, set ops | Key-value mapping |

```python
# list — ordered, mutable, indexed
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits[0])          # "apple"

# tuple — ordered, immutable, indexed
coords = (10.5, 20.3)
# coords[0] = 5.0        # TypeError!
print(coords[1])          # 20.3

# set — unordered, mutable, no duplicates
unique = {1, 2, 2, 3}
print(unique)             # {1, 2, 3}
print(1 in unique)        # True

# dict — key-value mapping, mutable
person = {"name": "Alice", "age": 30}
person["age"] = 31
print(person.keys())      # dict_keys(['name', 'age'])
```

---

## Summary Table

| Type | Keyword | Example | Mutable | Notes |
|------|---------|---------|---------|-------|
| Integer | `int` | `x = 42` | No | Unlimited precision |
| Float | `float` | `x = 3.14` | No | IEEE 754 double-precision |
| String | `str` | `x = "hello"` | No | Unicode, many built-in methods |
| Boolean | `bool` | `x = True` | No | Subclass of `int` |
| None | `NoneType` | `x = None` | No | Single null value |
