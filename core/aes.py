# def encrypt_block(plaintext: str, key: str, block_size: int = 4) -> str:
#     if not key:
#         raise ValueError("Key cannot be empty.")
#
#     padding_length = (block_size - len(plaintext) % block_size) % block_size
#     plaintext += 'X' * padding_length
#
#     ciphertext = ''
#     for i in range (0, len(plaintext), block_size):
#         block = plaintext[i:i+block_size]
#         encrypted_block = ''
#         for j in range(block_size):
#             p_char = block[j]
#             k_char = key[j % len(key)]
#             p_code = ord(p_char)
#             k_code = ord(k_char)
#             c_code = p_code ^ k_code
#             encrypted_block += chr(c_code)
#         ciphertext += encrypted_block
#     return ciphertext
#
# def decrypt_block(ciphertext, key: str, block_size: int = 4) -> str:
#     if not key:
#         raise ValueError("Key cannot be empty.")
#
#     plaintext = ''
#     for i in range(0, len(ciphertext), block_size):
#         block = ciphertext[i:i+block_size]
#         decrypted_block = ''
#         for j in range(block_size):
#             c_char = block[j]
#             k_char = key[j % len(key)]
#             c_code = ord(c_char)
#             k_code = ord(k_char)
#             p_code = c_code ^ k_code
#             decrypted_block += chr(p_code)
#         plaintext += decrypted_block
#     return plaintext.rstrip('X')

import base64

def encrypt_block(plaintext: str, key: str, block_size: int = 4) -> str:
    if not key:
        raise ValueError("Key cannot be empty.")

    padding_length = (block_size - len(plaintext) % block_size) % block_size
    plaintext += 'X' * padding_length

    ciphertext_bytes = bytearray()
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        for j in range(block_size):
            p_char = block[j]
            k_char = key[j % len(key)]
            p_code = ord(p_char)
            k_code = ord(k_char)
            c_code = p_code ^ k_code
            ciphertext_bytes.append(c_code)

    return base64.b64encode(ciphertext_bytes).decode('utf-8')

def decrypt_block(ciphertext: str, key: str, block_size: int = 4) -> str:
    if not key:
        raise ValueError("Key cannot be empty.")

    import base64
    ciphertext_bytes = base64.b64decode(ciphertext)

    plaintext = ''
    for i in range(0, len(ciphertext_bytes), block_size):
        block = ciphertext_bytes[i:i+block_size]
        for j in range(block_size):
            c_byte = block[j]
            k_char = key[j % len(key)]
            k_code = ord(k_char)
            p_code = c_byte ^ k_code
            plaintext += chr(p_code)

    return plaintext.rstrip('X')