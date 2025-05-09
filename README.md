# 🔐 CipherSuite-Py

**CipherSuite-Py** is a command-line encryption and hashing toolkit built with Python. It offers an easy-to-use interface for experimentation with various classical and modern cryptographic techniques. This tool serves as a hands-on learning platform for understanding the fundamentals of encryption and hashing. Each cipher is implemented in a modular fashion, allowing users to explore and compare different cryptographic methods.

---

## 📌 Features
### 🔍 Ciphers Implemented

- **Caesar Cipher** – Classic letter-shifting encryption
- **Transposition Cipher** – Columnar transposition with customizable keys
- **Vernam Cipher** – One-Time Pad XOR encryption
- **Stream Cipher** – Basic XOR-based stream cipher
- **Block Cipher** – Simplified AES-like block encryption
- **RSA Encryption** – Asymmetric encryption with key generation
- **Hashing** – Supports MD5, SHA-1, SHA-256, and SHA-512 for text and files
### 🔐 Hashing Support

Hash both text and files using:

- **MD5**
- **SHA-1**
- **SHA-256**
- **SHA-512**
---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. **Clone the repository and navigate to the tool:**

   ```bash
   git clone https://github.com/zerodayblitz/CipherSuite-Py.git
   cd CipherSuite-Py
2. **Run the tool**

   ```bash
   python main.py

## 🛠️ Usage
### Sample Run

```
$ python main.py
Choose an option:
1) Caesar Cipher
2) Transposition Cipher
3) Vernam Cipher (One-Time Pad XOR)
4) Stream Cipher (Basic XOR)
5) Block Cipher (AES)
6) Asymmetric Encryption (RSA)
7) Hashing
Enter your choice (1-7), or 'q' to quit: 1

[ Caesar Cipher Selected ] — (type 'b' to go back)
Encrypt or Decrypt? (e/d): e
Enter your message: hello world
Enter shift value (e.g., 3): 3
Encrypted message: khoor zruog

Done. Returning to main menu...
```

---

## 🧰 Technologies Used

- Python 3.6+
- Standard Python libraries:
  - `random`
  - `hashlib`
  - `time`

---

## 👤 Author

**[zerodayblitz](https://github.com/zerodayblitz)**  
