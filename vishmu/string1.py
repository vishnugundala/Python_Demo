# # Defining strings
#
# # name = 'Harsha'
# # print(name)
# #
# # name = "Vishnu"
# # print(name)
# #
# # poem = '''
# # Twinkle twinkle little star
# # how I wonder what you are
# # '''
# # print(poem)
#
# # Accessing
#
# # name = 'Vishnu Vardhan'
# # l = name[0:6]
# # print(l)
# # m = name[0:9]
# # print(m)
# #
# # n = name[-4:]
# # print(n)
# #
# # p = name[:]
# # print(p)
# # r = name[:5]
# # print(r)
#
# # Mathematical operations
# # Concatation
# # first_name = "Vishnu"
# # last_name = "Vardhan"
# # age = 26
# # a = str(age)
# #
# # print("*"*30)
# # print((type(age)))
# # print(type(a))
# # print(age)
# # print(a)
# #
# # full_name = first_name + " " + last_name
# # print(full_name)
# # print(first_name + str(age))
# # print(first_name*3)
# # print("*"*30)
#
# # Membership operators
# # name = "Vishnu vardhan"
# # print("Vishnu" in name)
# # print("Harsha" in name)
#
# # print("Vishnu" not in name)
# # if "vishnu" in name:
# #     print("Available")
# # else:
# #     print("NOt Available")
#
# # Methods
# s = "Harsha"
# print(s.find("sh"))
# print(s.index("sh"))
# print(s.count("a"))
# print(s.count("s"))
# print(s.count("H"))
#
#
# n = " Vishnu"
# # print(n)
# # print(n.lstrip())
# #
# # n1 = "vishnu "
# # print(n1)
# # print(n1.rstrip())
# # print(n.strip())
# #
# # date = "06-02-2023"
# # print(date)
# # rdate = date.split("-")
# # print(rdate)
# #
# # name = "vishnu vardhan"
# # print(name)
# # rname = name.split(" ")
# # print(rname)
# #
# # l = ['06', '02', '2023']
# # print(type(l))
# # m = "-".join(l)
# # print(m)
# # print(type(m))

#
# n = "vishnu vardhan"
# print(n.upper())
# print(n.lower())
# print(n.capitalize())
# print(n.title())
#
# s = "v1"
# print(type(s))
# print(s.isdigit())
# print(s.isalpha())
# print(s.isalnum())
#
# n = "Vishnu"
# print(n.replace("u", "z"))
#
#
# # r = "vishnu101"
# # print(r)
# # rs = ""
# # for item in r:
# #     if item.isalpha():
# #         rs = rs + item
# # print(rs)
#
#
# '''
# txt = "Hello, welcome to my world."
#
# x = txt.find("e", 5, 10)
#
# print(x)
# '''
#
# # s = "The quick brown fox jumps over the lazy dog"
# # rl = s.split(" ")
# #
# # rs = ""
# # for i in rl:
# #     for item in i:
# #         rs = rs + item
# # print(rs)
# # m = len(set(rs.lower()))
# # print(m)
# # if m == 26:
# #     print("This is a pangram")
# # else:
# #     print("It is not pangram")
#
# #
# # s = "The quick brown fox jumps over the lazy dog"
# #
# # rs = ""
# # for i in s:
# #     if type(i) == str:
# #         rs = rs + i
# #     elif i == " ":
# #         continue
# #
# #
# # print(rs)
# # m = len(set(rs.lower()))
# # print(m)
# # if m == 26:
# #     print("This is a pangram")
# # else:
# #     print("It is not pangram")
#
# # s = "harsha"
# # r = " "
# # for i in range(len(s)):
# #     if i % 2 == 0:
# #         r = r + s[i]
# # print(r)
#
# # name = input("Enter Your Name: ")
# # n = int(input("Enter index what we have to remove: "))
# #
# # l = list(name)
# # print(l)
# # del l[n]
# # s = ""
# # for item in l:
# #     s = s+item
# # print(s)
#
# # s = 10
# # for i in range(10):
# #     print(i)
#
# #
# # name = "vardhan"
# # s = " "
# # for item in name:
# #     if item == "a":
# #         s = s + "$"
# #     else:
# #         s = s + item
# # print(s)
#
# # s = "my name is vishnu"
# # l = s.split(" ")
# # print(l)
# # words = len(l)
# # character = 0
# # for item in l:
# #     for i in item:
# #         character = character + 1
# # print(character)
# # print(words)
# #
# #
# # s = "My Name is Vishnu"
# #
# # count = 0
# # for item in s:
# #     if item.islower():
# #         count = count + 1
# # print(count)
#
# # Python program to remove odd index characters in a list
# # name = "vishnu vardhan"
# # result = ""
# #
# # for i in range(len(name)):
# #     if i % 2 == 0:
# #         result = result + str(i)
# # print(result)
#
# # python program Remove odd numbers in a list
# # name = "124589"
# # result = " "
# #
# # for i in range(len(name)):
# #     if i % 2 == 0:
# #         result = result + str(i)
# # print(result)
#
# # Python program to remove nth index character and non empty string
# # string = input("Enter the string name:")
# # n = int(input("Enter the index number :"))
# # first = string[ :n]
# # last = string[n+1: ]
# # print("modify_string",first+last)
#
# # Python program to replace all occurrences 'a' with '$' in a string
# # str = "vishnu vardhan"
# #
# # name = str.replace('a', '$')
# # print(name)
#
# # Python program to replace every blank space with hyphen in a string
# # str = "i have a book"
# # str = input("Enter the string name :")
# # str1 = str.replace('','_')
# # print("original string :",str)
# # print("modify string :",str1)
#
# # st = "vasu vishnu pavan suresh mohan teja vasu mohan"
# # l = st.split(" ")
# # print(l)
# # words = len(l)
# # data = {}
# # for i in l:
# #     if i in data.keys():
# #         data[i] = data[i] + 1
# #     else:
# #         data[i] = 1
# # print(data)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
