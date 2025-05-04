import numpy as np

# Initialize global matrices
key_matrix = np.zeros((3, 3), dtype=int)
message_vector = np.zeros((3, 1), dtype=int)
cipher_matrix = np.zeros((3, 1), dtype=int)

# Function to generate the key matrix from the key string
def get_key_matrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            key_matrix[i][j] = ord(key[k]) % 65
            k += 1

# Function to encrypt the message vector
def encrypt(message_vector):
    for i in range(3):
        cipher_matrix[i][0] = 0
        for x in range(3):
            cipher_matrix[i][0] += (key_matrix[i][x] * message_vector[x][0])
        cipher_matrix[i][0] = cipher_matrix[i][0] % 26

# Hill cipher wrapper function
def hill_cipher(message, key):
    get_key_matrix(key)
    for i in range(3):
        message_vector[i][0] = ord(message[i]) % 65
    encrypt(message_vector)
    ciphertext = [chr(cipher_matrix[i][0] + 65) for i in range(3)]
    print("The Ciphertext:", "".join(ciphertext))

# Example usage
message = "DOG"
key = "YHGINUKER"  # Must be 9 characters long for 3x3 matrix
hill_cipher(message, key)