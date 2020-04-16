import string


def built_alphabet(string_):
    dictionary = dict()

    for i in range(len(string_)):
        dictionary[string_[i]] = i
        dictionary[i] = string_[i]

    dictionary['size'] = len(string_)

    return dictionary


lowercase = built_alphabet(string.ascii_lowercase)
uppercase = built_alphabet(string.ascii_uppercase)

alphabet = [lowercase, uppercase]