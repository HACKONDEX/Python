import flask
import lib
import server_functions

application = flask.Flask('Weather-control-system')
city_list = ["Vladivostok", "Moscow"]
city_dict = {"Vladivostok": 0, "Moscow": 1}
city_system = [lib.City("Vladivostok", 15, 70), lib.City("Moscow", 20, 40)]


def add(city):
    city_list.append(city.get_city_name())
    city_system.append(city)
    city_dict[city.get_city_name()] \
        = len(city_dict)

@application.route('/get_city_list', methods=['GET'])
def get_city_list():
    return_ = " "
    return return_.join(city_list)


@application.route('/add_city', methods=['POST'])
def add_city():
    name = flask.request.form["name"]
    if name in city_list:
        return "We already have this city in our served cities!"
    temp = flask.request.form["temp"]
    moist = flask.request.form["moist"]
    city = lib.City(name, int(temp), int(moist))
    add(city)
    return "City successfully added"


def main():
    application.run('::', port=8000, debug=True)


# if __name__ == '__server_main__':
#     main()

main()
