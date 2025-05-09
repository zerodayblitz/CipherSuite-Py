from core.caesar import encrypt_caesar, decrypt_caesar
from core.transposition import encrypt_transposition, decrypt_transposition
from core.vernam import encrypt_vernam, decrypt_vernam
from core.stream import encrypt_stream, decrypt_stream
from core.aes import encrypt_block, decrypt_block
from core.rsa import generate_keys, encrypt_rsa, decrypt_rsa
from core.hashing import hash_text, hash_file
import time

def menu():
    print("Choose an option:")
    print("1) Caesar Cipher")
    print("2) Transposition Cipher")
    print("3) Vernam Cipher (One-Time Pad XOR)")
    print("4) Stream Cipher (Basic XOR)")
    print("5) Block Cipher (AES)")
    print("6) Asymmetric Encryption (RSA)")
    print("7) Hashing")

def back_prompt(prompt):
    response = input(prompt)
    if response.strip().lower() == 'b':
        return None
    return response

def pause():
    print("\nDone. Returning to main menu...")
    time.sleep(3)

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-7), or 'q' to quit: ").strip().lower()

        if choice == 'q':
            print("Goodbye!")
            break

        elif choice == '1':
            print("\n[ Caesar Cipher Selected ] — (type 'b' to go back)")
            mode = back_prompt("Encrypt or Decrypt? (e/d): ")
            if mode is None: continue
            text = back_prompt("Enter your message: ")
            if text is None: continue
            shift_input = back_prompt("Enter shift value (e.g., 3): ")
            if shift_input is None: continue
            try:
                shift = int(shift_input)
            except ValueError:
                print("Shift must be an integer.")
                continue

            if mode == 'e':
                print(f"Encrypted message: {encrypt_caesar(text, shift)}")
            elif mode == 'd':
                print(f"Decrypted message: {decrypt_caesar(text, shift)}")
            else:
                print("Invalid mode.")
            pause()

        elif choice == '2':
            print("\n[ Transposition Cipher Selected ] - (type 'b' to go back)")
            mode = back_prompt("Encrypt or Decrypt? (e/d): ")
            if mode is None: continue
            text = back_prompt("Enter your message: ")
            if text is None: continue
            key = back_prompt("Enter a key (e.g., ENCRYPT): ")
            if key is None: continue
            if mode == 'e':
                print(f"Encrypted message: {encrypt_transposition(text, key)}")
            elif mode == 'd':
                print(f"Decrypted message: {decrypt_transposition(text, key)}")
            else:
                print("Invalid mode.")
            pause()

        elif choice == '3':
            print("\n[ Vernam Cipher Selected ] - (type 'b' to go back)")
            mode = back_prompt("Encrypt or Decrypt? (e/d): ")
            if mode is None: continue
            text = back_prompt("Enter your message: ")
            if text is None: continue
            key = back_prompt("Enter a key: ")
            if key is None: continue
            if len(text) != len(key):
                print("Key must be the same length as the message.")
                continue

            if mode == 'e':
                print(f"Encrypted message: {encrypt_vernam(text, key)}")
            elif mode == 'd':
                print(f"Decrypted message: {decrypt_vernam(text, key)}")
            else:
                print("Invalid mode.")
            pause()

        elif choice == '4':
            print("\n[ Stream Cipher Selected ] - (type 'b' to go back)")
            mode = back_prompt("Encrypt or Decrypt? (e/d): ")
            if mode is None: continue
            text = back_prompt("Enter your message: ")
            if text is None: continue
            key = back_prompt("Enter a key: ")
            if key is None: continue

            if mode == 'e':
                print(f"Encrypted message: {encrypt_stream(text, key)}")
            elif mode == 'd':
                print(f"Decrypted message: {decrypt_stream(text, key)}")
            else:
                print("Invalid mode.")
            pause()

        elif choice == '5':
            print("\n[ Block Cipher Selected ] - (type 'b' to go back)")
            mode = back_prompt("Encrypt or Decrypt? (e/d): ")
            if mode is None: continue
            text = back_prompt("Enter your message: ")
            if text is None: continue
            key = back_prompt("Enter a key: ")
            if key is None: continue

            if mode == 'e':
                print(f"Encrypted message: {encrypt_block(text, key)}")
            elif mode == 'd':
                print(f"Decrypted message: {decrypt_block(text, key)}")
            else:
                print("Invalid mode.")
            pause()

        elif choice == '6':
            print("\n[ RSA Asymmetric Encryption Selected ] - (type 'b' to go back)")
            public_key, private_key = generate_keys()
            mode = back_prompt("Encrypt or Decrypt? (e/d): ")
            if mode is None: continue

            if mode == 'e':
                plaintext = back_prompt("Enter message to encrypt: ")
                if plaintext is None: continue
                print(f"Encrypted (numeric list): {encrypt_rsa(plaintext, public_key)}")
            elif mode == 'd':
                raw = back_prompt("Enter the encrypted numbers (comma-separated): ")
                if raw is None: continue
                try:
                    encrypted = [int(num.strip()) for num in raw.split(',')]
                    print(f"Decrypted message: {decrypt_rsa(encrypted, private_key)}")
                except ValueError:
                    print("Invalid input. Must be comma-separated numbers.")
            else:
                print("Invalid mode.")
            pause()

        elif choice == '7':
            print("\n[ Hashing Selected ] - (type 'b' to go back)")
            print("Choose an algorithm:")
            print("1) MD5")
            print("2) SHA-1")
            print("3) SHA-256")
            print("4) SHA-512")
            algo_choice = back_prompt("Enter choice (1-4): ")
            if algo_choice is None: continue
            algo_map = {'1': 'md5', '2': 'sha1', '3': 'sha256', '4': 'sha512'}
            algorithm = algo_map.get(algo_choice)
            if not algorithm:
                print("Invalid algorithm choice.")
                continue
            mode = back_prompt("Hash [T]ext or [F]ile? ")
            if mode is None: continue
            if mode.lower() == 't':
                text = back_prompt("Enter the text to hash: ")
                if text is None: continue
                try:
                    print(f"\n{algorithm.upper()} digest: {hash_text(text, algorithm)}")
                except ValueError as ve:
                    print(f"Error: {ve}")
            elif mode.lower() == 'f':
                filepath = back_prompt("Enter path to the file: ")
                if filepath is None: continue
                try:
                    print(f"\n{algorithm.upper()} digest of file: {hash_file(filepath, algorithm)}")
                except (FileNotFoundError, ValueError) as e:
                    print(f"Error: {e}")
            else:
                print("Invalid option. Please enter 'T' or 'F'.")
            pause()
        else:
            print("Invalid choice. Please enter a number from 1 to 7 or 'q' to quit.")

if __name__ == "__main__":
    main()