from counter import Counter

class Result:

    list_data     = []
    prime_counter = Counter().set_counter_prime()
    even_counter  = Counter().set_counter_even()
    odd_counter   = Counter().set_counter_odd()


    def __init__(self, list_data):
        self.list_data = list_data

    def find_max_number(self):
        return max(self.list_data)

    def find_min_number(self):
        return min(self.list_data)

    def find_first_number(self):
        return self.list_data[0]

    def find_last_number(self):
        return self.list_data[len(self.list_data)-1]

    def find_number_of_prime_numbers(self, number:int):
        flag = 0 
        for i in range(2, int(number**0.5)+1): 
            if(number % i == 0): 
                flag = 1 
                break 
        if flag == 0 and number > 1: 
            Result.prime_counter += 1

    def find_number_of_even_and_odd_numbers(self, number:int):
        if(number % 2 == 0):
            Result.even_counter += 1
        else:
            Result.odd_counter += 1

    def show_results(self):
        max_number    = str(self.find_max_number())
        min_number    = str(self.find_min_number())
        first_number  = str(self.find_first_number())
        last_number   = str(self.find_last_number())
        prime_numbers = str(self.prime_counter)
        even_numbers  = str(self.even_counter)
        odd_numbers   = str(self.odd_counter)

        print(
            "El máximo número es: " + max_number + "\n" +
            "El mínimo número es: " + min_number + "\n" +
            "El primer número es: " + first_number + "\n" +
            "El último número es: " + last_number + "\n" +
            "La cantidad de números primos es: " + prime_numbers + "\n" +
            "La cantidad de números pares es: " + even_numbers + "\n" +
            "La cantidad de números impares es: " + odd_numbers + "\n"
        )

        self.restart_counters()

    def restart_counters(self):
        Result.prime_counter = Counter().set_counter_prime()
        Result.even_counter  = Counter().set_counter_even()
        Result.odd_counter   = Counter().set_counter_odd()