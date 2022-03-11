#
# class Computer(object):
#     #атрибуты
#     def __init__(self,cpu, ram):
#         self.cpu = cpu
#         self.ram = ram
#
#     def config(self):
#         print("Конфигурация ПК",self.cpu, self.ram)
#
#     def update(self):
#         self.cpu = 'i9'
#
# comp1 = Computer('i5',16)
# comp2 = Computer('Razer7',8)
#
# comp1.update()
#
# Computer.config(comp1)

# class car:
#     wheels = 4
#     def __init__(self):
#         self.mil = 10
#         self.com = 'BWM'
#
# c1 = car()
# c2 = car()
#
# print(c1.com, c1.mil)  # --> BWM 10
# print(c2.com, c2.mil)  # --> BWM 10
#
# print(c1.mil, c1.com, c1.wheels) # --> 10 BWM 4
# print(c2.mil, c2.com, c2.wheels) # --> 10 BWM 4


# class Student:
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     def avr(self):
#         return (self.m1+self.m2+self.m3)/3
#
#     def info(self):
#         print("Это класс студента: ")
#
# s1 = Student(34,67,100)
# s2 = Student(89,33,12)

# print(s1.avr())
# print(s2.avr())
# print(s1.info())

# class Student:
#     def __init__(self,name,rolno):
#         self.name = name
#         self.rolno = rolno
#     def show(self):
#         print(self.name, self.rolno)
#     class Laptop:
#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = 'i5'
#             self.ram = 8
#
#         def show(self):
#             print(self.brand, self.cpu,self.ram)

# s1 = Student("Sarvar",2)
# print(s1.name,s1.rolno) # --> Sarvar 2
# s1.show() # --> Sarvar 2

# lap1 = Student.Laptop()
# print(lap1.brand, lap1.cpu,lap1.ram) # --> HP i5 8
# lap1.show()

class A:
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")

a1 = A()
# a1.feature1() # --> Feature 1 working
# a1.feature2() # --> Feature 2 working

class B(A):
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")
b1 = B()

# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()

class C(B):
    def feature5(self):
        print("Feature 5 working")
    def feature6(self):
        print("Feature 6 working")

c1 = C()

# c1.feature1()
# c1.feature2()
# c1.feature3()
# c1.feature4()
# c1.feature5()
# c1.feature6()








