# class Computer(object):
#     # Атрибуты
#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram
#
#     def config(self):
#         print("Конфигурация ПК:",self.cpu,self.ram)
#
#     def update(self):
#         self.ram = 32
#
#     def update_from_key(self,new_ram):
#         self.ram = new_ram
#
# comp1 = Computer('i5',16)
# comp2 = Computer('Razer 3',8)
#
# comp1.config()  # --> Конфигурация ПК: i5 16
#
# comp1.update()
# comp1.config()  # --> Конфигурация ПК: i5 32
#
# comp1.update_from_key(4)
# comp1.config() # --> Конфигурация ПК: i5 4

# class car:
#     wheels = 4
#     def __init__(self):
#         self.mil = 100
#         self.com = "BMW"
#
# c1 = car()
# c2 = car()

# print(c1.com, c1.mil) #--> BMW 100
# print(c2.com, c2.mil) #--> BMW 100

# print(c2.com, c2.mil, c2.wheels) #--> BMW 100

# class Student:
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#     def avr(self):
#         return (self.m1+self.m2+self.m3)/3
#
#     def info(self):
#         print("Это студент класса: ")

# s1 = Student(34,67,100)
# s2 = Student(56,9,87)
# print(s1.avr()) # self = s1
# print(s2.avr())
# print(s1.info())
# s1.info()

# class Student:
#     def __init__(self,name,rolno):
#         self.name = name
#         self.rolno = rolno
#
#     def show(self):
#         print("Этот студент:",self.name,self.rolno)
#
#     class Laptop:
#         def __init__(self,brand,cpu, ram):
#             self.brand = brand
#             self.cpu = cpu
#             self.ram = ram
#         def show(self):
#             print("Этот ПК",self.brand,self.cpu, self.ram)
#
# s1 = Student("Sarvar",2)
# # print(s1.name,s1.rolno)
# # s1.show()
#
# lap1 = Student.Laptop("HP",'i5',8)
# # lap1.show()
# print(lap1.cpu)  # i5

# class A:
#     def feature1(self):
#         print("Это 1 работает")
#     def feature2(self):
#         print("Это 2 работает")
#
# a1 = A()

# print(a1) # --> 0x10dd4ee00
# print(a2) # --> 0x10dd4ddb0
# a1.feature1()
# a1.feature2()

# class B(A):
#     def feature3(self):
#         print("Это 3 работает")
#     def feature4(self):
#         print("Это 4 работает")
# b1 = B()

# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()

# class C(B):
#     def feature5(self):
#         print("Это 5 работает")
#     def feature6(self):
#         print("Это 6 работает")
#
# c1 = C()

# c1.feature1()
# c1.feature6()

# b1 = A()
# b1.feature3() #AttributeError: 'A' object has no attribute 'feature3'. Did you mean: 'feature1'?

# class A:
#     def __init__(self):
#         print("Внутри класса А")
#
# class B:
#     def __init__(self):
#         super().__init__()
#         print("Внутри класса B")
#
# class C(B,A):
#     def __init__(self):
#         super().__init__()
#         print("Внутри класса C")
#
# a1 = C()

















