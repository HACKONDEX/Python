import argparse
import functions
import constants as cs

default_port = 8000
default_host = 'localhost'


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default=default_host)
    parser.add_argument('--port', default=default_port, type=int)
    return parser


def main():
    functions.set_address(create_parser().parse_args())
    print(cs.hello_print)
    print(cs.help_print)
    while True:
        try:
            command = input(cs.command_print)
            if command in cs.commands_list:
                functions.command_functions_dict[command]()
            else:
                print(cs.unknown_command_message)
        except KeyboardInterrupt:
            functions.stop_session()


if __name__ == '__main__':
    main()

