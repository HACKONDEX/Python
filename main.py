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
    parser.add_argument('--port', default=8000, type= int)
    return parser


def stop_session():
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


def print_list(list_):
    for i in list_:
        print(i)


def main():
    parser = create_parser()
    args = parser.parse_args()
    print("Hello, you entered Weather control system!")
    print("Type \'help\' for command list")
    while True:
        try:
            command = input("\nEnter command> ")
            if command == commands_list[0]:
                # help
                print_list(commands_list)
            elif command == commands_list[1]:
                functions.add_city(args)
            elif command == commands_list[2]:
                functions.city_list(args)
            elif command == commands_list[3]:
                functions.temperature(args)
            elif command == commands_list[4]:
                functions.change_temperature(args)
            elif command == commands_list[5]:
                functions.moisture(args)
            elif command == commands_list[6]:
                functions.change_moisture(args)
            elif command == commands_list[7]:
                functions.temperature_difference(args)
            elif command == commands_list[8]:
                functions.last_days_statistics(args)
            elif command == commands_list[9]:
                functions.make_prediction(args)
            elif command == commands_list[10]:
                stop_session()
            else:
                print("Unknown command, please try again!")
        except KeyboardInterrupt:
            stop_session()


if __name__ == '__main__':
    main()
