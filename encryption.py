from dictionary_builder import dictionary_builder

def encrypt(lang, user_str):
    encoder=dictionary_builder(lang)
    list1 = list(user_str)
    list2 = [[]] * len(list1)
    for i in range (0, len(list1)):
        if list1[i] in dict.keys(encoder):
            list2[i] = encoder[list1[i]]
        elif list1[i] == " ":
            list2[i] = " "
        else:
            print("Error: Input keyword not found in Dictionary")
            return None

    return ''.join(list2)
