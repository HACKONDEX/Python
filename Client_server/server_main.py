import flask
import lib
import server_functions
from server_functions import check_name_and_do_request

application = flask.Flask('Weather-control-system')
city_list = ["Vladivostok", "Moscow"]
city_dict = {"Vladivostok": lib.City("Vladivostok", 15, 70), "Moscow": lib.City("Moscow", 20, 40)}
no_city_message = "We don't serve this city!!\nCheck the city list using command city list"


@application.route('/get_city_list', methods=['GET'])
def get_city_list():
    return " ".join(city_list)


@application.route('/add_city', methods=['POST'])
def add_city():
    name = flask.request.form["name"]
    temp = flask.request.form["temp"]
    moist = flask.request.form["moist"]
    return check_name_and_do_request \
        (name, city_list, "We already have this city in our serving cities list!!", False) \
        (server_functions.add_city) \
        (lib.City(name, int(temp), int(moist)), city_list, city_dict)


@application.route('/temperature', methods=['GET'])
def temperature():
    return check_name_and_do_request(flask.request.form["name"], city_list, no_city_message, True) \
        (server_functions.return_temperature) \
        (flask.request.form["name"], city_dict)


@application.route('/change_temperature', methods=['POST'])
def change_temperature():
    return check_name_and_do_request(flask.request.form["name"], city_list, no_city_message, True) \
        (server_functions.change_temperature) \
        (flask.request.form["name"], city_dict, int(flask.request.form["temp"]))


@application.route('/moisture', methods=['GET'])
def moisture():
    return check_name_and_do_request \
        (flask.request.form["name"], city_list, no_city_message, True) \
        (server_functions.return_moisture) \
        (flask.request.form["name"], city_dict)


@application.route('/change_moisture', methods=['POST'])
def change_moisture():
    name = flask.request.form["name"]
    new_moist = int(flask.request.form["moist"])
    return check_name_and_do_request(name, city_list, no_city_message, True) \
        (server_functions.change_moisture)(name, city_dict, new_moist)


@application.route('/temperature_difference', methods=['GET'])
def temperature_difference():
    first_name = flask.request.form["first"]
    second_name = flask.request.form["second"]
    message = "One the cities or both aren't being served!\n" \
              "Please check the serving city list using command city list"
    if check_name_and_do_request(first_name, city_list, False, True) \
            (server_functions.return_true)() and \
            check_name_and_do_request(second_name, city_list, False, True) \
            (server_functions.return_true)():
        return lib.get_temperature_difference(city_dict[first_name], city_dict[second_name])
    else:
        return message


@application.route('/make_prediction', methods=['GET'])
def make_prediction():
    return check_name_and_do_request(flask.request.form["name"], city_list, no_city_message, True) \
        (server_functions.make_prediction)(flask.request.form["name"], city_dict)


@application.route('/statistics', methods=['GET'])
def statistics():
    return check_name_and_do_request(flask.request.form["name"], city_list, no_city_message, True) \
        (server_functions.statistics)(flask.request.form["name"], city_dict)


def main():
    application.run('::', port=8000, debug=True)


main()
