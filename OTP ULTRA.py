import random
import string
def gen_key(msg):
    key = string.printable + ""
    random.shuffle(list(key))
    if len(key) < len(msg):
        msg_len = int(len(msg)/len(key)+1)
        key = (key * msg_len)
        return key  
    else:
        return key
    
def encrypt(msg, key):
    ciphertext = ""
    for char in range(len(msg)):
        cipherchar = chr((ord(msg[char]) ^ ord(key[char])))
        ciphertext += cipherchar
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in range(len(ciphertext)):
        plainchar = chr((ord(ciphertext[char]) ^ ord(key[char])))
        plaintext += plainchar
    return plaintext



if __name__ == "__main__":
    print("One Time Pad Encryptor/Decryptor by 0xl33t")
    
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an Option: ")
    if choice == "1":
        plaintext = input("Enter the plaintext: ")
        key = gen_key(plaintext)
        ciphertext = encrypt(plaintext, key)
        print("Ciphertext:", ciphertext, end="\n")
        print("Do you want to decrypt the ciphertext? (Y/n)")
        
        if input().lower() == "n":
            exit(0)
        else:
            plaintext = decrypt(ciphertext, key)
            print("Plaintext:", plaintext)
            
    elif choice == "2":
        ciphertext = input("Enter the ciphertext: ")
        key = gen_key(ciphertext)
        plaintext = decrypt(ciphertext, key)
        print("Plaintext:", plaintext)
        
    else:
        print("Invalid choice")
        exit(1)