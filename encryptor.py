import argparse
import base_functionals


def input_file_checker(args_input_file, file_name):
    if args_input_file:
        try:
            with open(args_input_file.name, 'r') as f:
                a = f.read()
            return_ = (True, args_input_file.name)
        except FileNotFoundError:
            print(" There is no such", file_name, "file ")
            raise FileNotFoundError
    else:
        return_ = (False, "no_file")
    return return_


def output_file_checker(args_output_file):
    if args_output_file:
        return_ = (True, args_output_file.name)
    else:
        return_ = (False, "no_file")
    return return_


def call_cipher(args, is_encode):
    input_information = input_file_checker(args.input_file, "input")
    input_string = base_functionals.return_input(input_information[1], input_information[0])
    output_string = base_functionals.ciphrator(input_string, args.key, args.cipher, is_encode)
    output_information = output_file_checker(args.output_file)
    base_functionals.create_output(output_information[1], output_information[0], output_string)


def encode(args):
    call_cipher(args, True)


def decode(args):
    call_cipher(args, False)


def train(args):
    input_information = input_file_checker(args.text_file, "text")
    input_string = base_functionals.return_input(input_information[1], input_information[0])
    base_functionals.make_model(input_string, args.model_file.name)


def hack(args):
    input_information = input_file_checker(args.input_file, "input")
    input_string = base_functionals.return_input(input_information[1], input_information[0])
    model_information = input_file_checker(args.model_file, "model")
    output_string = base_functionals.hack_cesar(input_string, model_information[1])
    output_information = output_file_checker(args.output_file)
    base_functionals.create_output(output_information[1], output_information[0], output_string)


parser = argparse.ArgumentParser(description=" Command line arguments reader",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
subparsers = parser.add_subparsers()
parser_encode = subparsers.add_parser('encode', help=' encode command ')
parser_encode.set_defaults(mode='encode', function=encode)
parser_encode.add_argument('--cipher', choices=['caesar', 'vigenere'], help=" type of cipher ", required=True)
parser_encode.add_argument('--key', help=" key of cipher ", required=True)
parser_encode.add_argument('--input-file', type=argparse.FileType('r'), help=" input file ")
parser_encode.add_argument('--output-file', type=argparse.FileType('w'), help=' output file ')

parser_decode = subparsers.add_parser('decode', help=' decode command')
parser_decode.set_defaults(mode='decode', function=decode)
parser_decode.add_argument('--cipher', choices=['caesar', 'vigenere'], help=' type o cipher ', required=True)
parser_decode.add_argument('--key', help='Cipher key', required=True)
parser_decode.add_argument('--input-file', type=argparse.FileType('r'), help=' input file ')
parser_decode.add_argument('--output-file', type=argparse.FileType('w'), help=' output file ')

parser_train = subparsers.add_parser('train', help=' train command')
parser_train.set_defaults(mode='train', function=train)
parser_train.add_argument('--text-file', type=argparse.FileType('r'), help=' input file ')
parser_train.add_argument('--model-file', type=argparse.FileType('w'), help=' model(output) file', required=True)

parser_hack = subparsers.add_parser('hack', help=' hack command ')
parser_hack.set_defaults(mode='hack', function=hack)
parser_hack.add_argument('--cipher', choices=['caesar'], help=' type of cipher ', required=True)
parser_hack.add_argument('--input-file', type=argparse.FileType('r'), help=' input file ')
parser_hack.add_argument('--output-file', type=argparse.FileType('w'), help=' output file ')
parser_hack.add_argument('--model-file', type=argparse.FileType('r'), help=' real model file ', required=True)

commands = parser.parse_args()
commands.function(commands)
