import cesar
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

    if cipher == 'cesar':
        if enc_dec == 'enc':
            output_string = cesar.encode_caesar(key, input_string)
        else:
            output_string = cesar.decode_caesar(key, input_string)
    else:
        if enc_dec == 'enc':
            output_string = vigenere.encode_vigenere(key, input_string)
        else:
            output_string = vigenere.decode_vigenere(key, input_string)

    create_output(output_filename, any_output_direction, output_string)


def hack_cesar(input_filename, output_filename, any_input_direction, any_output_direction, model_filename):

    input_string = return_input(input_filename, any_input_direction)
    right_key = hack.hack_cesar_from_string(input_string, model_filename)
    # print("right key is ", right_key)
    output_string = cesar.decode_caesar(right_key, input_string)
    create_output(output_filename, any_output_direction, output_string)


def make_model(input_filename, any_input_direction, model_filename):

    input_string = return_input(input_filename, any_input_direction)
    train.train(input_string, model_filename)


# Не знаю есть ли более ужасный метод но другого метода получше я не услпеваю искать((
def call_right_method(command, cipher, key, any_input_direction, any_output_direction,
                      input_filename, output_filename, model_filename):
    if command == 'encode':
        if cipher == 'caesar':
            key = int(key)
            ciphrator(input_filename, output_filename, key, any_input_direction, any_output_direction, 'cesar', 'enc')
        elif cipher == 'vigenere':
            ciphrator(input_filename, output_filename, key, any_input_direction, any_output_direction, 'vigenere', 'enc')
        else:
            print("No such command available")
    elif command == 'decode':
        if cipher == 'caesar':
            key = int(key)
            ciphrator(input_filename, output_filename, key, any_input_direction, any_output_direction, 'cesar', 'dec')
        elif cipher == 'vigenere':
            ciphrator(input_filename, output_filename, key, any_input_direction, any_output_direction, 'vigenere', 'dec')
        else:
            print("No such command available")
    elif command == 'hack':
        hack_cesar(input_filename, output_filename, any_input_direction, any_output_direction, model_filename)
    elif command == 'train':
        make_model(input_filename, any_input_direction, model_filename)
    else:
        print("No such command available")
