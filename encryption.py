from dictionary_builder import encoder_dict as encoder

user_str=input("please enter a string:")
list1=list(user_str)
list2=[[]]*len(list1)

def encrypt(str):
    for i in range (0, len(list1)):
        list2[i]=(encoder[list1[i]])
encrypt(str=user_str)
print(''.join(list2))
