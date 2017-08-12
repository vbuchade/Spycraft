def dictionary_builder(lang):
    dict_name = lang + "_dictionary.txt"
    file = open(dict_name, "r", -1, "UTF-8")
    lines = file.readlines()
    cleanedLines = [l.replace("\n", "") for l in lines]
    encoder_dict = dict()
    for entry in cleanedLines:
        kv = entry.split("=")
        encoder_dict[kv[0]] = kv[1]

    return encoder_dict
