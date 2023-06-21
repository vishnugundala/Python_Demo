# name = "Vishnu"
# age = 27
#
# print("My name is " + name + " and my age is " + str(age))
# print(f'My name is {name} and my age is {age}')


# def addition(a, b):
#     c = a+b
#     print(c)
#
#
# addition(3, 2)
# addition(1, 3)
# addition(10, 309430039)

# def details(name, age):
#     print(f'My name is {name} and my age is {age}')
#
#
# details("Vishnu", 27)
# details("Harsha", 27)

# Position arguments
# def addition(a, b):
#     c = a + b
#     return c
#
#
# s = addition(3, 5)
# print(s)

# Keywords arguments
# def multiplication(a, b):
#     print(a)
#     print(b)
#     c = a*b
#     return c
#
#
# print(multiplication(b=30, a=10))
# print(multiplication(a=5, b=50))

# Default arguments
# def addition(a, b=10):
#     print(a)
#     print(b)
#     c = a + b
#     return c
#
#
# print(addition(10, 20))
# print(addition(30))

# def data(first_name, last_name, middle_name=""):
#     return f'Full_Name {first_name} {last_name} {middle_name}'
#
#
# print(data("Vishnu", "gundala"))
# print(data("Vishnu", "gundala", "vardhan"))

# Variable length arguments

# def elements(*args):
#     t = args
#     print(type(t))
#     for item in t:
#         print(item)
#     return sum(t)
#
#
# print(elements(10, 5, 3))
# print(elements(10, 5, 3, 34, 89))


# def details(**kwargs):
#     d = kwargs
#     print(type(d))
#     return d
#
#
# print(details(name="Vishnu", age=27))
# print(details(name="Vishnu", age=27, phone=1234, address="Chejarla"))

'''
Examples:

def lst(l):
    return l


print(lst([10, 5, 3, 2]))
print(lst((10, 5, 3, 2)))
print(lst({"name": "Vishnu", "age": 27}))


def bigger_element(l):
    b = l[0]
    for item in l:
        if item > b:
            b = item
    return b


print(bigger_element([10, 2, 3, 50]))


def element_addition(l, n):
    l.append(n)
    return l


print(element_addition([10, 2, 3, 50], 80))
'''

# Scope
# 1.local scope
# 2.global scope

a = 10
b = 60

def display():
    global b
    b = 70
    return a


print(display())
print(b)
#
#
# def display2():
#     return a
#
#
# print(display2())
#
#
# def display3(b):
#     c = a + b
#     return c
#
#
# print(display3(50))
#
#
# def d1():
#     global a
#     a = 10
#     return a
#
#
# def d2():
#     a = 30
#     return a
#
#
# print(d1())
# print(d2())

# Lambda
# r = lambda a, b: a + b
# print(r(3, 4))

# Filter
# l = [10, 2, 3, 5]

# r = list(filter(lambda a:a%2==0, l))
# print(r)

# r = list(filter(lambda a:a if a>=5 else None, l))
# print(r)

# Map
# l = [10, 2, 3, 5]

# r = tuple(map(lambda a:a*a, l))
# print(r)

# l = [20, 50, 30]
#
# r = tuple(map(lambda a:a+30, l))
# print(r)

# Reduce
# from functools import reduce
# l = [20, 50, 30, 10]
# r = reduce(lambda x,y: x+y, l)
# print(r)

# Enumerate
# l = [20, 50, 30, 10]
#
# for i, e in enumerate(l):
#     print(f'Index {i} and element {e}')

# name = "Vishnu"
# age = 27
#
# print("My name is "+name+ " and age is "+ str(age))
# print(f'My name is {name} and my age is {age}')


# # lambda
# r = lambda a,b : a + b
# print(r(3,5))














