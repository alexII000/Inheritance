class Person:
    def __init__(self, name, address, tel_num):
        self.__name = name
        self.__address = address
        self.__tel_num = tel_num

    def print_person(self):
        return self.__name
        return self.__address
        return self.__tel_num


class Customer(Person):
    def __init__(self, cust_num):
        self.__cust_num = cust_num
