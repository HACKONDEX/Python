import requests

temperature_message = "Temperature should be a number, try again!"
moisture_message = "Moisture should be a number, try again!"
city_name_message = "Enter city name> "


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
        name=input(city_name_message),
        temp=input_for_int("Enter temperature> ", temperature_message),
        moist=input_for_int("Enter moisture> ", moisture_message)
    )).text
    print(verdict)


def city_list(args):
    city_list_ = requests.get(f'http://{args.host}:{args.port}/get_city_list').text
    city_list_ = str(city_list_)
    city_list_ = city_list_.split(" ")
    for i in city_list_:
        print(i)


def temperature(args):
    verdict = requests.get(f'http://{args.host}:{args.port}/temperature',
                           data=dict(name=input(city_name_message))).text
    print(verdict)


def change_temperature(args):
    verdict = requests.post(f'http://{args.host}:{args.port}/change_temperature', data=dict(
        name=input(city_name_message),
        temp=input_for_int("Enter new temperature> ", temperature_message)
    )).text
    print(verdict)


def moisture(args):
    verdict = requests.get(f'http://{args.host}:{args.port}/moisture',
                           data=dict(name=input(city_name_message))).text
    print(verdict)


def change_moisture(args):
    verdict = requests.post(f'http://{args.host}:{args.port}/change_moisture', data=dict(
        name=input(city_name_message),
        moist=input_for_int("Enter new moisture> ", moisture_message))).text
    print(verdict)


def temperature_difference(args):
    verdict = requests.get(f'http://{args.host}:{args.port}/temperature_difference', data=dict(
        first=input("Enter first city name> "),
        second=input("Enter second city name> "))).text
    print(verdict)


def last_days_statistics(args):
    verdict = requests.get(f'http://{args.host}:{args.port}/statistics',
                           data=dict(name=input(city_name_message))).text
    print(verdict)


def make_prediction(args):
    verdict = requests.get(f'http://{args.host}:{args.port}/make_prediction',
                           data=dict(name=input(city_name_message))).text
    print(verdict)

