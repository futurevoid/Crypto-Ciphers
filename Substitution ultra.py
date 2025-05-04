import string
import random

alphabet = string.ascii_letters + string.digits + string.punctuation + " "

def gen_key(alphabet=alphabet):
    key = list(alphabet)
    random.shuffle(key)
    return key

def encrypt(key, msg):
    encrypted_msg = ""
    for char in msg:
        idx = alphabet.index(char)
        encrypted_msg += key[idx]
    return encrypted_msg

def decrypt(key, msg):
    decrypted_msg = ""
    for char in msg:
        idx = key.index(char)
        decrypted_msg += alphabet[idx]
    return decrypted_msg

key = gen_key()

print("Substitution Cipher Encryptor/Decryptor by 0xl33t",end="\n\n")

msg = input(f"Enter the Message to be Encrypted:")

encrypted_message = encrypt(key, msg)

print(f"Encrypted: {encrypted_message}")

decrypted_message = decrypt(key, encrypted_message)

print(f"Decrypted: {decrypted_message}")

