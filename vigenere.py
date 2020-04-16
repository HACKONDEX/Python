# Vigenere
import alphabet


def code_vigenere(coefficient, code_key, code_string):
    coded_answer = ""
    for i in range(len(code_string)):
        for letter_type in alphabet:
            if code_string[i] in letter_type:
                coded_answer += letter_type[(letter_type[code_string[i]] + coefficient *
                                             letter_type[code_key[i]] + letter_type['size']) % letter_type['size']]
                break
    return coded_answer


def encode_vigenere(code_key, code_string):
    return code_vigenere(1, code_key, code_string)


def decode_vigenere(code_key, code_string):
    return code_vigenere(-1, code_key, code_string)
