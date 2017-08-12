from encryption import encrypt
from decryption import decrypt

#input
user_str=input("Please enter a string:")

#encode
encoded_msg = encrypt(user_str)
print("Encoded message = " + encoded_msg)

#decode
print("Decoded message = " + decrypt(encoded_msg))