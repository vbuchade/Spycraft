from encryption import encrypt
from decryption import decrypt

#input
user_str=input("Please enter a string:")
code_choice=input("Do you want to Encode or Decode?")
while code_choice not in ("encode", "Encode", "Encrypt", "encrypt", "decode", "Decode", "Decrypt", "decrypt"):
    print("Please tell me if you want to Encode or Decode")
    code_choice = input("Do you want to Encode or Decode?")

if code_choice in ("encode", "Encode", "Encrypt", "encrypt"):
    language_choice=input("Choose which language to encode to: English or Mandarin?")

    while language_choice not in ("English", "english", "Mandarin", "mandarin"):
        print("Please enter a supported language")
        language_choice=input("Choose which language to encode to: English or Mandarin?")

#encode
if code_choice in ("encode", "Encode", "Encrypt", "encrypt"):
    encoded_msg = encrypt(language_choice,user_str)
    if encoded_msg != None:
        print("Encoded message = " + encoded_msg)
    else:
        print("Could not encrypt those values")

#decode
if code_choice in ("Decode", "decode", "Decrypt", "decrypt"):
    decoded_msg = decrypt(user_str)
    if decoded_msg != None:
        print("Decoded message = " + decoded_msg)
    else:
        print("Could not decode those values")
