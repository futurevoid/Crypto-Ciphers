def gen_key(msg):
    key = input("Enter the key: ")
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



msg = input("Enter the message: ")
key = gen_key(msg)
ciphertext = encrypt(msg, key)
print("Encrypted: " ,ciphertext)
print("Encrypted(UTF-8 Encoded): ", ciphertext.encode('utf-8'))
plaintext = decrypt(ciphertext, key)
print("Decrypted: ", plaintext)