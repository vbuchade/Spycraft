from dictionary_builder import encoder_dict as encoder

def encrypt(user_str):
    list1 = list(user_str)
    print(list1)
    list2 = [[]] * len(list1)
    for i in range (0, len(list1)):
        list2[i]=(encoder[list1[i]])
    return ''.join(list2)
