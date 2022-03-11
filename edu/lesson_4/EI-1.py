# class Student:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def update(self):
#         self.name = "Nodir"
#
#     def update_new(self, new_name):
#         self.name = new_name
#
#     def show(self):
#         print("We are inside Student class",self.name, self.age)
# #
# s1 = Student('Sarvar',30)      #self = s1
# s2 = Student("Shaha",19)    #self = s2
# s1.show()                   # self.name = "Sarvar"
#
# s1.update()
# s1.show()                   # self.name = "Nodir"

# s1.update_new("Sevara")
# s1.show()                   # self.name = "Sevara"
# class car:
#     wheels = 4
#     def __init__(self):
#         self.com = "BMW"
#         self.price = 1000
#
# c1 = car()
#
# print(c1.com,c1.price) #BMW 1000
# print(c1.com,c1.price, c1.wheels) #BMW 1000 4

# class Student:
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     def avr(self):
#         return (self.m1+self.m2+self.m3)/3
#
#     def shaha(self):
#         return "Hello Shaha"
#
# s1 = Student(23,67,90)
# print(s1.avr())
# hi = s1.shaha()
# print(hi)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print("The student name is:",self.name, self.age)
#
#     class Laptop:
#         def __init__(self,brand,cpu, ram):
#             self.brand = brand
#             self.cpu = cpu
#             self.ram = ram
#
#         def show(self):
#             print("The PC config is:", self.brand, self.cpu, self.ram)
#
# s1 = Student("Shaha", 19)
# s1.show()
#
# pc1 = Student.Laptop("Apple",'i5',16)
# pc1.show()

class A:
    def feature1(self):
        print("Printing feature 1")
    def feature2(self):
        print("Printing feature 2")

class B(A):
    def feature3(self):
        print("Printing feature 3")
    def feature4(self):
        print("Printing feature 4")

    def feature6(self):
        print("Printing feature 6 form B")

a = A()
b = B()

# a.feature1()
# a.feature2()

# b.feature1()
# b.feature2()
# b.feature3()
# b.feature4()

class C(B):
    def feature5(self):
        print("Printing feature 5")
    def feature6(self):
        print("Printing feature 6")

c = C()

c.feature1()
c.feature3()
c.feature6()



















