# Python Fundamentals

## 1 - Comparison Operators

| Operator | Description | Example |
| --- | --- | --- |
| `==` | Equal to | `5 == 5` -> `True` |
| `!=` | Not equal to | `5 != 3` -> `True` |
| `>` | Greater than | `7 > 4` -> `True` |
| `<` | Less than | `2 < 9` -> `True` |
| `>=` | Greater than or equal to | `6 >= 6` -> `True` |
| `<=` | Less than or equal to | `3 <= 8` -> `True` |
| `is` | True if both variables reference the same object | `a = [1]; b = a; a is b` -> `True` |
| `is not` | True if variables reference different objects | `a = [1]; b = [1]; a is not b` -> `True` |
| `in` | True if a value exists in a sequence | `'a' in "apple"` -> `True` |
| `not in` | True if a value does not exist in a sequence | `'z' not in "apple"` -> `True` |

### More Examples

#### Equal To `==`
- `10 == 10` -> `True`
- `'cat' == 'cat'` -> `True`
- `[1, 2] == [1, 2]` -> `True`

#### Not Equal To `!=`
- `10 != 5` -> `True`
- `'apple' != 'orange'` -> `True`
- `3 != 3` -> `False`

#### Greater Than `>`
- `9 > 4` -> `True`
- `2 > 7` -> `False`
- `100 > 99` -> `True`

#### Less Than `<`
- `1 < 8` -> `True`
- `5 < 5` -> `False`
- `-3 < 0` -> `True`

#### Greater Than or Equal To `>=`
- `8 >= 8` -> `True`
- `9 >= 3` -> `True`
- `2 >= 10` -> `False`

#### Less Than or Equal To `<=`
- `4 <= 4` -> `True`
- `1 <= 9` -> `True`
- `12 <= 7` -> `False`

#### Is (Same Object) `is`
- `a = [1, 2]; b = a; a is b` -> `True`
- `x = 256; y = 256; x is y` -> `True` (often)
- `m = [1]; n = [1]; m is n` -> `False`

#### Is Not (Different Object) `is not`
- `a = [1]; b = [1]; a is not b` -> `True`
- `x = None; x is not None` -> `False`
- `p = 'hi'; q = p; p is not q` -> `False`

#### In (Membership) `in`
- `'a' in 'banana'` -> `True`
- `3 in [1, 2, 3, 4]` -> `True`
- `'key' in {'key': 1, 'value': 2}` -> `True`

#### Not In (Membership) `not in`
- `'z' not in 'banana'` -> `True`
- `5 not in [1, 2, 3]` -> `True`
- `'id' not in {'name': 'Ava'}` -> `True`

### Advanced Comparison Tricks

#### 1) Compare strings safely (case-insensitive)
- `'Admin'.casefold() == 'ADMIN'.casefold()` -> `True`
- `'Straße'.casefold() == 'STRASSE'.casefold()` -> `True`

#### 2) Compare floats with tolerance (not strict `==`)
- `0.1 + 0.2 == 0.3` -> `False`
- `import math; math.isclose(0.1 + 0.2, 0.3)` -> `True`

#### 3) Use tuple/list lexicographic comparisons
- `(1, 9) < (2, 0)` -> `True`
- `[1, 'a'] < [1, 'b']` -> `True`

#### 4) Set comparisons use subset/superset meaning
- `{1, 2} < {1, 2, 3}` -> `True` (proper subset)
- `{1, 2} <= {1, 2}` -> `True` (subset or equal)

#### 5) Know `==` vs `is` in real code
- `a = [1, 2]; b = [1, 2]; a == b` -> `True`
- `a = [1, 2]; b = [1, 2]; a is b` -> `False`
- `x = None; x is None` -> `True` (preferred style for `None` checks)

#### 6) Membership with dictionaries checks keys
- `'name' in {'name': 'Ava', 'age': 20}` -> `True`
- `'Ava' in {'name': 'Ava', 'age': 20}` -> `False`

## 2 - Chained Comparisons

Chained comparisons let you combine multiple comparisons in a single expression.
For example, `x < y < z` means `x < y and y < z`, but `y` is evaluated only once.
Python evaluates chained comparisons from left to right and stops as soon as one part is `False`.

### Chained Comparison Examples

