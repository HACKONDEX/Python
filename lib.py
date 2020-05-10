from random import random


def input_check(input_):
    while True:
        try:
            tmp = int(input_)
            break
        except ValueError:
            print("Input must be a number!!")
            print("Try again!")
    return tmp


class City:
    def __init__(self, name, temperature, moisture):
        self.name = name
        self.temperature = temperature
        self.moisture = moisture
        statistics = list()
        for i in range(3):
            temperature_change = random() % 6
            moisture_change = random() % 10
            sign = random() % 2
            if sign == 0:
                sign = -1
            statistics.append((temperature + sign * temperature_change, moisture + sign * moisture_change))
        self.statistics = statistics

    def get_temperature_in_kelvins(self):
        return self.temperature + 273

    def get_temperature_in_celsius(self):
        return self.temperature

    def get_temperature_in_fahrenheit(self):
        return self.temperature * (9 / 5) + 32

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
        for i in self.statistics:
            temperature += i[0]
            moisture += i[1]
        temperature /= len(self.statistics)
        moisture /= len(self.statistics) + 1
        return_ = (temperature, moisture)
        return return_


def get_temperature_difference(first_city, second_city):
    difference = first_city.get_temperature_in_celsius() - second_city.get_temperature_in_fahrenheit()
    if difference > 0:
        print("In " + first_city.get_city_name() + " is hotter than in "
              + second_city.get_city_temperature() + "by", difference, " degrees")
    else:
        print("In " + second_city.get_city_name() + " is coder than in "
              + first_city.get_city_temperature() + "by", -difference, " degrees")