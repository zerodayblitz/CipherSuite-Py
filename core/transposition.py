def encrypt_transposition(plaintext: str, key: str) -> str:
    cleaned = plaintext.replace(" ", "").upper()
    num_cols = len(key)
    num_rows = -(-len(cleaned) // num_cols)

    padded_length = num_cols * num_rows
    cleaned += 'X' * (padded_length - len(cleaned))
    grid = [list(cleaned[i:i+num_cols]) for i in range(0, len(cleaned), num_cols)]

    key_order = sorted([(char,i) for i, char in enumerate(key)])
    sorted_indices = [index for (char, index) in key_order]

    ciphertext = ''
    for col in sorted_indices:
        for row in grid:
            ciphertext += row[col]
    return ciphertext
def decrypt_transposition(ciphertext: str, key: str) -> str:
    # determine grid size
    num_cols = len(key)
    num_rows = -(-len(ciphertext) // num_cols)

    # calculate how many cells were padded
    total_cells = num_cols * num_rows
    padding = total_cells - len(ciphertext)
    key_order = sorted([(char, i) for i, char in enumerate(key)])
    sorted_indices = [index for (char, index) in key_order]

    # extract order of columns based on key
    col_lengths = [num_rows] * num_cols
    for i in sorted_indices[-padding:]:
        col_lengths[i] -= 1

    # slice ciphertext int columns
    cols = {}
    start = 0
    for idx in sorted_indices:
        length = col_lengths[idx]
        cols[idx] = list(ciphertext[start:start + length])
        start += length
    plaintext = ''
    for row in range(num_rows):
        for col in range(num_cols):
            if row < len(cols[col]):
                plaintext += cols[col][row]
    return plaintext