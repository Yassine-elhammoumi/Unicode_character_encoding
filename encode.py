def byte_to_variation_selector(byte: int) -> str:
    if byte < 16:
        return chr(0xFE00 + byte)
    else:
        return chr(0xE0100 + (byte - 16))

def encode(base: str, byte_list: list[int]) -> str:
    result = base
    for byte in byte_list:
        result += byte_to_variation_selector(byte)
    return result

if __name__ == '__main__':
    conf_text = list(input("Enter the text you want to hide: ").encode('utf-8'))

    char_uni = input("Enter the character you want to hide the text in: ")
    
    encoded = encode(char_uni, conf_text)
    print("Encoded length:", len(encoded))

    
    print(f"Encoded: {encoded}")
