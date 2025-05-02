# Crypto Ciphers

This project demonstrates simple implementations of a substitution cipher in Python.

## Files

- **Substitution.py**  
  Implements a monoalphabetic substitution cipher for encrypting and decrypting messages using a randomly generated key.

- **Substitution exam.py**  
  A simplified version of the cipher, designed to be as easy as possible for quick application in an exam setting.

## How It Works

- **Key Generation:**  
  A shuffled version of all printable ASCII characters (uppercase, lowercase, digits, punctuation, and space) is used as the cipher key.

- **Encryption:**  
  Each character in the message is replaced by the character at the same index in the original alphabet.

- **Decryption:**  
  Each character in the encrypted message is replaced by the character at the same index in the key.

## Usage

Run either script:

```bash
python3 Substitution.py
# or
python3 "Substitution exam.py"
```

The exam version is the easiest possible for applying in the exam.

## Notes

- The decryption logic in these scripts may not fully reverse the encryption process as written. Review and adjust as needed for your use case.
