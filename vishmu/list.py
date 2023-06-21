# numbers = [3, 7, 2, 10, 15]
# print(numbers)
# print(type(numbers))

# Indexing
#  forward indexing
# numbers = [3, 7, 2, 10, 15]
# print(numbers[0])
# print(numbers[3])
# print(numbers[4])

# backward indexing
# numbers = [3, 7, 2, 10, 15]
# print(numbers[-1])
# print(numbers[-3])
# print(numbers[-5])

#slicing
# numbers = [3, 7, 2, 10, 15]
# print(numbers[0:4])
# print(numbers[0:2])
# print(numbers[0:3])
# print(numbers[-3:])
# print(numbers[:])
# print(numbers[1:])
# print(numbers[:3])
#
# print(numbers[0:5:2])


# Modify lists
# numbers = [3, 7, 2, 10, 15]
# print(numbers)
# numbers[0] = 20
# print(numbers)
# numbers[-1] = 50
# print(numbers)

# Adding elements to the list
# append method

# n = [1, 3, 4, 10, 15]
# print(n)
# n.append(50)
# print(n)
# n.append(100)
# print(n)

# extend method

# n = [1, 3, 4, 10, 15]
# print(n)
# l = [10, 20, 30]
# n.extend(l)
# print(n)
# n.extend([40, 50, 60])
# print(n)

# n.insert(0, 10)
# print(n)
# n.insert(4, 60)
# print(n)


# Deleting

# n = [10, 20, 30, 40, 50]
# print(n)
# n.remove(30)
# print(n)
# n.remove(10)
# print(n)

#
# n.pop()
# print(n)
# n.pop(1)
# print(n)
#

# del n[2]
# print(n)
# del n[2]
# print(n)


# n = [10, 20, 30, 40, 50]
# print(n)
# n.clear()
# print(n)
#
# n = [10, 5, 20, 3, 30, ]
# print(n)
# print(len(n))
# print(sorted(n))
#
# print(max(n))
# print(min(n))
# print(sum(n))

# n = [10, 5, 3, 20, 100, 9]
# print(n)
# t = sorted(n)
# print(t)
# print(t[-1])
# print(t[0])
# print(t[-2:])



# n = [10, 5, 30, 100, 200]
#
# m = len(n)
# r = m + 10
# print(r)
# n = [10, 20, 30, 40, 50]
#
# l = sum(n)
# k = len(n)
# s = l/k
# print(s)
#
# l1 = [10, 30, 40, 50, 60, 70, 100]
# l2 = [20, 30, 50, 70, 90]
# l3 = []
#
# for i in l1:
#     if i in l2:
#         l3.append(i)
# print(l3)

# programs
# python program to find largest number in a list
# n = [1, 5, 7, 10, 19]
# l = []
#
# for i in n:
#     if i > 18:
#         l.append(i)
#
# print(l)

# Python program to print the largest even and largest odd numbers in a list
# l = [2, 3, 6, 9, 10, 12]
# E = []
# O = []
#
# for i in l:
#     if i % 2 == 0:
#         E.append(i)
#     else:
#         O.append(i)
#
# print(max(E))
# print(max(O))

# Python program to find average of the list
# l = [1, 3, 5, 6, 8]
# r = sum(l)
# s = len(l)
# h = r/s
# print(h)


# python program to remove duplicates of the list
# l1 = [1, 3, 5, 6, 9, 11, 5, 9, 10]
#
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)

# Reverse String
# s = "vishnu"
# str = ""
# for i in s:
#     print(type(i))
#     str = i+str
# print(str)

# Multiplication table
# num = 20
# num = int(input("Display multiplication table to "))

# for i in range(1,11):
#     print(num,"x", i, "=", num * i)

# num = int(input("Display multiplication table to "))
# range_num = int(input("Enter the numbers to "))
# for i in range(0,range_num+1):
#      print(num,"x", i, "=", num * i)



# list1 = [3, 6, 9, 2]
# l2 = 1
# for i in list1:
#     l2 = l2 * i
#     print(l2)

# list1 = [3, 5, 7, 1, 8]
# l2 = [ ]
# for i in list1:
#     l2.append(i**2)
#     print(l2)

# l1 = [1, 3, 4, 5, 6, 7, 2, 9]
# l2 = [10, 9, 3, 8, 2, 11, 12, 13]
# l3 = []
# non_common = [1,2,3,5]
# for i in l1:
#     if i in l2:
#         l3.append(i)
# print(l3)
# print(list(map(lambda a : a*2,non_common)))
#
# l = [1,2,3,4]
# l1 = ["pavan","jana","vishnu"]
# print(list(zip(l,l1)))
#
# print(dict([(1, 'pavan'), (2, 'jana'), (3, 'vishnu')]))
#
#
# for index, elem in zip(l,l1):
#     print(index, elem)



l = [5, 10, 11, 17, 20, 25]
s = []

for i in l:
    if i >= 25:
        s.append(i)

print(s)
































