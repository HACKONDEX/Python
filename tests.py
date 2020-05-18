import lib
from lib import City
import unittest


class TestCity(unittest.TestCase):
    def test_temperature_in_celsius(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(havana.get_temperature_in_celsius(), 25)

    def test_temperature_in_kelvin(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(havana.get_temperature_in_kelvins(), havana.get_temperature_in_celsius() + 273)

    def test_temperature_in_fahrenheit(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(havana.get_temperature_in_fahrenheit(), 77)

    def test_temperature_change(self):
        havana = City("Havana", 25, 70)
        helsinki = City("Helsinki", -10, 50)
        havana.change_temperature(45)
        self.assertEqual(havana.get_temperature_in_celsius() - helsinki.get_temperature_in_celsius(), 55)

    def test_moisture(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(havana.get_moisture(), 70)

    def test_moisture_change(self):
        havana = City("Havana", 25, 70)
        helsinki = City("Helsinki", -10, 50)
        havana.change_moisture(100)
        self.assertEqual(havana.get_moisture() - helsinki.get_moisture(), 50)

    def test_wrong_input_1(self):
        with self.assertRaises(ValueError):
            City("Monte-Carlo", "temp", 45)

    def test_wrong_input_2(self):
        with self.assertRaises(TypeError):
            City("Athens", 20, (1, True))

    def test_wrong_argument_1(self):
        with self.assertRaises(ValueError):
            havana = City("Havana", 25, 70)
            havana.change_moisture("$")

    def test_wrong_argument_2(self):
        with self.assertRaises(ValueError):
            havana = City("Havana", 25, 70)
            havana.change_temperature("&")

    def test_wrong_argument_3(self):
        with self.assertRaises(TypeError):
            havana = City("Havana", 25, 70)
            havana.change_moisture([1, 2, "sda"])

    def test_wrong_argument_4(self):
        with self.assertRaises(TypeError):
            havana = City("Havana", 25, 70)
            havana.change_temperature((5, 6))

    def test_return_type_1(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(int, type(havana.get_temperature_in_celsius()))

    def test_return_type_2(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(int, type(havana.get_moisture()))

    def test_return_type_3(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(int, type(havana.get_temperature_in_fahrenheit()))

    def test_return_type_4(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(int, type(havana.get_temperature_in_kelvins()))

    def test_return_type_5(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(str, type(havana.get_city_name()))

    def test_return_type_6(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(tuple, type(havana.make_prediction()))

    def test_city_name(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(havana.get_city_name(), "Havana")

    def test_make_prediction(self):
        havana = City("Havana", 25, 70)
        self.assertEqual(havana.make_prediction(), (50.0, 70.0))
