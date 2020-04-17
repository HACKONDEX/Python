import cesar
import vigenere


def chiphrator(input_filename, output_filename, key, any_input_direction,
               any_output_direction, chipher, enc_dec):

    if any_input_direction:
        with open(input_filename, 'r') as input_file:
            input_string = input_file.read()
    else:
        input_string = input()

    if chipher == 'cesar':
        if enc_dec == 'enc':
            output_string = cesar.encode_caesar(key, input_string)
        else:
            output_string = cesar.decode_caesar(key, input_string)
    else:
        if enc_dec == 'enc':
            output_string = vigenere.encode_vigenere(key, input_string)
        else:
            output_string = vigenere.decode_vigenere(key, input_string)

    if any_output_direction:
        with open(output_filename, 'w') as output_file:
            output_file.write(output_string)
    else:
        print(output_string)


chiphrator("aka_vig_enc.txt", "aka_decode_new.txt", "dog", True, True, "vig", "dec")
