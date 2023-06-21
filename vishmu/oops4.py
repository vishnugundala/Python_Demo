# Encapsulation

# class Bank:
#
#     # Public variables
#     bank_name = "State Bank India"
#     name = "Harsha"
#     address = "Madapalli"
#
#     # Private Variables
#     __atm_card_number = "1207463 2178388 28983"
#     __cvv = "923"
#     __phone = "9100344"
#
#     # Protected Variables
#     _account_number = "31797242483987"
#
#     def details(self):
#         return f'Bank name is {Bank.bank_name}, account holder name is {self.name} and address is {Bank.address}'
#
#     def details2(self):
#         return f'ATM card number is {self.__atm_card_number}, CVV is {self.__cvv} and mobile number is {self.__phone}'
#
#     def details3(self):
#         return f'Account number is {self._account_number}'
#
#     def __sensitive_information(self):
#         print(f'Bank name is {Bank.bank_name}, account holder name is {self.name} and address is {Bank.address}')
#
#     def display(self):
#         self.__sensitive_information()
#
#     def _display2(self):
#         print("This is protected method")
#
#
# obj = Bank()
# print(obj.details())
# print(Bank.bank_name)
# print(obj.address)
# print(obj.details2())
# print(obj.__atm_card_number)
# print(obj.__cvv)
# print(obj.details3())
# print(obj._account_number)
# print(obj._Bank__atm_card_number)
# print(obj.__sensitive_information())
# print(obj._Bank__sensitive_information())
# obj.display()
# obj._display2()


# class Insurance(Bank):
#
#     def details4(self):
#         self._display2()
#
#
#
# ob = Insurance()
# ob.details4()


# class Mangling:
#
#     __a = 10
#     __b_ = 20
#     _c = 30
#     ___e_ = 40
#     ___f = 50
#     __g__ = 60
#

# obj = Mangling()
# print(dir(obj))