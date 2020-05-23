import requests
import constants as cs


address = ""


def set_address(args):
    global address
    address = f'http://{args.host}:{args.port}'


def stop_session():
    while True:
        input_ = input(cs.stop_session_print["sure"])
        if input_ in cs.input_y:
            print(cs.stop_session_print["next time"])
            exit()
            break
        elif input_ in cs.input_n:
            print(cs.stop_session_print["good"])
            break
        else:
            print(cs.stop_session_print["answer"])


def print_list():
    print(*cs.commands_list, sep='\n')


def input_for_int(input_message, error_message):
    while True:
        try:
            return_ = int(input(input_message))
            break
        except ValueError:
            print(error_message)
    return return_


def add_city():
    verdict = requests.post(address + cs.add_city, data=dict(
        name=input(cs.city_name_message),
        temp=input_for_int(cs.enter_temp_print, cs.temperature_message),
        moist=input_for_int(cs.enter_moisture_print, cs.moisture_message)
    )).text
    print(verdict)


def city_list():
    for city_name in requests.get(address + cs.get_city_list).text.split(" "):
        print(city_name)


def temperature():
    verdict = requests.get(address + cs.temperature,
                           data=dict(name=input(cs.city_name_message))).text
    print(verdict)


def change_temperature():
    verdict = requests.post(address + cs.change_temperature, data=dict(
        name=input(cs.city_name_message),
        temp=input_for_int(cs.enter_new_temp_print, cs.temperature_message)
    )).text
    print(verdict)


def moisture():
    verdict = requests.get(address + cs.moisture,
                           data=dict(name=input(cs.city_name_message))).text
    print(verdict)


def change_moisture():
    verdict = requests.post(address + cs.change_moisture, data=dict(
        name=input(cs.city_name_message),
        moist=input_for_int(cs.enter_new_moisture_print, cs.moisture_message))).text
    print(verdict)


def temperature_difference():
    verdict = requests.get(address + cs.temperature_difference, data=dict(
        first=input(cs.first_city_print),
        second=input(cs.second_city_print))).text
    print(verdict)


def last_days_statistics():
    verdict = requests.get(address + cs.statistics,
                           data=dict(name=input(cs.city_name_message))).text
    print(verdict)


def make_prediction():
    verdict = requests.get(address + cs.make_prediction,
                           data=dict(name=input(cs.city_name_message))).text
    print(verdict)


command_functions_dict = {"help": print_list,
                          "add city": add_city,
                          "city list": city_list,
                          "temperature": temperature,
                          "change temperature": change_temperature,
                          "moisture": moisture,
                          "change moisture": change_moisture,
                          "temp diff": temperature_difference,
                          "last days statistics": last_days_statistics,
                          "make prediction": make_prediction,
                          "exit": stop_session}

