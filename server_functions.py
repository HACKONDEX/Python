import lib
import functools


def check_name_and_do_request(name, city_list, error_message, need_to_be_in_list):
    def function_call(function):
        @functools.wraps(function)
        def wrapper(*args, **kwarg):
            if (name not in city_list) == need_to_be_in_list:
                return error_message
            else:
                return function(*args, **kwarg)

        return wrapper

    return function_call


def add_city(city, city_list, city_dict):
    city_list.append(city.get_city_name())
    city_dict[city.get_city_name()] = city
    return "City successfully added!!"


def return_moisture(name, city_dict):
    return "Moisture level " + str(city_dict[name].get_moisture())


def return_temperature(name, city_dict):
    temperatures = [
        "Celsius ", str(city_dict[name].get_temperature_in_celsius()), "\n",
        "Fahrenheit ", str(city_dict[name].get_temperature_in_fahrenheit()), "\n",
        "Kelvin ", str(city_dict[name].get_temperature_in_kelvins())]
    return_ = ""
    return return_.join(temperatures)


def change_temperature(name, city_dict, new_temp):
    old_temp = city_dict[name].get_temperature_in_celsius()
    city_dict[name].change_temperature(new_temp)
    return_ = ["In", name, "temperature was changed from", str(old_temp), "to", str(new_temp)]
    return " ".join(return_)


def change_moisture(name, city_dict, new_moisture):
    old_moisture = city_dict[name].get_moisture()
    city_dict[name].change_moisture(new_moisture)
    return_ = ["In", name, "moisture was changed from", str(old_moisture), "to", str(new_moisture)]
    return " ".join(return_)


def make_prediction(name, city_dict):
    data = city_dict[name].make_prediction()
    return_ = ["Tomorrow in", name, "will be", str(int(data[0])),
               "degrees by Celsius.", "Moisture level will be", str(int(data[1]))]
    return " ".join(return_)


def statistics(name, city_dict):
    data = city_dict[name].get_statistics()
    days_count = len(data)
    return_ = list()
    for i in range(days_count):
        return_.append(str(days_count - i))
        return_.append(" days ago temperature was ")
        return_.append(str(int(data[i][0])))
        return_.append(" degrees in Celsius, moisture level was ")
        return_.append(str(int(data[i][1])))
        return_.append("\n")
    return "".join(return_)
