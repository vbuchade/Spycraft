from dictionary_builder import dictionary_builder
import os
import sys

def validate_dictionary_substring_rules(lang):

    # Get rid of keys from encoder_dictionary.
    # Append all values as "one big string"
    dictionary = dictionary_builder(lang)
    appended_vals = getValueAsString(dictionary)

    # Find length of all values appended together
    vals_len = len(appended_vals)

    # For each value-v in encoder_dictionary check that "one big string" of all values does not have more than 1 occurrence of v
    # Length_of_one_big_string_of_all_values_in_dictionary == length_of_value-v + length_of_string_found_after_replace-all_of_v_from_one_big_string
    repeated_substrings = []
    for v in dictionary.values():
        removed_sub_str = appended_vals.replace(v,"")
        if(len(removed_sub_str)+len(v) == vals_len): # Value v is not present as substring in any other values used.
            continue
        else:
            repeated_substrings.append(v)

    # repeated_substrings contains all the strings which are present as substrings inside other values
    print(str(repeated_substrings) + " are present inside another value in your dictionary")

def getValueAsString(d):
    appended_vals = ""
    #d is a dict
    for v in d.values():
        appended_vals += v
    return appended_vals

# Find language based on encoded string provided by the user
def findLanguage(encoded_str):
    foundFlag = False

    # Get all languages from .txt files from current directory
    languages = [str(f).replace("_dictionary.txt","") for f in os.listdir() if f.endswith(".txt")]

    # For each file do ->
    for lang in languages:
        # get all the values used for encoding
        values = dictionary_builder(lang).values()

        # use a window whose size increases from 1 to length-of-encoded-string
        # at each window-size check if the word exists in dictionary's values
        windowSize = 1
        while(windowSize <= len(encoded_str)):
            word = encoded_str[0:windowSize]
            if word in values:
                foundFlag = True
                break;
            windowSize += 1
        if foundFlag:
            print("Language = " + lang)
            return lang

    return None

if __name__ == "__main__":
    validate_dictionary_substring_rules(sys.argv[1])

