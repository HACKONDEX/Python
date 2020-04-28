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


def call_cipher(args, enc_dec):
    input_ = input_file_checker(args.input_file, "input")
    output_ = output_file_checker(args.output_file)
    base_functionals.ciphrator(input_[1], output_[1], args.key, input_[0],
                               output_[0], args.cipher, enc_dec)


def encode(args):
    call_cipher(args, 'enc')


def decode(args):
    call_cipher(args, 'dec')


def train(args):
    input_ = input_file_checker(args.text_file, "text")
    base_functionals.make_model(input_[1], input_[0], args.model_file.name)


def hack(args):
    input_ = input_file_checker(args.input_file, "input")
    output_ = output_file_checker(args.output_file)
    model_ = input_file_checker(args.model_file, "model")
    base_functionals.hack_cesar(input_[1], output_[1], input_[0], output_[0], model_[1])


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
