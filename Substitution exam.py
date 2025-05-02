import string
import random

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + " "
print(alphabet)

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
        
msg = "0xlol is a L33T H4X0R"

key = gen_key()

encrypt(key,msg)

print()

decrypt(key,msg)