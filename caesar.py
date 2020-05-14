# Caesar
import alphabet


def code_caesar(key, code_string):
    key = int(key)
    answer_list = list()
    for i in code_string:
        alphabet.code_one_symbol(i, key, answer_list)
    return "".join(answer_list)


def encode_caesar(key, code_string):
    return code_caesar(key, code_string)


def decode_caesar(key, code_string):
    return code_caesar(-key, code_string)
