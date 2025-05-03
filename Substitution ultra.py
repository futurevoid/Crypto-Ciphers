import string
import random

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + " "

def gen_key(alphabet=alphabet):
    key = list(alphabet)
    random.shuffle(key)
    return key

def encrypt(key,msg):
    for char in msg:
        idx = key.index(char)
        print(alphabet[idx],end="")

def decrypt(key,msg):
    for char in msg:
        idx = key.index(char)
        print(key[idx],end="")
        
msg = input("Enter the message: ")

key = gen_key()

print("Encrypted: ", end="")
encrypt(key,msg)

print()

print("Decrypted: ", end="")
decrypt(key,msg)