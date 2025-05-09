import base64
import random

def encrypt_stream(plaintext: str, key: str) -> str:
    if not key:
        raise ValueError("Key cannot be empty.")

    seed = sum(ord(char) for char in key)
    random.seed(seed)

    ciphertext_bytes = bytes([ord(char) ^ random.randint(0, 255) for char in plaintext])
    return base64.b64encode(ciphertext_bytes).decode('utf-8')

def decrypt_stream(ciphertext: str, key: str) -> str:
    if not key:
        raise ValueError("Key cannot be empty.")

    seed = sum(ord(char) for char in key)
    random.seed(seed)

    ciphertext_bytes = base64.b64decode(ciphertext)
    plaintext = ''.join(chr(b ^ random.randint(0, 255)) for b in ciphertext_bytes)
    return plaintext
