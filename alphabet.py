import string


def built_alphabet(string_, need_dict_reversed):
    dictionary = dict()
    for i in enumerate(string_):
        dictionary[i[int(not need_dict_reversed)]] = i[1 - int(not need_dict_reversed)]

    return dictionary


lowercase_dict = built_alphabet(string.ascii_lowercase, True)
uppercase_dict = built_alphabet(string.ascii_uppercase, True)
lowercase = built_alphabet(string.ascii_lowercase, False)
uppercase = built_alphabet(string.ascii_uppercase, False)
size = len(lowercase)
