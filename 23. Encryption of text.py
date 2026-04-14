import random
import string
from operator import index

char = " " + string.ascii_letters + string.punctuation + string.digits
char = list(char)
key = char.copy()
random.shuffle(key)
print(char)
print(key)

#Encryption
user_input = input("Enter the a message to encrypt: ")
encrypted_text = ''
for ch in user_input:
    index = char.index(ch)
    encrypted_text += key[index]
print(f"Encryption: {encrypted_text}")

#Decryption

user_input = input("Enter the a message to Decrypt: ")
decrypted_text = ''
for ch in user_input:
    index = key.index(ch)
    decrypted_text += char[index]
print(f"Decryption: {decrypted_text}")


