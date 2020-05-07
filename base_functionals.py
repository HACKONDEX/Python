import caesar
import vigenere
import hack
import train


def return_input(input_filename, any_input_direction):
    if any_input_direction:
        with open(input_filename, 'r') as input_file:
            input_string = input_file.read()
    else:
        input_string = input()
    return input_string


def create_output(output_filename, any_output_direction, output_string):
    if any_output_direction:
        with open(output_filename, 'w') as output_file:
            output_file.write(output_string)
    else:
        print(output_string)


def ciphrator(input_string, key, cipher, is_encode):
    if cipher == 'caesar':
        key = int(key)
        if is_encode:
            return caesar.encode_caesar(key, input_string)
        return caesar.decode_caesar(key, input_string)
    elif cipher == 'vigenere':
        if is_encode:
            return vigenere.encode_vigenere(key, input_string)
        return vigenere.decode_vigenere(key, input_string)


def hack_caesar(input_string, model_filename):

    right_key = hack.hack_cesar_from_string(input_string, model_filename)
    return caesar.decode_caesar(right_key, input_string)


def make_model(input_string, model_filename):

    train.train(input_string, model_filename)
