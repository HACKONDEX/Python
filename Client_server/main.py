import argparse
import functions
import requests

commands_list = ["help",
                 "add city",
                 "city list",
                 "temperature",
                 "change temperature",
                 "moisture",
                 "change moisture",
                 "temp diff",
                 "last days statistics",
                 "make prediction",
                 "exit"]


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=8000, type=int)
    return parser


def stop_session(*args):
    while True:
        input_ = input('Are you really sure you want to end the session (Y/N)?\n')
        if input_ == 'Y' or input_ == 'y':
            print('See you next time!')
            exit()
            break
        elif input_ == 'N' or input_ == 'n':
            print("It is a better idea")
            break
        else:
            print("Unexpected answer, please try again!")


def print_list(*args):
    for command_name in commands_list:
        print(command_name)


command_functions_dict = {"help": print_list,
                          "add city": functions.add_city,
                          "city list": functions.city_list,
                          "temperature": functions.temperature,
                          "change temperature": functions.change_temperature,
                          "moisture": functions.moisture,
                          "change moisture": functions.change_moisture,
                          "temp diff": functions.temperature_difference,
                          "last days statistics": functions.last_days_statistics,
                          "make prediction": functions.make_prediction,
                          "exit": stop_session}


def main():
    parser = create_parser()
    args = parser.parse_args()
    print("Hello, you entered Weather control system!")
    print("Type \'help\' for command list")
    while True:
        try:
            command = input("\nEnter command> ")
            if command in commands_list:
                command_functions_dict[command](args)
            else:
                print("Unknown command, please try again!")
        except KeyboardInterrupt:
            stop_session()


if __name__ == '__main__':
    main()

