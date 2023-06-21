# class Test:
#
#     def __init__(self):
#         print("Constructor calling...")
#
#
# t1 = Test()
# t2 = Test()

# Exam 1


# class studentDetails:
#
#     '''
#     This is a student class
#     It displays the number of students
#     '''
#
#     def __init__(self, name, address, phone):
#         self.name = name
#         self.address = address
#         self.mobile = phone
#
#     def display(self):
#         print("Student Name:", self.name)
#         print("Student address:", self.address)
#         print("Student mobile number: ", self.mobile)
#
#
# # print(help(studentDetails))
# # print(studentDetails.__doc__)
#
#
# s1 = studentDetails("Harsha", "Chejarla", "123")
# s1.display()
#
# s2 = studentDetails("Vishnu", "Madapalli", "9440")
# s2.display()


# Exam 2

# class Employee:
#
#     '''
#     This employee class
#     It captures all details
#     '''
#
#     def __init__(self, empid, name, address, phone, designation):
#         self.id = empid
#         self.name = name
#         self.location = address
#         self.mobile = phone
#         self.designation = designation
#
#     def details(self):
#         print("Employee ID: ", self.id)
#         print("Employee Name: ", self.name)
#         print("Employee Location: ", self.location)
#         print("Employee Mobile: ", self.mobile)
#         print("Employ Designation: ", self.designation)
#
#
# # print(help(Employee))
# # print(Employee.__doc__)
# e1 = Employee("100", "Harsha", "Chejarla", "9322", "Trainee")
# e1.details()
#
# e2 = Employee("101", "Vishnu", "Madapalli", "9443", "Associate")
# e2.details()


# class StudentDetails:
#
#     def __init__(self, name, address, phone):
#         self.name = name
#         self.address = address
#         self.mobile = phone
#
#     def display(self):
#         print("student Name:",self.name)
#         print("Student Address:",self.address)
#         print("Student mobile:",self.mobile)
#
# # print(help(StudentDetails))
#
# # print(StudentDetails.__doc__)
#
# s1 = StudentDetails("vishnu", "cjl", "191919")
# s1.display()




# class Student:
#
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#     def contact_info(self, phone):
#         self.mobile = phone
#
# s1 = Student("Harsha","Nlr")
# print(s1.__dict__)
# s1.contact_info("83838")
# print(s1.__dict__)
# s1.age = 92
# print(s1.__dict__)





















