# Vigenere
import alphabet


def get_key_of_the_same_size(key, code_string):
    code_key = key
    while len(key) + len(code_key) <= len(code_string):
        code_key += key
    for i in key:
        if len(code_key) < len(code_string):
            code_key += i
        else:
            break
    return code_key


def code_vigenere(coefficient, key, code_string):
    code_key = get_key_of_the_same_size(key, code_string)

    coded_answer = ""
    for i in range(len(code_string)):

        if code_key[i] in alphabet.alphabet[0]:
            index = alphabet.alphabet[0][code_key[i]]
        elif code_key[i] in alphabet.alphabet[1]:
            index = alphabet.alphabet[1][code_key[i]]

        if code_string[i] in alphabet.alphabet[0]:
            letter_type = alphabet.alphabet[0]
        elif code_string[i] in alphabet.alphabet[1]:
            letter_type = alphabet.alphabet[1]
        else:
            coded_answer += code_string[i]
            continue

        coded_answer += letter_type[(letter_type[code_string[i]] + coefficient *
                                    index + letter_type['size']) % letter_type['size']]

    return coded_answer


def encode_vigenere(code_key, code_string):
    return code_vigenere(1, code_key, code_string)


def decode_vigenere(code_key, code_string):
    return code_vigenere(-1, code_key, code_string)
