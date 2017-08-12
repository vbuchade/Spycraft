lang = "english"
# lang = "japanese"
dict_name = lang + "_dictionary"
file = open(dict_name, "r", -1, "UTF-8")
lines = file.readlines()
cleanedLines = []

cleanedLines = [l.replace("\n","") for l in lines]
# ^^ this is same as below
# for line in lines:
#     cleanedLines.append(line.replace("\n", ""))
# print(cleanedLines)

# create dict from cleanedLines
encoder_dict = dict()
for entry in cleanedLines:
    kv = entry.split("=")
    encoder_dict[kv[0]] = kv[1]
# print(encoder_dict)
