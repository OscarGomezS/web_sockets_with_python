from dataInitial import DataInitial
from dataFinal import DataFinal
from result import Result

import unittest
import json

"""
class TestDataInitial(unittest.IsolatedAsyncioTestCase):

    async def test_functionality_of_listen_server(self):
        url = "ws://209.126.82.146:8080"
        result = await DataInitial(url).listen_server()
        self.assertEqual(type(json), type(result))

    def test_run_loop_function(self):
        pass """

def create_json():
    data_json = json.dumps({"a": 1, "b": 2})
    return data_json

def create_dict():
    dict = {"a": 1, "b": 2}
    return dict

def create_list():
    list = [0, 1, 2]
    return list

class TestDataFinal(unittest.TestCase):

    def test_load_json(self):
        """
        Test to prove if load_json() return a dictionary.
        """
        data_json = create_json()
        dataFinal = DataFinal(data_json).load_json()
        data_dict = create_dict()
        self.assertEqual(type(data_dict), type(dataFinal))
        

    def test_create_list(self):
        """
        Test to set if the create_list() function returns a list after entering a dictionary
        """
        data_json = create_json()
        data_dict = create_dict()
        data_list = create_list()
        dataFinal = DataFinal(data_json).create_list(data_dict)
        self.assertEqual(type(data_list), type(dataFinal))

    def test_stop_counter(self):
        """
        Test to set if the stop_counter() function returns a counter equals to zero after entering
        a counter equals to 60000
        """
        data_json = create_json()
        counter = 60000
        counter_return = DataFinal(data_json).stop_counter(counter)
        self.assertEqual(0, counter_return)

class TestResult(unittest.TestCase):

    def test_find_max_number(self):
        """
        Test to set if find_max_number() function returns a maximun number from a list
        """
        data_list = create_list()
        result = Result(data_list).find_max_number()
        self.assertEqual(max(data_list), result)

    def test_find_min_number(self):
        """
        Test to set if find_min_number() function returns a minimun number from a list
        """
        data_list = create_list()
        result = Result(data_list).find_min_number()
        self.assertEqual(min(data_list), result)

    def test_find_first_number(self):
        """
        Test to set if find_first_number() function returns the first number of a list
        """
        data_list = create_list()
        result = Result(data_list).find_first_number()
        self.assertEqual(data_list[0], result)

    def test_find_last_number(self):
        """
        Test to set if find_last_number() function returns the last number of a list
        """
        data_list = create_list()
        result = Result(data_list).find_last_number()
        last_index = len(data_list) - 1
        self.assertEqual(data_list[last_index], result)

    def test_find_number_of_prime_numbers(self):
        """
        Test to set if find_number_of_prime_numbers() function returns one when it's entering a prime
        number
        """
        data_list = create_list()
        prime_number = 2
        Result(data_list).find_number_of_prime_numbers(prime_number)
        self.assertEqual(1, Result.prime_counter)

    def test_find_number_of_even_numbers(self):
        """
        Test to set if find_number_of_even_and_odd_numbers() function returns one when it's entering 
        a even number
        """
        data_list = create_list()
        even_number = 2
        Result(data_list).find_number_of_even_and_odd_numbers(even_number)
        self.assertEqual(1, Result.even_counter)
    
    def test_find_number_of_odd_numbers(self):
        """
        Test to set if find_number_of_even_and_odd_numbers() function returns one when it's entering 
        a odd number
        """
        data_list = create_list()
        odd_number = 1
        Result(data_list).find_number_of_even_and_odd_numbers(odd_number)
        self.assertEqual(1, Result.odd_counter)


if __name__=='__main__':
    unittest.main()
