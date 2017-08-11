from encryption import encrypt
from decryption import decrypt

#input
msg = "B AC" # sample english input : "B CFC D ##4 ~ CE"
#input("Original message to encrypt")
print("Original message = " + msg)

#encode
encoded_msg = encrypt(msg)
print("Encoded message = " + encoded_msg)

#decode
print("Decoded message = " + decrypt(encoded_msg))