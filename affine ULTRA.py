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

print("Affine Cipher Encryptor/Decryptor by 0xl33t")
print("1. Encrypt")
print("2. Decrypt")
choice = input("Choose an Option: ")
if choice == "1":
   plaintext = input("Enter the plaintext: ")
   a = int(input("Enter the value of a (must be coprime to 256): "))
   b = int(input("Enter the value of b: "))
   ciphertext = encrypt(plaintext, a, b)
   print("Ciphertext:", ciphertext, end="\n")
   print("Do you want to decrypt the ciphertext? (Y/n)")
   
   if input().lower() == "n":
       exit(0)
   else:
       plaintext = decrypt(ciphertext, a, b)
       print("Plaintext:", plaintext)