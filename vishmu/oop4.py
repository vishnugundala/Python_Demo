#1 Operator overloading

# class A:
#     def __init__(self, a):
#         self.a = a
#         print(self.a)
#
#     def __add__(self, other):
#         return self.a + other.a
#
#
#
# obj1 = A(30)
# obj2 = A(50)
# print(obj1 + obj2)

# Method overriding

class Parent:
    def marriage(self):
        print("Parent arranged marriage with x")


class Child(Parent):
    def marriage(self):
        print("Child himself choosen a brid")


obj = Child()
obj.marriage()

# Exam
# class Mobile:
#     def __init__(self, price, model_no):
#         self.price = price
#         self.model_no = model_no
#
#     def getPrice(self):
#         return  self.price
#
#     def getModel(self):
#         return self.model_no
#
#     def discountedPrice(self):
#         return self.price * (10/100)
#
#
# class Iphone(Mobile):
#     def __init__(self, price, model_no):
#         super().__init__(price, model_no)
#
#     def iphoneUnique(self):
#         print("It has unique features")
#
#     def discountedPrice(self):
#         return self.price * (40/100)
#
#
# class Samsung(Mobile):
#     def __init__(self, price, model_no):
#         super().__init__(price, model_no)
#
#     def discountedPrice(self):
#         return self.price * (30/100)
#
#     def samsungUnique(self):
#         print("Samsung has unique features")
#
#
# iobj = Iphone(45000, "Iphone 14")
# print(iobj.getPrice())
# print(iobj.getModel())
# print(iobj.discountedPrice())
#
# sobj = Samsung(30000, "Samsung galaxy")
# print(sobj.getPrice())
# print(sobj.getModel())
# print(sobj.discountedPrice())

#
# 3
# class A:
#     def __init__(self):
#         print("This is class A constructor")
#
#
# class B(A):
#     # def __init__(self):
#     #     print("THis  is class B constructor")
#
#     pass
#
#
# obj = B()





















