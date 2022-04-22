from result import Result
from counter import Counter

import json

class DataFinal:
    counter_json = Counter().set_counter_json()
    datoI        = json
    type         = int
    list_data    = []


    def __init__(self, datoI):
        self.datoI = datoI

    def load_json(self):
        json_data = self.datoI
        data_dict = json.loads(json_data)
        return data_dict
        
    def create_list(self, data_dict):
        self.list_data.append(data_dict['b'])
        return self.list_data

    def call_prime_even_odd(self, number: int):
        results = Result([])
        results.find_number_of_prime_numbers(number)
        results.find_number_of_even_and_odd_numbers(number)

    def stop_counter(self, counter):
        if counter == 60000:
            Result(self.list_data).show_results()
            self.list_data.clear()
            counter = self.counter_json
            return counter
        return counter

    def run_data_final(self, counter):
        data_dict = self.load_json()
        data_list = self.create_list(data_dict)
        self.call_prime_even_odd(data_list[counter-1])
        counter = self.stop_counter(counter)
        return counter

