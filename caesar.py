# Caesar
import alphabet


def code_caesar(key, code_string):
    answer_list = list()
    letter_type = dict()
    letter_number = 0
    for i in code_string:
        if i in alphabet.uppercase:
            letter_type = alphabet.uppercase_dict
            letter_number = alphabet.uppercase[i]
        elif i in alphabet.lowercase:
            letter_type = alphabet.lowercase_dict
            letter_number = alphabet.lowercase[i]
        else:
            answer_list.append(i)
            continue
        answer_list.append(letter_type[(letter_number + key % alphabet.size
                                        + alphabet.size) % alphabet.size])
        answer = ""

    return answer.join(answer_list)


def encode_caesar(key, code_string):
    return code_caesar(key, code_string)


def decode_caesar(key, code_string):
    return code_caesar(-key, code_string)
