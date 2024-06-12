When you store something as binary data using the Pickle module in Python, the data is not base64 encoded. Let me clarify the difference between binary data and base64 encoding:

1. **Binary Data:**
   - Binary data refers to data that is stored in a binary format, which is the raw form that the computer uses. When you use the Pickle module to serialize an object, it converts the object into a byte stream (a sequence of bytes) that represents the object in a way that can be stored or transmitted and later reconstructed.

2. **Base64 Encoding:**
   - Base64 encoding is a method of converting binary data into an ASCII string format. This is often used for transmitting binary data over text-based protocols (like email) that require ASCII text. Base64 encoding increases the size of the data by about 33%.

When you pickle an object using the Pickle module, the resulting serialized data is binary, not base64 encoded. If you look at the serialized data, it will appear as a sequence of bytes, which might include non-printable characters.

However, if you need to store or transmit this binary data in a medium that requires text (like JSON, XML, or some text-based protocols), you might encode the binary data into a base64 string. In that case, you'd manually convert the pickled binary data to a base64 string before transmission or storage.

Here’s an example to illustrate this:

```python
import pickle
import base64

# Create a Python object
data = {'key': 'value'}

# Serialize the object using pickle (binary format)
pickled_data = pickle.dumps(data)

# If needed, encode the binary data into a base64 string
base64_encoded_data = base64.b64encode(pickled_data).decode('utf-8')

print(f"Binary pickled data: {pickled_data}")
print(f"Base64 encoded data: {base64_encoded_data}")

# To decode and deserialize back to original object
decoded_data = base64.b64decode(base64_encoded_data)
original_data = pickle.loads(decoded_data)

print(f"Original data: {original_data}")
```

In summary:
- **Pickling** converts an object to binary data.
- **Base64 encoding** converts binary data to a text string format.
- Pickled data is not base64 encoded by default, but you can encode it if needed for specific use cases.