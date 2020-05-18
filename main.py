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
    for i in commands_list:
        print(i)


command_functions = [print_list,
                     functions.add_city,
                     functions.city_list,
                     functions.temperature,
                     functions.change_temperature,
                     functions.moisture,
                     functions.change_moisture,
                     functions.temperature_difference,
                     functions.last_days_statistics,
                     functions.make_prediction,
                     stop_session]


def main():
    parser = create_parser()
    args = parser.parse_args()
    print("Hello, you entered Weather control system!")
    print("Type \'help\' for command list")
    while True:
        try:
            command = input("\nEnter command> ")
            flag = True
            for i in range(11):
                if command == commands_list[i]:
                    command_functions[i](args)
                    flag = False
                    break
            if flag:
                print("Unknown command, please try again!")

        except KeyboardInterrupt:
            stop_session()


if __name__ == '__main__':
    main()
