# class Computer:
    #stuff can be only Atributes (variables) and Behaviour (Methods)
    #what every has?

#     def __init__(self,cpu,ram):
#         # print("in init")
#         # pass
#         self.cpu = cpu
#         self.ram = ram

#     def config (self):
#         print("Configuration is:",self.cpu, self.ram)

# comp1 = Computer('i5',16)
# comp2 = Computer('Razer 3',8)

# a = "Hello"
# print(type(a))      # --> <class 'str'>
# print(type(comp))  # --> <class '__main__.Computer'>

# When you want to use a method you need to call first the class name of the class which consist of the method
# what will happen if we run this command ?
# Computer.config(comp1) # --> i5, 16gb, 1TB
# # Computer.config() # -->  Computer.config() missing 1 required positional argument: 'self
# Computer.config(comp2)

# ----------------------------------------------------------------------------------------------------------------------------
# Computer.config() # -->  Computer.config() missing 1 required positional argument: 'self

# comp1.config() #in this case you are using the object itself to call the function
# comp2.config() # so in most of the codes you will see this type of syntax 

# x = 0b100101              # Example
# print(x.bit_length())
    
# class Computer:
#     def __init__(self) -> None:
#         self.name = "Sarvar"
#         self.age = 39

#     def update(self):
#         self.age = 30
    
#     def compare(self,other): # compare (who is calling it, whom to compare)
#         print(self.age)     # --> 39
#         print(other.age)    # --> 23

# c1 = Computer()
# c2 = Computer()

# # print(c1.name) # --> Sarvar
# # print(c2.name) # --> Sarvar 

# # c1.name = 'Mirza'
# # print(c1.name) # --> Mirza

# # c1.update()
# # print(c1.age) # --> Mirza 
# c2.age = 23
# c1.compare(c2)

# ----------------------------------------------------------------------------------------------------------------------------

# class car:
#     wheels = 4              # class variable
#     def __init__(self) -> None:
#         self.mil = 10       # instance variable
#         self.com = 'BWM'    # instance variable
        

# c1 = car()
# c2 = car()
# # print(c1.com, c1.mil)  # --> BWM 10
# # print(c2.com, c2.mil)  # --> BWM 10

# c1.mil = 20
# # print(c1.com, c1.mil)  # --> BWM 20
# # print(c2.com, c2.mil)  # --> BWM 10

# # print(c1.com, c1.mil,c1.wheels)  # --> BWM 20 4
# print(c2.com, c2.mil,c2.wheels)  # --> BWM 10 4

# ----------------------------------------------------------------------------------------------------------------------------

# class Student:

#     def __init__(self,m1,m2,m3) -> None:
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def avr(self):
#         return (self.m1+self.m2+self.m3)/3

# s1 = Student(34,67,32)
# s2 = Student(89,33,12)

# print(s1.avr())

# ----------------------------------------------------------------------------------------------------------------------------
# class Student:
#     school = 'TIUE'

#     @classmethod
#     def info(cls):
#         return cls.school

# s1 = Student()

# print(Student.info())

# ----------------------------------------------------------------------------------------------------------------------------

# class Student:
#     school = "TIUE"

#     def info(): # instatnt variable
#         print("This is the class")

# Student.info()

# ----------------------------------------------------------------------------------------------------------------------------

# class Student:
#     def __init__(self,name,rolno) -> None:
#         self.name = name
#         self.rolno = rolno 
#     def show(self):
#         print(self.name, self.rolno)
    
#     class Laptop:

#         def __init__(self) -> None:
#             self.brand = 'HP'
#             self.cpu = 'i5'
#             self.ram = 8


# s1 = Student("Sarvar",2)

# print(s1.name,s1.rolno)  # inconvinient
# s1.show() # --> sarvar 2

# lap1 = Student.Laptop()
# print(lap1.brand,lap1.cpu,lap1.ram)

