# Vigenere
import alphabet


def code_vigenere(coefficient, key, code_string):
    key_size = len(key)
    answer_list = list()
    index = 0
    for i in range(len(code_string)):
        if key[i % key_size] in alphabet.lowercase:
            index = alphabet.lowercase[key[i % key_size]]
        elif key[i % key_size] in alphabet.uppercase:
            index = alphabet.uppercase[key[i % key_size]]

        alphabet.code_one_symbol(code_string[i], coefficient * index, answer_list)
    answer = ""
    return answer.join(answer_list)


def encode_vigenere(code_key, code_string):
    return code_vigenere(1, code_key, code_string)


def decode_vigenere(code_key, code_string):
    return code_vigenere(-1, code_key, code_string)
