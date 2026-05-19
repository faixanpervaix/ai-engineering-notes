# Python Fundamentals

## Comparison Operators

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

## Chained Comparisons

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

## Conditional Statements

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

## Loops

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

#### 3) `while` loop

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

#### 4) `break` and `continue`

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

#### 5) `for` loop with `enumerate()`

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

#### 6) Loop through dictionary items

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

#### 7) Nested `for` loops

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

#### 8) `while True` with `break`

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
