import string


def built_alphabet(string_, mode):
    dictionary = dict()
    key = mode - 1
    value = 2 - mode
    for i in enumerate(string_):
        dictionary[i[key]] = i[value]

    return dictionary


lowercase_dict = built_alphabet(string.ascii_lowercase, 1)
uppercase_dict = built_alphabet(string.ascii_uppercase, 1)
lowercase = built_alphabet(string.ascii_lowercase, 2)
uppercase = built_alphabet(string.ascii_uppercase, 2)
size = 26
