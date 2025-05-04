def gen_key(plaintext):
    key = input("Enter the key: ")
    if len(key) < len(plaintext):
        msg_len = int(len(plaintext)/len(key)+1)
        key = key * msg_len
        return key
    else:
        return key
    
def encrypt(key, plaintext):
    ciphertext = ""
    for idx in range(len(plaintext)):
        cipherchar = chr((ord(plaintext[idx]) + ord(key[idx])) % 256 )
        ciphertext += cipherchar
    return ciphertext

def decrypt(key, ciphertext):
    plaintext = ""
    for idx in range(len(ciphertext)):
        plainchar = chr((ord(ciphertext[idx]) - ord(key[idx]))% 256)
        plaintext += plainchar
    return plaintext


if __name__ == "__main__":
    print("Vigenere Cipher Encryptor/Decryptor by 0xl33t")
    
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an Option: ")
    if choice == "1":
        plaintext = input("Enter the plaintext: ")
        key = gen_key(plaintext)
        ciphertext = encrypt(key, plaintext)
        print("Ciphertext:", ciphertext, end="\n")
        print("Do you want to decrypt the ciphertext? (Y/n)")
        
        if input().lower() == "n":
            exit(0)
        else:
            plaintext = decrypt(key, ciphertext)
            print("Plaintext:", plaintext)
            
    elif choice == "2":
        ciphertext = input("Enter the ciphertext: ")
        key = gen_key(ciphertext)
        plaintext = decrypt(key, ciphertext)
        print("Plaintext:", plaintext)
        
    else:
        print("Invalid choice")
        exit(1)
        