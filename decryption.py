from dictionary_builder import dictionary_builder
from utilities import findLanguage
import sys


# check if any k(key) from decoder matches to anything in encoded_msg
# what-ever matches replace by v(value)
def decrypt(msg):
    if msg == "" or msg is None:
        print("Empty / Null encoded input. Nothing to do here.")
        return ""

    lang = findLanguage(msg)

    if lang == None:
        print("Did not find a valid language to decrypt with.")
        return None

    dictionary = dictionary_builder(lang)
    decoder = dict((v, k) for k, v in dictionary.items())

    decoded_msg = msg

    for k, v in decoder.items():
        # print(" k = " + k + " v = " + v)
        decoded_msg = decoded_msg.replace(k, v)

    # print(decoded_msg)
    return decoded_msg

if __name__ == "__main__":
    decrypt(str(sys.argv[1]))