# ----------------------------------------------------------------------------------------------------------------------------

# class Student:
#     def __init__(self,name,rolno) -> None:
#         self.name = name
#         self.rolno = rolno
#         self.lap = self.Laptop()

#     def show(self):
#         print(self.name, self.rolno)
#         self.lap.show()

#     class Laptop:

#         def __init__(self) -> None:
#             self.brand = 'HP'
#             self.cpu = 'i5'
#             self.ram = 8
        

#         def show (self):
#             print(self.brand, self.cpu, self.ram)

# s1 = Student("Sarvar",2)

# # print(s1.name,s1.rolno)  # inconvinient
# s1.show() # --> sarvar 2

# # lap1 = Student.Laptop()
# # print(lap1.brand,lap1.cpu,lap1.ram)

# --------------------------------------------------------INharitance--------------------------------------------------------------------

# class A:
#     def feature1(self):
#         print("feature 1 working")

#     def feature2(self):
#         print("feature 2 working")

# a1 = A()

# a1.feature1()
# a1.feature2()

# class B(A):                         # A is a Super or Parent class, B is sub or child class 
#     def feature3(self):
#         print("feature 3 working")

#     def feature4(self):
#         print("feature 4 working")

# b1 = B()

# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()

# class C(B):
#     def feature5(self):
#         print("feature 5 working")

# c1 = C()

# c1.feature1()
# c1.feature5()

# --------------------------------------------------------INharitance (2)--------------------------------------------------------------------

# class A:
#     def feature1(self):
#         print("feature 1 working")

#     def feature2(self):
#         print("feature 2 working")

# a1 = A()

# # a1.feature1()
# # a1.feature2()

# class B:                         
#     def feature3(self):
#         print("feature 3 working")

#     def feature4(self):
#         print("feature 4 working")

# b1 = B()

# # b1.feature3()
# # b1.feature4()

# class C(A,B):                                 # A and B is a Super or Parent classes, C is sub or child class 
#     def feature5(self):
#         print("feature 5 working")

# c1 = C()

# c1.feature1()
# c1.feature5()

# --------------------------------------------------------INharitance (3)--------------------------------------------------------------------

# class A:

#     def __init__(self) -> None:
#         print("inside A init")

# class B(A):  
#     pass


# # a1 = A()
# # a1            # --> inside A init

# a1 = B()
# a1              # --> inside B init
# --------------------------------------------------------INharitance (3)--------------------------------------------------------------------

# class A:

#     def __init__(self) -> None:
#         print("inside A init")

# class B(A):  

#     def __init__(self) -> None:
#         print("inside B  init")


# # a1 = A()
# # a1            # --> inside A init

# a1 = B()
# a1              # --> inside B init

# # --------------------------------------------------------INharitance (4) super --------------------------------------------------------------------

# class A:

#     def __init__(self):
#         print("inside A init")

# class B(A):  

#     def __init__(self):
#         super().__init__()              #  you can access all the features of the parent class
#         print("inside B  init")


# # a1 = A()
# # a1            # --> inside A init

# a1 = B()
# a1              # --> inside A init inside B init

# --------------------------------------------------------INharitance (4) super --------------------------------------------------------------------

# class A:

#     def __init__(self):
#         print("inside A init")

# class B:  

#     def __init__(self):
#         super().__init__()              #  you can access all the features of the parent class
#         print("inside B  init")

# class C(A,B):

#     def __init__(self):
#         super().__init__()
#         # print("Inside C init")
# a1 = C()
# a1              # --> inside A init inside B init

# --------------------------------------------------------INharitance (6) --------------------------------------------------------------------

# class A:

#     def __init__(self):
#         print("inside A init")
#     def feature1(self):
#         print("feature 1-A working")

# class B:  

#     def __init__(self):
#         super().__init__()              #  you can access all the features of the parent class
#         print("inside B  init")
    
#     def feature1(self):
#         print("feature 1-B working")

