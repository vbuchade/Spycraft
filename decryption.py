from dictionary_builder import encoder_dict as encoder
import sys

decoder = dict((v, k) for k, v in encoder.items())


# check if any k(key) from decoder matches to anything in encoded_msg
# what-ever matches replace by v(value)
def decrypt(encoded_msg):
    if encoded_msg == "" or encoded_msg is None:
        print("Empty / Null encoded input. Nothing to do here.")
        return ""

    decoded_msg = encoded_msg

    for k, v in decoder.items():
        # print(" k = " + k + " v = " + v)
        decoded_msg = decoded_msg.replace(k, v)

    # print(decoded_msg)
    return decoded_msg

if __name__ == "__main__":
    decrypt(str(sys.argv[1]))
