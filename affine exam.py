def encrypt(plaintext, a, b):
   ciphertext = ""
   for char in plaintext:
      cipherchar = chr((a * ord(char) + b) % 256)
      ciphertext += cipherchar
   return ciphertext

def decrypt(ciphertext, a, b):
   plaintext = ""
   a_inv = pow(a, -1, 256)
   for char in ciphertext:
      plainchar = chr((a_inv * (ord(char) - b) ) % 256)
      plaintext += plainchar
   return plaintext

# plain text message and keys
plain_text = "Hello, World!"
a = 5
b = 8

encrypted_text = encrypt(plain_text, a, b)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, a, b)
print("Decrypted text:", decrypted_text)