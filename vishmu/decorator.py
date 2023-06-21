# def f1():
#     return "Hello"
#
#
# print(f1())
# print(f1)
# print(id(f1))

# def wish(name):
#     return f'Good morning {name}'


# print(wish("Harsha"))
# display = wish
# print(display("Vishnu"))
# print(wish("Suresh"))
# print(id(display))
# print(id(wish))
#
# del wish
# print(display("Janardhan"))

# def outer():
#     print("Outer function execution starts")
#
#     def inner():
#         print("Inner function execution")
#     print("Outer function execution ends")
#
#
# outer()

# def outer():
#     print("Outer function execution starts")
#
#     def inner():
#         print("Inner function execution")
#     inner()
#     print("Outer function execution ends")
#
#
# outer()

# def outer():
#
#     def inner(name):
#         return f"Good morning {name}"
#     return inner
#
#
# f1 = outer()
# print(f1("Harsha"))
#
# def f1():
#     print("Hello")
#
#
# def f(func):
#     func()
#
#
# f(f1)

# def decor(func):
#
#     def inner():
#         r = func()
#         n = "This is a decorated function"
#         return r+n
#     return inner
#
#
# @decor
# def display():
#     return "Hello"


# print(display())


# import datetime
#
#
# def decor(func):
#
#     def inner(name):
#         d = datetime.datetime.now()
#         r = func(name)
#         return f'Wishing at {d} {r}'
#     return inner
#
#
# @decor
# def display(name):
#     return f'Good morning {name}'
#
#
# print(display("Harsha"))


# def decor(func):
#
#     def inner():
#         author = "Guido Van Rosum"
#         r = func()
#         return f'{r} by {author}'
#     return inner
#
#
# @decor
# def title():
#     return "How to learn Python"
#
#
# print(title())

# def login_required(func):
#
#     def inner():
#         email_id = input("Enter Your Email Id: ")
#         password = input("Enter Your Password: ")
#         if email_id == "admin@gmail.com" and password == "admin123":
#             return func()
#         else:
#             return "Please Provide Valid Credentials"
#     return inner
#
#
# @login_required
# def profile():
#     return "This is your profile"
#
#
# print(profile())


# def login_required(func):
#
#     def inner(email, password):
#         email_id = email
#         password = password
#         if email_id == "admin@gmail.com" and password == "admin123":
#             return func(email, password)
#         else:
#             return "Please Provide Valid Credentials"
#     return inner
#
#
# @login_required
# def profile(email, password):
#     return "This is your profile"
#
#
# print(profile("admin@gmail.com", "admin123"))


# def publication(func):
#
#     def inner():
#         pb = "Python Foundation"
#         r = func()
#         return pb + r
#     return inner
#
#
# def author(func):
#
#     def inner():
#         author = "Guido Van Rosum"
#         r = func()
#         return author + r
#     return inner
#
#
# @publication
# @author
# def title():
#     return "How to learn Python"
#
#
# print(title())







































