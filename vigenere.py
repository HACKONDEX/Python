# Vigenere
import alphabet


def get_key_of_the_same_size(key, code_string):
    keys_count = int(len(code_string) / len(key)) + int(not len(code_string) % len(key) == 0)
    answer_list = list()
    for i in range(keys_count):
        answer_list.append(key)
    answer = ""
    return answer.join(answer_list)


def code_vigenere(coefficient, key, code_string):
    code_key = get_key_of_the_same_size(key, code_string)

    answer_list = list()
    index = 0
    for i in range(len(code_string)):

        if code_key[i] in alphabet.lowercase:
            index = alphabet.lowercase[code_key[i]]
        elif code_key[i] in alphabet.uppercase:
            index = alphabet.uppercase[code_key[i]]

        if code_string[i] in alphabet.lowercase:
            letter_type = alphabet.lowercase_dict
            letter_number = alphabet.lowercase[code_string[i]]
        elif code_string[i] in alphabet.uppercase:
            letter_type = alphabet.uppercase_dict
            letter_number = alphabet.uppercase[code_string[i]]
        else:
            answer_list.append(code_string[i])
            continue

        answer_list.append(letter_type[(letter_number + coefficient *
                                        index + alphabet.size) % alphabet.size])
    answer = ""
    return answer.join(answer_list)


def encode_vigenere(code_key, code_string):
    return code_vigenere(1, code_key, code_string)


def decode_vigenere(code_key, code_string):
    return code_vigenere(-1, code_key, code_string)


aaa = " My heart is beating fast!@#$%^&*()er an2342d 5fa6435ster"
ax = encode_vigenere('dog', aaa)
print(ax)
print(decode_vigenere('dog', ax))

a = True
print(int(a))
