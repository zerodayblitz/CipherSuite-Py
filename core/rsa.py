def generate_keys():
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key
def encrypt_rsa(plaintext: str, public_key: tuple) -> list:
    e, n = public_key
    ciphertext = []
    for char in plaintext:
        m = ord(char)
        c = pow(m, e, n)
        ciphertext.append(c)
    return ciphertext
def decrypt_rsa(ciphertext: list, private_key: tuple) -> str:
    d, n = private_key
    plaintext = ''
    for c in ciphertext:
        m = pow(c, d, n)
        plaintext += chr(m)
    return plaintext