# class C(A,B):

#     def __init__(self):
#         super().__init__()
#         # print("Inside C init")
# a1 = C()
# a1.feature1()              # --> feature 1-A working

# --------------------------------------------------------INharitance (7) super --------------------------------------------------------------------

# class A:

#     def __init__(self):
#         print("inside A init")
#     def feature1(self):
#         print("feature 1-A working")

# class B:  

#     def __init__(self):
#         super().__init__()              #  you can access all the features of the parent class
#         print("inside B  init")
    
#     def feature2(self):
#         print("feature 1-B working")

# class C(A,B):

#     def __init__(self):
#         super().__init__()
#         # print("Inside C init")
    
#     def feat(self):
#         super().feature2()
# a1 = C()
# a1.feat()                       # --> feature 1-B working     

# -------------------------------------------------------- Polymorphisim --------------------------------------------------------------------
# Duck typing
# Operator overloding
# Method Overloading
# Method Overridding

# # -------------------------------------------------------- Duck typing --------------------------------------------------------------------
# class VSC:

#     def execute(self):
#         print("Compiling")
#         print("Running")
# class Laptop:

#     def code(self, ide):
#         ide.execute()
    
# ide = VSC()

# lap1 = Laptop()
# lap1.code(ide)

# -------------------------------------------------------- Duck typing (2) --------------------------------------------------------------------
# class VSC:

#     def execute(self):
#         print("Compiling")
#         print("Running")

# class MyIDE:
#     def execute(self):
#         print("Spell check")
#         print("Compiling")
#         print("Running")

# class Laptop:

#     def code(self, ide):
#         ide.execute()
    
# ide = MyIDE()

# lap1 = Laptop()
# lap1.code(ide)

# -------------------------------------------------------- Operator overloding --------------------------------------------------------------------
# a = 4
# b = 2

# print(a+b)
# print(int.__add__(a,b))

# a = '4'
# b = '2'

# print(a+b)
# print(str.__add__(a,b)) # that moment you add a plus operator it calls the __add__ method the moment you put a minus operator it will call a __sub__
                        # method the moment you use a star simple which is multiplication it will call __mult__ method so we have different methods

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
    
#     def __add__(self,other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1,m2)

#         return s3
    
#     def __str__(self):
#         return self.m1, self.m2


# s1 = Student(58,69)
# s2 = Student(60,65)

# s3 = s1 + s2
# print(s3)               # actually we ar using __str__ method <__main__.Student object at 0x109067610>
# print(s1.__str__())       # --> <__main__.Student object at 0x109067610>

# -------------------------------------------------------- Operator overloding (1) --------------------------------------------------------------------

# class Student:

#     def __init__(self):
#         pass

#     def sum(self,a,b):
#         s = a+b
#         return s

# s1 = Student()

# print(s1.sum(4,5))

# -------------------------------------------------------- Operator overloding (2) --------------------------------------------------------------------

# class Student:

#     def __init__(self):
#         pass

#     def sum(self,a=None,b=None,c=None):
#         s = 0
#         if a!=None and b!=None and c!=None:
#             s = a+b+c
#         elif a!=None and b!=None:
#             s = a+b
#         else:
#             s = a
#         return s

# s1 = Student()

# print(s1.sum(4))

# -------------------------------------------------------- Operator overidding --------------------------------------------------------------------

# class A:
#     def show(self):
#         print("in A show")

# class B:
#     pass

# a1 = A()
# a1.show() # --> in A show

# a1 = B()
# a1.show()  # --> AttributeError: 'B' object has no attribute 'show'

# class A:
#     def show(self):
#         print("in A show")
# class B(A):
#     pass

# a1 = B()
# a1.show() # --> in A show
#
# class A:
#     def show(self):
#         print("in A show")
# class B:
#     def show(self):
#         print("in B show")
#
# a1 = B()
# a1.show() # --> in B show
