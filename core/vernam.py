# def encrypt_vernam(plaintext: str, key: str) -> str:
#     if len(plaintext) != len(key):
#         raise ValueError("Key must be the same length as plaintext.")
#
#     ciphertext = ''
#     for p_char, k_char in zip(plaintext, key):
#         p_code = ord(p_char)
#         k_code = ord(k_char)
#         c_code = p_code ^ k_code
#         ciphertext += chr(c_code)
#     return ciphertext
# def decrypt_vernam(ciphertext: str, key: str) -> str:
#     if len(ciphertext) != len(key):
#         raise ValueError("Key must be the same length as plaintext.")
#     plaintext = ''
#     for c_char, k_char in zip(ciphertext, key):
#         c_code = ord(c_char)
#         k_code = ord(k_char)
#         p_code = c_code ^ k_code
#         plaintext += chr(p_code)
#     return plaintext

import base64

def encrypt_vernam(plaintext: str, key: str) -> str:
    if len(plaintext) != len(key):
        raise ValueError("Key must be the same length as plaintext.")

    ciphertext_bytes = bytes([ord(p) ^ ord(k) for p, k in zip(plaintext, key)])
    return base64.b64encode(ciphertext_bytes).decode('utf-8')

def decrypt_vernam(ciphertext: str, key: str) -> str:
    ciphertext_bytes = base64.b64decode(ciphertext)
    if len(ciphertext_bytes) != len(key):
        raise ValueError("Key must be the same length as ciphertext.")

    plaintext = ''.join(chr(c ^ ord(k)) for c, k in zip(ciphertext_bytes, key))
    return plaintext