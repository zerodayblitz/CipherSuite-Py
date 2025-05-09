def encrypt_caesar(plaintext: str, shift: int) -> str:
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            ciphertext += chr(shifted)
        else:
            ciphertext += char
    return ciphertext
def decrypt_caesar(ciphertext: str, shift: int) -> str:
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - shift) % 26 + base
            plaintext += chr(shifted)
        else:
            plaintext += char
    return plaintext
