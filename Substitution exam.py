import string
import random

alphabet = string.ascii_uppercase + string.ascii_lowercase + " "

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
        
msg = "Hacko is a real hacker"

key = gen_key()

encrypt(key,msg)

print()

decrypt(key,msg)