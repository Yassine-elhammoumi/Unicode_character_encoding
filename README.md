# Unicode Character Encoding

This repository demonstrates how to hide a message within a base character using Unicode variation selectors in Python. [Variation selectors](https://en.wikipedia.org/wiki/Variation_Selectors_(Unicode_block)) are special Unicode characters that modify the appearance of preceding characters, allowing for the embedding of hidden information.

## How It Works

The process involves two functions: `encode` and `decode`.

### Encoding

1. **Convert the Message to Bytes:**
   - The input message is converted into a list of bytes using UTF-8 encoding.

2. **Map Bytes to Variation Selectors:**
   - Each byte is mapped to a corresponding variation selector character.
   - Bytes less than 16 are mapped to the range U+FE00 to U+FE0F.
   - Bytes 16 and above are mapped to the range U+E0100 to U+E01EF.

3. **Construct the Encoded String:**
   - The base character is prepended to the sequence of variation selectors to form the final encoded string.

### Decoding

1. **Extract Variation Selectors:**
   - The base character is removed, leaving only the variation selectors.

2. **Map Variation Selectors Back to Bytes:**
   - Each variation selector is mapped back to its corresponding byte value.

3. **Reconstruct the Original Message:**
   - The list of bytes is decoded back into the original message using UTF-8 decoding.


## Example Usage
![til](https://github.com/Yassine-elhammoumi/Unicode_character_encoding/blob/main/assets/screen.gif?raw=true)
## References

- [Variation Selectors (Unicode block)](https://en.wikipedia.org/wiki/Variation_Selectors_%28Uncode_block%29)
- [Unicode & Character Encodings in Python: A Painless Guide](https://realpython.com/python-enodings-guide/)
