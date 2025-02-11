import base64 # Importing the base64 module

string1="My name is Rahul"
print("string1:",string1)

Encoded_string1=base64.b64encode(string1.encode('utf-8'))
# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
# The b64encode() method encodes the string, using the base64 encoding. This encoding is designed to make binary data survive transport through transport layers that are not 8-bit clean, such as mail bodies.
print("Encoded_string1:",Encoded_string1)

print(type(Encoded_string1)) # <class 'bytes'>

Decoded_string1=base64.b64decode(Encoded_string1).decode('utf-8')
# The b64decode() method decodes the string, using the base64 encoding. This encoding is designed to make binary data survive transport through transport layers that are not 8-bit clean, such as mail bodies.
# if we don't use decode('utf-8') then it will return bytes
print("Decoded_string1:",Decoded_string1)