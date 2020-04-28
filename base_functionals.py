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


def ciphrator(input_filename, output_filename, key, any_input_direction, any_output_direction, cipher, enc_dec):

    input_string = return_input(input_filename, any_input_direction)

    if cipher == 'caesar':
        key = int(key)
        if enc_dec == 'enc':
            output_string = caesar.encode_caesar(key, input_string)
        else:
            output_string = caesar.decode_caesar(key, input_string)
    else:
        if enc_dec == 'enc':
            output_string = vigenere.encode_vigenere(key, input_string)
        else:
            output_string = vigenere.decode_vigenere(key, input_string)

    create_output(output_filename, any_output_direction, output_string)


def hack_cesar(input_filename, output_filename, any_input_direction, any_output_direction, model_filename):

    input_string = return_input(input_filename, any_input_direction)
    right_key = hack.hack_cesar_from_string(input_string, model_filename)
    output_string = caesar.decode_caesar(right_key, input_string)
    create_output(output_filename, any_output_direction, output_string)


def make_model(input_filename, any_input_direction, model_filename):

    input_string = return_input(input_filename, any_input_direction)
    train.train(input_string, model_filename)
