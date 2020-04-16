# Cesar
import alphabet


def code_caesar(key, code_string):
    coded_answer = ""
    letter_type = dict()
    for i in code_string:
        if i in alphabet.alphabet[0]:
            letter_type = alphabet.alphabet[0]
        elif i in alphabet.alphabet[1]:
            letter_type = alphabet.alphabet[1]
        else:
            coded_answer += i
            continue
        coded_answer += letter_type[(letter_type[i] + key % letter_type['size']
                                     + letter_type['size']) % letter_type['size']]

    return coded_answer


def encode_caesar(key, code_string):
    return code_caesar(key, code_string)


def decode_caesar(key, code_string):
    return code_caesar(-key, code_string)
