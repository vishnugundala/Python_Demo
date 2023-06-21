# d = {
#     "name": "Vishnu",
#     "age": 27,
#     "weight": 67.5
# }

# print(d)
# print(type(d))
# print(d["name"])
# print(d["weight"])
# print(d["age"])
# print(d["address"])

# print(d.get("name"))
# print(d.get("middle_name", 0))
# print(d.get("weight"))
# print(d.get("address"))


# d = {
#     "name": "Vishnu",
#     "age": 27
# }
# print(d)
# d["name"] = "Harsha"
# d["address"] = "Chajarla"
# print(d)
#
# d = {}
# print(d)
# d["name"] = "Vishnu"
# d["age"] = 27
# d["weight"] = 67.5
# print(d)

# d = {
#     "name": "Vishnu"
# }
# print(d)
# d1 = {
#     "age": 27,
#     "weight": 65.7,
#     "address": "Chejarla"
# }
#
# d.update(d1)
# print(d)

# Copy method
# d = {
#     "name": "Vishnu",
#     "address": "Chejarla"
# }
# print(d)
#
# d1 = d.copy()
# print(d1)

# Nested dictionaries
# d = {
#     "name": "Vishnu",
#     "address": "Chejarla",
#     "kids": {
#         "son": "Ram",
#         "daughter": "Laxmi"
#     },
#     "cars": ["BMW", "Tesla", "Benz"]
# }
#
# print(d)
# print(d["name"])
# print(d["address"])
# print(d["kids"])
# print(d["kids"]["son"])
# print(d["cars"][1])
#
# d["kids"]["son"] = "Laxman"
# d["cars"][-1] = "Maruti suzuki"
# print(d)


# d = {
#     "name": "Vishnu",
#     "age": 27,
#     "address": "Chejarla"
# }
# print(d)
#
# del d["age"]
# del d["address"]
#
# d.pop("name")
# d.pop("address")
#
# d.popitem()
# d.popitem()
#
# d.clear()

#del d
# print(d)

# Methods
# d = {
#     "a": 10,
#     "b": 5,
#     "c": 2
# }
# print(d)
#
# k = []
#
# for item in d.keys():
#     k.append(item)
# print(k)
#
# v = []
#
# for item in d.values():
#     v.append(item)
# print(v)

# print(d.items())
# print(d.keys())
# print(d.values())

# for k, v in d.items():
#     print(k, '---', v)












#  Nested dictionaries
# d = {
#     "name" : "harsha",
#     "address" : "chejerla"
#     "kids": {
#            "son": "rana"
#            "daughter":
# }
# }
#
# print(d)
# print(d["name"])
# print(d["address"])
# print(d["kids"]["son"])
# print(d["son"]["daughter"])
# print(d["cars"][-1])
#
# d["kids"]["son"] = "vishnu"
# d["kids"]["daughter"] = "harsha"
# print(d)


# def emp_pho_num():
#     while True:
#         number = int(input("Enter the number:"))
#         emp_pho_num = 10
#         if emp_pho_num == len(str(number)):
#             return number
#
#             break
#         else:
#             print("Invalid Phone number Please Enter valid phone number")
# result = emp_pho_num()







# emp_pho_num = number
# print(emp_pho_num)

