- `1 < 5 < 10` -> `True`
- `score = 85; 0 <= score <= 100` -> `True`
- `a, b, c = 2, 5, 3; a < b > c` -> `True`

```python
age = 25
is_valid_age = 18 <= age < 65
print(is_valid_age)
```

Output:

```text
True
```

## 3 - Conditional Statements

Conditional statements let your program make decisions.
Use `if` to check a condition, `elif` for additional conditions, and `else` for a fallback case.
Python uses indentation to define each block, so spacing is required and meaningful.

### Conditional Statement Examples

#### 1) Basic `if`

```python
temperature = 34

if temperature > 30:
    print("It is a hot day")
```

Output:

```text
It is a hot day
```

#### 2) `if` + `else`

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Odd
```

#### 3) `if` + `elif` + `else`

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

Output:

```text
Grade B
```

#### 4) Multiple conditions with `and`

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
```

Output:

```text
Entry allowed
```

## 4 - Loops

Loops let you run a block of code multiple times without writing the same lines again.
In Python, the two main loop types are `for` (iterate over items) and `while` (repeat while a condition is `True`).
You can also control loops using `break` (stop early) and `continue` (skip current iteration).

### The `range()` Function

`range()` is used to generate a sequence of numbers, mostly inside `for` loops.
The `stop` value is not included in the result.

- `range(stop)` -> starts from `0` and goes up to `stop - 1`
- `range(start, stop)` -> starts from `start` and goes up to `stop - 1`
- `range(start, stop, step)` -> moves by `step` each time (step can be negative)

```python
print(list(range(5)))
print(list(range(2, 6)))
print(list(range(10, 2, -2)))
```

Output:

```text
[0, 1, 2, 3, 4]
[2, 3, 4, 5]
[10, 8, 6, 4]
```

### Loop Examples

#### 1) `for` loop with a list

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
apple
banana
mango
```

#### 2) `for` loop with `range()`

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

### Intermediate Loop Examples

#### 1) `for` loop to sum even numbers

```python
numbers = [12, 7, 5, 10, 8]
total = 0

for n in numbers:
    if n % 2 == 0:
        total += n

print("Sum of even numbers:", total)
```

Output:

```text
Sum of even numbers: 30
```

#### 2) `while` loop for factorial

```python
n = 5
factorial = 1

while n > 1:
    factorial *= n
    n -= 1

print("Factorial:", factorial)
```

Output:

```text
Factorial: 120
```

### Advanced Loop Examples

#### 1) `for` + `else` to check prime number

```python
n = 29

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print(n, "is not prime")
        break
else:
    print(n, "is prime")
```

Output:

```text
29 is prime
```

#### 2) `while` + `else` for retry logic

```python
attempt = 1
max_attempts = 3
pin = "2580"
entered_pin = ["1111", "9999", "2580"]

while attempt <= max_attempts:
    current = entered_pin[attempt - 1]
    if current == pin:
        print("Access granted on attempt", attempt)
        break
    print("Wrong PIN on attempt", attempt)
    attempt += 1
else:
    print("Card blocked")
```

Output:

```text
Wrong PIN on attempt 1
Wrong PIN on attempt 2
Access granted on attempt 3
```

#### 3) Nested `for` loops for matrix transpose

```python
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = []

for col in range(len(matrix[0])):
    new_row = []
    for row in range(len(matrix)):
        new_row.append(matrix[row][col])
    transpose.append(new_row)

print(transpose)
```

Output:

```text
[[1, 4], [2, 5], [3, 6]]
```

#### 4) `while` loop

```python
count = 1

while count <= 3:
    print("Count:", count)
    count += 1
```

Output:

```text
Count: 1
Count: 2
Count: 3
```

#### 5) `break` and `continue`

```python
for n in range(1, 8):
    if n == 3:
        continue  # skip 3
    if n == 6:
        break  # stop loop at 6
    print(n)
```

Output:

```text
1
2
4
5
```

#### 6) `for` loop with `enumerate()`

`enumerate()` lets you loop through items and their index at the same time (`start=1` begins indexing from 1).

```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors, start=1):
    print(index, color)
```

Output:

```text
1 red
2 green
3 blue
```

#### 7) Loop through dictionary items

```python
student = {"name": "Ava", "age": 20, "grade": "A"}

