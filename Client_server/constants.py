default_port = 8000
default_host = 'localhost'

input_n = ['n', 'N']
input_y = ['y', 'Y']
hello_print = "Hello, you entered Weather control system!"
help_print = "Type 'help' for command list"
command_print = "\nEnter command> "
unknown_command_message = "Unknown command, please try again!"
temperature_message = "Temperature should be a number, try again!"
moisture_message = "Moisture should be a number, try again!"
city_name_message = "Enter city name> "
enter_temp_print = "Enter temperature> "
enter_moisture_print = "Enter moisture> "
enter_new_temp_print = "Enter new temperature> "
enter_new_moisture_print = "Enter new moisture> "
first_city_print = "Enter first city name> "
second_city_print = "Enter second city name> "

stop_session_print1 = "Are you really sure you want to end the session (Y/N)?\n"
stop_session_print2 = "See you next time!"
stop_session_print3 = "It is a better idea"
stop_session_print4 = "Unexpected answer, please try again!"
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

get_city_list = "/get_city_list"
add_city = "/add_city"
temperature = "/temperature"
change_temperature = "/change_temperature"
moisture = "/moisture"
change_moisture = "/change_moisture"
temperature_difference = "/temperature_difference"
make_prediction = "/make_prediction"
statistics = "/statistics"


wrong_input_message = "Input must be a number!!"
hotter = "hotter"
colder = "colder"
degrees_in_celsius = "degrees of Celsius"
no_city_message = "We don't serve this city!!\nCheck the city list using command city list"
wrong_city_message = "One of the cities or both aren't being served!\n" \
              "Please check the serving city list using command city list"
sever_city_message = "We already have this city in our serving cities list!!"
city_added = "City successfully added!!"
moisture_level = "Moisture level "
in_ = "In"
celsius = "Celsius "
fahrenheit = "Fahrenheit "
kelvin = "Kelvin "
temperature_was_changed = "temperature was changed from"
to = "to"
moisture_was_changed = "moisture was changed from"
tomorrow_in = "Tomorrow in"
will_be = "will be"
degrees_by_celsius = "degrees by Celsius."
days_ago_temp_was = " days ago temperature was "
degrees_moisture_level = " degrees in Celsius, moisture level was "
is_ = "is"
than_on = "than on"
by = "by"


def get_fahrenheit_from_celsius(temp):
    return int(temp * (9 / 5) + 32)


def get_kelvin_from_celsius(temp):
    return temp + 273

