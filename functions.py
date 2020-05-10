import requests


def input_for_int(input_message, error_message):
    while True:
        try:
            return_ = int(input(input_message))
            break
        except ValueError:
            print(error_message)
    return return_


def add_city(args):
    verdict = requests.post(f'http://{args.host}:{args.port}/add_city', data=dict(
        name=input("Enter city name> "),
        temp=input_for_int("Enter temperature> ", "Temperature should be a number, try again!"),
        moist=input_for_int("Enter moisture> ", "Moisture should be a number, try again!")
    )).text
    print(verdict)


def city_list(args):
    city_list_ = requests.get(f'http://{args.host}:{args.port}/get_city_list').text
    city_list_ = str(city_list_)
    city_list_ = city_list_.split(" ")
    for i in city_list_:
        print(i)


def temperature(args):
    pass


def change_temperature(args):
    pass


def moisture(args):
    pass


def change_moisture(args):
    pass


def temperature_difference(args):
    pass


def last_days_statistics(args):
    pass


def make_prediction(args):
    pass
