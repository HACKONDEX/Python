import flask
import lib
import server_functions
import constants as cs
from server_functions import check_name_and_do_request

application = flask.Flask('Weather-control-system')
city_list = ["Vladivostok", "Moscow"]
city_dict = {city_list[0]: lib.City(city_list[0], 15, 70), city_list[1]: lib.City(city_list[1], 20, 40)}


@application.route(cs.get_city_list, methods=['GET'])
def get_city_list():
    return " ".join(city_list)


@application.route(cs.add_city, methods=['POST'])
def add_city():
    name = flask.request.form["name"]
    temp = flask.request.form["temp"]
    moist = flask.request.form["moist"]
    return check_name_and_do_request \
        (name, city_list, cs.sever_city_message, False) \
        (server_functions.add_city) \
        (lib.City(name, int(temp), int(moist)), city_list, city_dict)


@application.route(cs.temperature, methods=['GET'])
def temperature():
    return check_name_and_do_request(flask.request.form["name"], city_list, cs.no_city_message, True) \
        (server_functions.return_temperature) \
        (flask.request.form["name"], city_dict)


@application.route(cs.change_temperature, methods=['POST'])
def change_temperature():
    return check_name_and_do_request(flask.request.form["name"], city_list, cs.no_city_message, True) \
        (server_functions.change_temperature) \
        (flask.request.form["name"], city_dict, int(flask.request.form["temp"]))


@application.route(cs.moisture, methods=['GET'])
def moisture():
    return check_name_and_do_request \
        (flask.request.form["name"], city_list, cs.no_city_message, True) \
        (server_functions.return_moisture) \
        (flask.request.form["name"], city_dict)


@application.route(cs.change_moisture, methods=['POST'])
def change_moisture():
    name = flask.request.form["name"]
    new_moist = int(flask.request.form["moist"])
    return check_name_and_do_request(name, city_list, cs.no_city_message, True) \
        (server_functions.change_moisture)(name, city_dict, new_moist)


@application.route(cs.temperature_difference, methods=['GET'])
def temperature_difference():
    first_name = flask.request.form["first"]
    second_name = flask.request.form["second"]
    if check_name_and_do_request(first_name, city_list, False, True) \
            (lambda: True)() and \
            check_name_and_do_request(second_name, city_list, False, True) \
            (lambda: True)():
        return lib.get_temperature_difference(city_dict[first_name], city_dict[second_name])
    else:
        return cs.wrong_city_message;


@application.route(cs.make_prediction, methods=['GET'])
def make_prediction():
    return check_name_and_do_request(flask.request.form["name"], city_list, cs.no_city_message, True) \
        (server_functions.make_prediction)(flask.request.form["name"], city_dict)


@application.route(cs.statistics, methods=['GET'])
def statistics():
    return check_name_and_do_request(flask.request.form["name"], city_list, cs.no_city_message, True) \
        (server_functions.statistics)(flask.request.form["name"], city_dict)


def main():
    application.run('::', port=cs.default_port, debug=True)


if __name__ == "__main__":
    main()

