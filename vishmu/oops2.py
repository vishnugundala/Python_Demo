# Exa 1 :

# class Student:
#
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#     def contact_info(self, phone):
#         self.mobile = phone
#
#
# s1 = Student("Harsha", "Madapalli")
# print(s1.__dict__)
#
# s1.contact_info("94410")
# print(s1.__dict__)
#
# s1.age = 12
#
# print(s1.__dict__)

# Exa 2:

# class Emplopyee:
#
#     def __init__(self, name):
#         self.name = name
#
#     def contact_info(self, phone):
#         self.phone = phone
#
#     def deleting_name(self):
#         del self.name
#
#
# e1 = Emplopyee("Harsha")
# print(e1.__dict__)
#
# e1.contact_info("9442")
# print(e1.__dict__)
#
# e1.deleting_name()
# print(e1.__dict__)
#
# del e1.phone
# print(e1.__dict__)

# Exa 3:

class Student:
    school_name = "Sri Chaitanya"

    def __init__(self, name, address):
        self.name = name
        self.address = address

        Student.school_address = "Kundhanahalli"

    def contact_info(self):
        Student.school_phone = "944233"
#
    @classmethod
    def head_master_info(cls):
        Student.principal_phone_number = "12345"
        cls.principal_address = "Whitefield"

    @staticmethod
    def vice_principal():
        Student.vice_principal_cotact = "8901"
#
    def display(self):
        print("School Name: ", Student.school_name)
        print("School Address: ", Student.school_address)
        print("School Phone Number: ", Student.school_phone)
        print("School Principal Phone Number: ", Student.principal_phone_number)
        print("Vice Principal Phone Nuber: ", Student.vice_principal_cotact)
        print("Student Name: ", self.name)
        print("Student Address: ", self.address)


s1 = Student("Harsha", "Madapalli")
print(Student.__dict__)
s1.contact_info()
Student.head_master_info()
s1.vice_principal()
s1.display()
Student.unique = "Sri"

print(Student.__dict__)


# Exa 4:

# class Student:
#
#     @staticmethod
#     def addition():
#         x = 10
#         y = 20
#         print(x+y)
#
#
# s1 = Student()
# s1.addition()

# a = 10
# b = a
#
# del a
# print(b)
























