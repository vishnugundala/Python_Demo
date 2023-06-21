# simple objects
# numbers
a = 10
b = 20.5
c = 4 + 5j
print(a, type(a), id(a))
print(b, type(b), id(b))
print(c, type(c), id(c))


# strings
s1 = "w"
s2 = 'hello'
s3 = """ abc 12335567
xyz
"""
print(s1, type(s1), id(s1))
print(s3, type(s3), id(s3))

# Container objects
# list
l = [10, 20, 30, 50.6, 4+5j, "welcome"]
print(l, type(l), id(l), l[3])



# tuple
t = (10, 20, 30, 50.6, 4+5j, "welcome")
print(t, type(t), id(t), t[2])

# set
s = {10, 20, 30, 50.6, 4+5j, "welcome"}
print(s, type(s), id(s))

# dictionary
d = {"mango": 10, "banana": 40, "apple": 80}
print(d, type(d), id(d), d["banana"])