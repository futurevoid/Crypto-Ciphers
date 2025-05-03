import string

def encrypt(alphabet, shift ,msg):
    shift = shift % len(alphabet)
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    encrypted_msg = msg.translate(table)
    print(f"Encrypted: {encrypted_msg}")
    return encrypted_msg
    

def decrypt(alphabet, shift, msg):
    shift = shift % len(alphabet)
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(shifted, alphabet)
    decrypted_msg = msg.translate(table)
    print(f"Decrypted: {decrypted_msg}")
    return decrypted_msg

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + " "
        
msg = input("Enter the message: ")

shift = int(input("Enter the shift value: "))

encrypted = encrypt(alphabet,shift,msg)

print()

decrypted = decrypt(alphabet,shift,encrypted)