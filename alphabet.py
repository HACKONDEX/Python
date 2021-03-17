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


def code_one_symbol(symbol, shift, coded_list):
    if symbol in uppercase:
        letter_type = uppercase_dict
        letter_number = uppercase[symbol]
    elif symbol in lowercase:
        letter_type = lowercase_dict
        letter_number = lowercase[symbol]
    else:
        coded_list.append(symbol)
        return
    coded_list.append(letter_type[((letter_number + shift) % size + size) % size])
