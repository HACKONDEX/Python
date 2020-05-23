import constants as cs


def input_check(input_):
    while True:
        try:
            input_int = int(input_)
            break
        except ValueError as error:
            print(cs.wrong_input_message)
            raise ValueError from error
        except TypeError as error:
            print(cs.wrong_input_message)
            raise TypeError from error
    return input_int


class City:
    def __init__(self, name, temperature, moisture):
        self.name = name
        self.temperature = input_check(temperature)
        self.moisture = input_check(moisture)
        self.statistics = [(temperature, moisture)]

    def get_temperature_in_kelvins(self):
        return cs.get_kelvin_from_celsius(self.temperature)

    def get_temperature_in_celsius(self):
        return self.temperature

    def get_temperature_in_fahrenheit(self):
        return cs.get_fahrenheit_from_celsius(self.temperature)

    def get_moisture(self):
        return self.moisture

    def change_temperature(self, new_temperature):
        tmp = input_check(new_temperature)
        self.statistics.append((self.temperature, self.moisture))
        self.temperature = tmp

    def change_moisture(self, new_moisture):
        tmp = input_check(new_moisture)
        self.statistics.append((self.temperature, self.moisture))
        self.moisture = tmp

    def get_city_name(self):
        return self.name

    def get_statistics(self):
        return self.statistics

    def make_prediction(self):
        temperature = self.temperature
        moisture = self.moisture
        for t, m in self.statistics:
            temperature += t
            moisture += m
        temperature /= len(self.statistics)
        moisture /= len(self.statistics) + 1
        return temperature, moisture


def get_temperature_difference(first_city, second_city):
    difference = int(first_city.get_temperature_in_celsius()) - int(second_city.get_temperature_in_celsius())
    hotter_colder = cs.hotter
    if difference > 0:
        difference = str(difference)
    else:
        hotter_colder = cs.colder
        difference = str(-difference)
    return f"{cs.in_} {first_city.get_city_name()} {cs.is_} {hotter_colder} {cs.than_on} " \
           f"{second_city.get_city_name()} {cs.by} {difference} {cs.degrees_in_celsius}"

