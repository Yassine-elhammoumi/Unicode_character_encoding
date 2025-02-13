def variation_selector_to_byte(variation_selector: str) -> int | None:
    codepoint = ord(variation_selector)
    if 0xFE00 <= codepoint <= 0xFE0F:
        return codepoint - 0xFE00
    elif 0xE0100 <= codepoint <= 0xE01EF:
        return codepoint - 0xE0100 + 16
    else:
        return None

def decode(variation_selectors: str) -> list[int]:
    result = []
    # Skip the base character
    for ch in variation_selectors[1:]:
        byte = variation_selector_to_byte(ch)
        if byte is not None:
            result.append(byte)
        # Instead of breaking, just ignore non-variation selectors.
    return result

if __name__ == '__main__':
    encoded = input("Enter the encoded text: ")
    decoded_bytes = decode(encoded)
    try:
        decoded_text = bytes(decoded_bytes).decode('utf-8')
    except Exception as e:
        decoded_text = f"Decoding error: {e}"
    print(f"Decoded: {decoded_text}")
