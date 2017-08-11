import sys
from dictionary_builder import encoder_dict as encoder


def encrypt(msg):
    # Varsha's implementation. But will be replaced by Xiao/Ling's implementation
    encoded_msg = [encoder[char] if (char in encoder) else char for char in msg]
    return "".join(encoded_msg)
    # TODO:
    # if any of the alphabets / letters in input plain-text message do NOT match with dictionary keys used for encoding
    # -> Throw error
    # -> Dynamically generate dictionary key-value for new keys.
    #    Then write it in the <language>_dictionary file to be used in future for decryption

if __name__ == "__main__":
    encrypt(str(sys.argv[1]))

