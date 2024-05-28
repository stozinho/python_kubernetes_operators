Here's a summary of frequently used Python standard library modules along with examples for each:

### 1. `collections`
This module provides alternatives to Python’s general-purpose built-in containers like `list`, `dict`, etc.

- **Example: `defaultdict`**
  ```python
  from collections import defaultdict

  dd = defaultdict(int)
  dd['apple'] += 1
  print(dd)  # defaultdict(<class 'int'>, {'apple': 1})
  ```

- **Example: `Counter`**
  ```python
  from collections import Counter

  words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
  count = Counter(words)
  print(count)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})
  ```

### 2. `datetime`
This module supplies classes for manipulating dates and times.

- **Example: Current date and time**
  ```python
  from datetime import datetime

  now = datetime.now()
  print(now)  # e.g., 2023-10-23 10:19:15.123456
  ```

- **Example: Formatting dates**
  ```python
  from datetime import datetime

  now = datetime.now()
  print(now.strftime("%Y-%m-%d %H:%M:%S"))  # e.g., 2023-10-23 10:19:15
  ```

### 3. `json`
This module provides methods to parse JSON into Python dictionaries and vice versa.

- **Example: Parse JSON string**
  ```python
  import json

  json_string = '{"name": "John", "age": 30}'
  data = json.loads(json_string)
  print(data)  # {'name': 'John', 'age': 30}
  ```

- **Example: Convert Python dict to JSON string**
  ```python
  import json

  data = {'name': 'John', 'age': 30}
  json_string = json.dumps(data)
  print(json_string)  # {"name": "John", "age": 30}
  ```

### 4. `itertools`
This module provides functions that create iterators for efficient looping.

- **Example: `chain`**
  ```python
  import itertools

  a = [1, 2, 3]
  b = [4, 5, 6]
  combined = itertools.chain(a, b)
  print(list(combined))  # [1, 2, 3, 4, 5, 6]
  ```

- **Example: `permutations`**
  ```python
  import itertools

  perm = itertools.permutations([1, 2, 3])
  for p in perm:
      print(p)
  # (1, 2, 3)
  # (1, 3, 2)
  # (2, 1, 3)
  # (2, 3, 1)
  # (3, 1, 2)
  # (3, 2, 1)
  ```

### 5. `os`
This module provides a way of using operating system dependent functionality like reading or writing to the file system.

- **Example: List files in a directory**
  ```python
  import os

  files = os.listdir('.')
  print(files)
  ```

- **Example: Environment variables**
  ```python
  import os

  path = os.getenv('PATH')
  print(path)
  ```

### 6. `re`
This module provides support for regular expressions.

- **Example: Simple match**
  ```python
  import re

  pattern = r'\d+'
  text = 'The year is 2023'
  match = re.search(pattern, text)
  if match:
      print(match.group())  # 2023
  ```

- **Example: Find all matches**
  ```python
  import re

  pattern = r'\b\w+\b'
  text = 'This is a test.'
  matches = re.findall(pattern, text)
  print(matches)  # ['This', 'is', 'a', 'test']
  ```

### 7. `sys`
This module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.

- **Example: Command-line arguments**
  ```python
  import sys

  args = sys.argv
  print(args)  # e.g., ['script.py', 'arg1', 'arg2']
  ```

- **Example: Exiting a script**
  ```python
  import sys

  print("Exiting script")
  sys.exit()
  ```

### 8. `functools`
This module provides higher-order functions that act on or return other functions.

- **Example: `partial`**
  ```python
  from functools import partial

  def multiply(x, y):
      return x * y

  double = partial(multiply, 2)
  print(double(5))  # 10
  ```

- **Example: `lru_cache`**
  ```python
  from functools import lru_cache

  @lru_cache(maxsize=32)
  def fib(n):
      if n < 2:
          return n
      return fib(n-1) + fib(n-2)

  print(fib(10))  # 55
  ```

These examples cover common uses of these modules and provide a basis for understanding how they can be applied to real-world problems.