import random
import string

chars = string.digits + string.punctuation + string.ascii_letters
chars = list(chars) # converting the string into a list of chars
key =chars.copy()

random.shuffle(key) # shuffling the list

# print(f"chars :{chars}")
# print(f"key : {key}")

#ENCRYPT
plain_text= input("Enter a message to encrypt: ")
cipher_text=""

for letter in plain_text:
    index = plain_text.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"original message: {cipher_text}")

# #DENCRYPT
# plain_text=""
#
# for letter in cipher_text:
#     index = cipher_text.index(letter)
#     plain_text += key[index]