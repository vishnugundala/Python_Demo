def f1():
    return "Hello"
print(f1())
print(f1)
print(id(f1))

def wish(name):
    return f'Good morning {name}'


print(wish("Harsha"))
display = wish
print(display("Vishnu"))
print(wish("Suresh"))
print(id(display))
print(id(wish))

del wish
print(display("Janardhan"))