import argparse
import base_functionals
import json


def get_input(args_input_file, file_name):
    if args_input_file:
        try:
            with open(args_input_file.name, 'r') as input_file:
                input_string = input_file.read()
            return input_string
        except FileNotFoundError:
            print(" There is no such", file_name, "file ")
            raise FileNotFoundError
    else:
        input_string = input()
    return input_string


def create_output(args_output_file, output_string):
    if args_output_file:
        with open(args_output_file.name, 'w') as output_file:
            output_file.write(output_string)
    else:
        print(output_string)


def call_cipher(args, is_encode):
    output_string = base_functionals.ciphrator(get_input(args.input_file, "input"),
                                               args.key, args.cipher, is_encode)
    create_output(args.output_file, output_string)


def encode(args):
    call_cipher(args, True)


def decode(args):
    call_cipher(args, False)


def train(args):
    base_functionals.make_model(get_input(args.text_file, "text"),
                                args.model_file.name)


def hack(args):
    try:
        with open(args.model_file.name) as model:
            right_frequency = json.load(model)
    except FileNotFoundError:
        print("There is no model file")
    create_output(args.output_file, base_functionals.hack_caesar(
        get_input(args.input_file, "input"), right_frequency
    ))


parser = argparse.ArgumentParser(description=" Command line arguments reader",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
subparsers = parser.add_subparsers()
parser_encode = subparsers.add_parser('encode', help=' encode command ')
parser_encode.set_defaults(mode='encode', function=encode)
parser_encode.add_argument('--cipher', help=" type of cipher ", required=True)
parser_encode.add_argument('--key', help=" key of cipher ", required=True)
parser_encode.add_argument('--input-file', type=argparse.FileType('r'), help=" input file ")
parser_encode.add_argument('--output-file', type=argparse.FileType('w'), help=' output file ')

parser_decode = subparsers.add_parser('decode', help=' decode command')
parser_decode.set_defaults(mode='decode', function=decode)
parser_decode.add_argument('--cipher', help=' type o cipher ', required=True)
parser_decode.add_argument('--key', help='Cipher key', required=True)
parser_decode.add_argument('--input-file', type=argparse.FileType('r'), help=' input file ')
parser_decode.add_argument('--output-file', type=argparse.FileType('w'), help=' output file ')

parser_train = subparsers.add_parser('train', help=' train command')
parser_train.set_defaults(mode='train', function=train)
parser_train.add_argument('--text-file', type=argparse.FileType('r'), help=' input file ')
parser_train.add_argument('--model-file', type=argparse.FileType('w'), help=' model(output) file', required=True)

parser_hack = subparsers.add_parser('hack', help=' hack command ')
parser_hack.set_defaults(mode='hack', function=hack)
parser_hack.add_argument('--cipher', help=' type of cipher ', required=True)
parser_hack.add_argument('--input-file', type=argparse.FileType('r'), help=' input file ')
parser_hack.add_argument('--output-file', type=argparse.FileType('w'), help=' output file ')
parser_hack.add_argument('--model-file', type=argparse.FileType('r'), help=' real model file ', required=True)

commands = parser.parse_args()
commands.function(commands)
