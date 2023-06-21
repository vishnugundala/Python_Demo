# Inheritance
# Simple Inheritance

# class Person:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#     def details(self):
#         print("This is from parent class")
#
#     def display(self):
#         print(f'My name is {self.name} from {self.address}')
#
#
# ob = Person("Vishnu", "Chejarla")
# ob.display()
#
#
# class Employee(Person):
#     def __init__(self, name, address, empid)
#         super()=__init__(name, address)
#         self.empid = empid
#
#     def display(self):
#         print(f'My name is {self.name} and employee id is {self.empid} from {self.address}')
#
#     def details(self):
#         super().details()
#         print("This is from child class")
#
#
# obj = Employee("Harsha", "Madapalli", "100")
# print(obj.__dict__)
#
# obj.display()
# obj.details()

# Multilevel Inheritance

# class Parent:
#     def lands(self):
#         return "He contains lands"
#
#     def diamonds(self):
#         return "He owns diamonds"
#
#
# class Child1(Parent):
#     def gold(self):
#         return "He contains gold"
#
#
# class Child2(Child1):
#     def cash(self):
#         return "He owns cash"
#
#
# obj = Child2()
# print(obj.cash())
# print(obj.lands())
# print(obj.gold())
# print(obj.diamonds())


# Multiple Inheritance

# class GranFather():
#     def house(self):
#         return "He owns house"
#
# class Father:
#     def lands(self):
#         return "He have lands"
#
#     def cash(self):
#         return "He own a cash"
#
#
# class Mother:
#     def gold(self):
#         return "She contains a gold"
#
#
# class Son(Father, Mother, GranFather):
#     def job(self):
#         return "He achieved a job"
#
#
# obj = Son()
# print(obj.house())
# print(obj.lands())
# print(obj.cash())
# print(obj.gold())
# print(obj.job())

# Hierarchical Inheritance
# Exam 1

class Father:
    def house(self):
        return "He owns a house"


class Son1(Father):
    def lands(self):
        return "He owns a lands"


class Son2(Father):
    def gold(self):
        return "He owns a gold"


obj = Son2()
print(obj.gold())
print(obj.house())

# Exam 2

class GrandFather:
    def house(self):
        return "He owns a house"


class Child1(GrandFather):
    def lands(self):
        return "He owns a lands"


class Child2(GrandFather):
    def cash(self):
        return "He owns a cash"


class GrandChild(Child1, Child2):
    def gold(self):
        return "He owns a gold"


obj = GrandChild()
print(obj.house())
print(obj.cash())

# Hybrid Inheritance

# class Dog:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
# class Robo:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#
#
# class RoboDog(Dog, Robo):
#     def __init__(self, name, color, height, width, model_no):
#         Dog.__init__(self, name, color)
#         Robo.__init__(self, height, width)
#         self.model = model_no
#
#     def talk(self):
#         return f'Hi my name is {self.name}, color is {self.color}, height is {self.height}, width is {self.width} and my model number is {self.model}'
#
#
# obj = RoboDog("Chitti", "grey", "5", "2", "193")
# print(obj.talk())












































