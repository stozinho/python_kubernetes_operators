### Unicode and UTF-8 Explained

**Unicode** and **UTF-8** are standards used for encoding text in computers.

#### Unicode
- **Unicode** is a character encoding standard designed to support text and symbols from all writing systems around the world.
- It assigns a unique number, called a code point, to every character. For example:
  - The character 'A' is U+0041.
  - The character '漢' is U+6F22.

#### UTF-8
- **UTF-8** (Unicode Transformation Format - 8-bit) is a variable-width character encoding for Unicode.
- It can encode each Unicode character in one to four bytes.
  - ASCII characters (0-127) are encoded in one byte, making UTF-8 backward compatible with ASCII.
  - Characters from other languages and symbols use two, three, or four bytes.

### Python Examples

Python provides built-in support for Unicode and UTF-8. Here are some examples demonstrating how to work with these encodings.

#### Basic Unicode and UTF-8 Encoding/Decoding

1. **Encoding a string to UTF-8 bytes:**
   ```python
   text = "Hello, 世界"
   utf8_encoded = text.encode('utf-8')
   print(utf8_encoded)
   ```

   Output:
   ```
   b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
   ```

2. **Decoding UTF-8 bytes to a string:**
   ```python
   utf8_bytes = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
   decoded_text = utf8_bytes.decode('utf-8')
   print(decoded_text)
   ```

   Output:
   ```
   Hello, 世界
   ```

#### Handling Unicode Characters

1. **Unicode string and its code points:**
   ```python
   text = "Hello, 世界"
   for char in text:
       print(f'Character: {char}, Unicode code point: U+{ord(char):04X}')
   ```

   Output:
   ```
   Character: H, Unicode code point: U+0048
   Character: e, Unicode code point: U+0065
   Character: l, Unicode code point: U+006C
   Character: l, Unicode code point: U+006C
   Character: o, Unicode code point: U+006F
   Character: ,, Unicode code point: U+002C
   Character:  , Unicode code point: U+0020
   Character: 世, Unicode code point: U+4E16
   Character: 界, Unicode code point: U+754C
   ```

2. **Working with Unicode in file I/O:**
   ```python
   # Writing Unicode text to a file
   with open('example.txt', 'w', encoding='utf-8') as f:
       f.write("Hello, 世界")

   # Reading Unicode text from a file
   with open('example.txt', 'r', encoding='utf-8') as f:
       content = f.read()
       print(content)
   ```

   Output:
   ```
   Hello, 世界
   ```

These examples demonstrate basic operations with Unicode and UTF-8 in Python, showcasing how to encode, decode, and handle Unicode characters in various contexts.

## `chr()`

`chr()` prints a unicode code point (and ASCII - 0-127 is ASCII, and can be represented in a single byte). 

```python
print(chr(65))  # Output: 'A'
print(chr(8364))  # Output: '€'
```