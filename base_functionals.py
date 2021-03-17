import caesar
import vigenere
import hack
import train


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


def hack_caesar(input_string, right_frequency):
    return caesar.decode_caesar(hack.hack_caesar_from_string(input_string, right_frequency), input_string)


def make_model(input_string, model_filename):
    train.train(input_string, model_filename)
