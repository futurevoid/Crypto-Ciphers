import numpy as np

dim = int(input("Enter the length of the message: "))

# Initialize global matrices
key_matrix = np.zeros((dim, dim), dtype=int)
message_vector = np.zeros((dim, 1), dtype=int)
cipher_matrix = np.zeros((dim, 1), dtype=int)

# Function to generate the key matrix from the key string
def gen_key(key):
    k = 0
    for row in range(dim):
        for col in range(dim):
            key_matrix[row][col] = ord(key[k]) % 256
            k += 1

def encrypt(message):
    ciphertext = ""
    for idx in range(dim):
        message_vector[idx][0] = ord(message[idx]) % 256
    cipher_matrix = np.dot(key_matrix, message_vector) % 256
    for idx in range(dim):
        ciphertext += chr(int(cipher_matrix[idx][0]))
    return ciphertext

msg = input("Enter the message: ")
key = input(f"Enter the key of length {dim**2}: ")
gen_key(key)
ciphertext = encrypt(msg)
print("Encrypted: ", ciphertext)
print("Encrypted(UTF-8 Encoded): ", ciphertext.encode('utf-8'))