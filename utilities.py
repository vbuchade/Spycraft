from dictionary_builder import encoder_dict

appended_vals = ""

# Get rid of keys from encoder_dictionary.
# Append all values as "one big string"
for v in encoder_dict.values():
    appended_vals += v

# Find length of all values appended together
vals_len = len(appended_vals)

# For each value-v in encoder_dictionary check that "one big string" of all values does not have more than 1 occurrence of v
# Length_of_one_big_string_of_all_values_in_dictionary == length_of_value-v + length_of_string_found_after_replace-all_of_v_from_one_big_string
repeated_substrings = []
for v in encoder_dict.values():
    removed_sub_str = appended_vals.replace(v,"")
    if(len(removed_sub_str)+len(v) == vals_len): # Value v is not present as substring in any other values used.
        continue
    else:
        repeated_substrings.append(v)

# repeated_substrings contains all the strings which are present as substrings inside other values
print(str(repeated_substrings) + " are present inside another value in your dictionary")
