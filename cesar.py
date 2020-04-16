# Cesar
import alphabet


def code_caesar(key, code_string):
    coded_answer = ""
    for i in code_string:
        for letter_type in alphabet.alphabet:
            if i in letter_type:
                coded_answer += letter_type[(letter_type[i] + key % letter_type['size']
                              + letter_type['size']) % letter_type['size']]
                break
    return coded_answer


def encode_caesar(key, code_string):
    return code_caesar(key, code_string)


def decode_caesar(key, code_string):
    return code_caesar(-key, code_string)
