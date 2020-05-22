import functools
import constants as cs


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
    return cs.city_added


def return_moisture(name, city_dict):
    return cs.moisture_level + str(city_dict[name].get_moisture())


def return_temperature(name, city_dict):
    temperatures = [
        cs.celsius, str(city_dict[name].get_temperature_in_celsius()), "\n",
        cs.fahrenheit, str(city_dict[name].get_temperature_in_fahrenheit()), "\n",
        cs.kelvin, str(city_dict[name].get_temperature_in_kelvins())]
    return "".join(temperatures)


def change_temperature(name, city_dict, new_temp):
    old_temp = city_dict[name].get_temperature_in_celsius()
    city_dict[name].change_temperature(new_temp)
    return_ = [cs.in_, name, cs.temperature_was_changed, str(old_temp), cs.to, str(new_temp)]
    return " ".join(return_)


def change_moisture(name, city_dict, new_moisture):
    old_moisture = city_dict[name].get_moisture()
    city_dict[name].change_moisture(new_moisture)
    return_ = [cs.in_, name, cs.moisture_was_changed, str(old_moisture), cs.to, str(new_moisture)]
    return " ".join(return_)


def make_prediction(name, city_dict):
    data = city_dict[name].make_prediction()
    return_ = [cs.tomorrow_in, name, cs.will_be, str(int(data[0])),
               cs.degrees_by_celsius, cs.moisture_level, cs.will_be, str(int(data[1]))]
    return " ".join(return_)


def statistics(name, city_dict):
    data = city_dict[name].get_statistics()
    days_count = len(data)
    return_ = list()
    for i in range(days_count):
        return_.append(str(days_count - i))
        return_.append(cs.days_ago_temp_was)
        return_.append(str(int(data[i][0])))
        return_.append(cs.degrees_moisture_level)
        return_.append(str(int(data[i][1])))
        return_.append("\n")
    return "".join(return_)

