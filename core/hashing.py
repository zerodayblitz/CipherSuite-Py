import hashlib

def hash_text(text: str, algorithm: str) -> str:
    text_bytes = text.encode('utf-8')

    try:
        hash_function = getattr(hashlib, algorithm.lower())
    except:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    hash_obj = hash_function()
    hash_obj.update(text_bytes)
    return hash_obj.hexdigest()

def hash_file(filepath: str, algorithm: str, chunk_size: int = 4096) -> str:
    try:
        hash_function = getattr(hashlib, algorithm.lower())
    except AttributeError:
        raise ValueError(f"Unsupported algorithm {algorithm}")

    hash_obj = hash_function()

    try:
        with open(filepath, 'rb') as file:
            while chunk := file.read(chunk_size):
                hash_obj.update(chunk)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found; {filepath}")
    return hash_obj.hexdigest()