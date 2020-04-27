import argparse
import base_functionals

commands = argparse.ArgumentParser()
commands.add_argument('command', help='encode|decode|hack|train')
commands.add_argument('--cipher', help='caesar|vigenere')
commands.add_argument('--key', help='key == number|word')
commands.add_argument('--input-file', help='file with text to encode')
commands.add_argument('--output-file', help='the output file')
commands.add_argument('--text-file', help='file to make model from')
commands.add_argument('--model-file', help='file to make model there')
args = commands.parse_args()

try:
    with open(args.input_file, 'r') as f:
        a = f.read()
    any_input_direction = True
    input_filename = args.input_file
except:
    any_input_direction = False
    input_filename = "file.nothing"

any_output_direction = False
output_filename = "file.nothing"
try:

    if not type(args.output_file) == type(None):
        any_output_direction = True
        output_filename = args.output_file
    else:
        any_output_direction = False
        output_filename = "file.nothing"
except:
    any_output_direction = False
    output_filename = "file.nothing"

if args.command == 'train':
    try:
        with open(args.text_file, 'r') as f:
            a = f.read()
        any_input_direction = True
        input_filename = args.text_file
    except:
        any_input_direction = False
        input_filename = "file.nothing"

base_functionals.call_right_method(args.command, args.cipher, args.key, any_input_direction,
                                   any_output_direction, input_filename, output_filename, args.model_file)
