from abc import ABC, abstractmethod

#
# class Main(ABC):
#
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#     def display(self):
#         return "This is normal method"
#
#
# class Main2(Main):
#
#     def display1(self):
#         return "THis is displa1 implementation"
#
#     def display2(self):
#         return "This is display2 implementation"
#
#     def display3(self):
#         return "This is display 3"
#
#
# obj = Main2()
# print(obj.display1())
# print(obj.display())
# print(obj.display2())
# print(obj.display3())


class Polygon(ABC):

    @abstractmethod
    def sides(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def concrete_method(self):
        return "All polygons are two dimensional "


class Rectangle(Polygon):

    def sides(self, length, breath):
        self.length = length
        self.breath = breath

    def area(self):
        return self.length * self.breath

    def perimeter(self):
        return 2 * (self.length + self.breath)


class Square(Polygon):

    def sides(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# obj = Rectangle()
# obj.sides(3, 4)
# print(obj.area())
# print((obj.perimeter()))

obj = Square()
obj.sides(3)
print(obj.area())
print((obj.perimeter()))






