for key, value in student.items():
    print(key, "->", value)
```

Output:

```text
name -> Ava
age -> 20
grade -> A
```

#### 8) Nested `for` loops

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)
```

Output:

```text
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
```

#### 9) `while True` with `break`

```python
num = 1

while True:
    print(num)
    num += 1
    if num > 5:
        break
```

Output:

```text
1
2
3
4
5
```

## 5 - Functions in Python

Functions are reusable blocks of code that perform a specific task.
In Python, you define a function using the `def` keyword.
Functions can take inputs (parameters), can return output using `return`, and help avoid repeating the same logic.

### Basic Function Syntax

```python
def function_name(parameters):
    # function body
    return value  # optional
```

### Function Examples

#### 1) Function with no parameters and no return value

```python
def greet():
    print("Hello, learner!")


greet()
```

Output:

```text
Hello, learner!
```

#### 2) Function with parameters and return value

```python
def add(a, b):
    return a + b


result = add(10, 5)
print(result)
```

Output:

```text
15
```

#### 3) Function with default argument

```python
def power(base, exponent=2):
    return base ** exponent


print(power(4))
print(power(4, 3))
```

Output:

```text
16
64
```

#### 4) Function called with keyword arguments

```python
def introduce(name, city):
    print(name, "lives in", city)


introduce(city="Lahore", name="Ava")
```

Output:

```text
Ava lives in Lahore
```

#### 5) Function with variable positional arguments (`*args`)

```python
def total_sum(*numbers):
    return sum(numbers)


print(total_sum(1, 2, 3))
print(total_sum(10, 20, 30, 40))
```

Output:

```text
6
100
```

#### 6) Function with variable keyword arguments (`**kwargs`)

```python
def show_profile(**details):
    for key, value in details.items():
        print(key, "->", value)


show_profile(name="Ava", role="Engineer", experience=3)
```

Output:

```text
name -> Ava
role -> Engineer
experience -> 3
```

#### 7) Function returning multiple values

```python
def min_max(values):
    return min(values), max(values)


smallest, largest = min_max([12, 4, 19, 7])
print("Min:", smallest)
print("Max:", largest)
```

Output:

```text
Min: 4
Max: 19
```

#### 8) Recursive function

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
```

Output:

```text
120
```

## 6 - Lambda Function

Lambda functions are small anonymous functions created with the `lambda` keyword.
They can take multiple arguments, but they can contain only one expression.
They are useful for short operations, especially with `sorted()`, `map()`, and `filter()`.

### Lambda Function Syntax

```python
lambda arguments: expression
```

### Lambda Function Examples

#### 1) Add two numbers

```python
add = lambda a, b: a + b
print(add(4, 6))
```

Output:

```text
10
```

#### 2) Square a number

```python
square = lambda n: n * n
print(square(7))
```

Output:

```text
49
```

#### 3) Use lambda with `sorted()`

```python
students = [("Ava", 22), ("Zain", 19), ("Mina", 21)]
by_age = sorted(students, key=lambda item: item[1])
print(by_age)
```

Output:

```text
[('Zain', 19), ('Mina', 21), ('Ava', 22)]
```

#### 4) Use lambda with `map()`

```python
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
```

Output:

```text
[2, 4, 6, 8]
```

#### 5) Use lambda with `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
```

Output:

```text
[2, 4, 6]
```

#### 6) Lambda with conditional expression

```python
label = lambda n: "positive" if n > 0 else "zero" if n == 0 else "negative"
print(label(-3))
print(label(0))
print(label(8))
```

Output:

```text
negative
zero
positive
```

### When Not to Use Lambda

Use a normal `def` function instead of `lambda` when:

- The logic needs multiple statements (loops, `try/except`, multiple `return` points).
- The expression becomes too long and hurts readability.
- You want a clear function name for debugging, stack traces, or reuse.
- You want to add a docstring or type hints for better documentation.

```python
# Less readable with lambda
result = list(map(lambda n: n * 2 if n % 2 == 0 else n * 3, [1, 2, 3, 4]))


# Clearer with def
def transform(n):
    if n % 2 == 0:
        return n * 2
    return n * 3


result = list(map(transform, [1, 2, 3, 4]))
print(result)
```

Output:

```text
[3, 4, 9, 8]
```
