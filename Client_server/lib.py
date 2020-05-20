def input_check(input_):
    while True:
        try:
            input_int = int(input_)
            break
        except:
            print("Input must be a number!!")
            raise
    return input_int


class City:
    def __init__(self, name, temperature, moisture):
        self.name = name
        self.temperature = input_check(temperature)
        self.moisture = input_check(moisture)
        self.statistics = [(temperature, moisture)]

    def get_temperature_in_kelvins(self):
        return self.temperature + 273

    def get_temperature_in_celsius(self):
        return self.temperature

    def get_temperature_in_fahrenheit(self):
        return int(self.temperature * (9 / 5) + 32)

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
    return_ = ["In ", first_city.get_city_name(), " is ", "", " than in ",
               second_city.get_city_name(), " by ", "", " degrees of Celsius"]
    if difference > 0:
        return_[3] = "hotter"
        return_[7] = str(difference)
    else:
        return_[3] = "colder"
        return_[7] = str(-difference)
    return "".join(return_)

