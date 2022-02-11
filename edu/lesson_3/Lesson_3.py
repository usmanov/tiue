# # ---------------------------------------------------------------------# Variable

# height = 1.79
# weight = 68.7
# bmi = weight / height ** 2 # <- 68.7 / 1.79 ** 2
# print(bmi)

# #---------------------------------------------------------------------# Reproducibility
# height = 1.79
# weight = 74.2 # <-  simply change the declaration of the weight variable,
# bmi = weight / height ** 2
# print(bmi)

# #---------------------------------------------------------------------# Python Types
# type(bmi) # float
# day_of_week = 5
# type(day_of_week) # int

# x = "body mass index"
# y = 'this works too'
# type(y) #str

# z = True
# type(z) # bool

# # ---------------------------------------------------------------------# Python Data Types

# height = 1.73
# tall = True

# # ---------------------------------------------------------------------# Problem 

# height1 = 1.73
# height2 = 1.68
# height3 = 1.71
# height4 = 1.89

# # ---------------------------------------------------------------------# Python List

# [1.73, 1.68, 1.71, 1.89]

# fam = [1.73, 1.68, 1.71, 1.89]
# print(fam)

# fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
# fam2 = [["liz", 1.73],
#     ["emma", 1.68],
# 	["mom", 1.71],
# 	["dad", 1.89]]
# print(fam2)

# # ---------------------------------------------------------------------# List type

# type(fam)
# type(fam2)

# # ---------------------------------------------------------------------# Subsetting Lists

# fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
# print(fam) #['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]

# fam[3] # 1.68
# fam[6] # 'dad'
# fam[-1] # 1.89
# fam[7] # 1.89

# # ---------------------------------------------------------------------# List slicing
# ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
# fam[3:5] # [1.68, 'mom']
# fam[1:4] # [1.73, 'emma', 1.68]
# fam[:4] # ['liz', 1.73, 'emma', 1.68]
# fam[5:] # [1.71, 'dad', 1.89]

# # ---------------------------------------------------------------------# Manipulating Lists

# # ------------------------------# Changing list elements
# fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
# fam[7] = 1.86
# fam[0:2] = ["lisa", 1.74]

# print(fam) # ['lisa', 1.74, 'emma', 1.68, 'mom', 1.71, 'dad', 1.86]

# fam + ["me", 1.79] # ['lisa', 1.74,'emma', 1.68, 'mom', 1.71, 'dad', 1.86, 'me', 1.79]

# fam_ext = fam + ["me", 1.79] # ['lisa', 1.74,'emma', 1.68, 'mom', 1.71, 'dad', 1.86, 'me', 1.79]

# del(fam[2])

# print(fam) # ['lisa', 1.74, 1.68, 'mom', 1.71, 'dad', 1.86]

# # ---------------------------------------------------------------------# Behind the scenes (1)

# x = ["a", "b", "c"]
# y = x
# y[1] = "z"
# print(y) # ['a', 'z', 'c']
# print(x) # ['a', 'z', 'c']

# x = ["a", "b", "c"]
# y = list(x)
# y = x[:]

# # ---------------------------------------------------------------------# Functions
# fam = [1.73, 1.68, 1.71, 1.89]
# max(fam) # 1.89
# tallest = max(fam)

# round(1.68, 1) # 1.7

# round(1.68) # 2

# help(round) # Open up documentation

# # ---------------------------------------------------------------------# Built-in Functions
# sister = "liz"
# height = 1.73
# fam = ["liz", 1.73, "emma", 1.68,
#     "mom", 1.71, "dad", 1.89]

# # ---------------------------------------------------------------------# Back 2 Basics
# # ---------------------------------# list methods

# fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
# fam.index("mom") # "Call method index() on fam" --> 4

# fam.count(1.73) # --> 1

# print(sister) # --> 'liz'

# sister.capitalize() # --> 'Liz'

# sister.replace("z", "sa") # --> 'lisa'

# sister.replace("z", "sa") # --> 'lisa'

# fam.replace("mom", "mommy") # --> AttributeError: 'list' object has no attribute 'replace'

# sister.index("z") # --> 2

# fam.index("mom") # --> 4

# print(fam) # --> ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]

# fam.append("me") # --> 

# print(fam) # --> ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89, 'me']

# fam.append(1.79) # -->

# print(fam) # --> ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89, 'me', 1.79]

# type(fam) # --> list

# fam.index("dad") # --> 6

# #---------------------------------------------------------------------# Loops
# For loop travesing a list
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# # For loop iterating 6 times
# for i in range(6):
#   print(i)

#---------------------------------------------------------------------# Object Oriented Programming (OOP)

#---------------------------------# Creating a class
# class cl: # Creating class
#     def bark(): #  function inside class
#         print('bark') # --> 'bark'

#     def add_one(x):
#         return x+1

# d = cl # Assigning class object to variable 'd'
# # print(type(d))  # --> <class 'type'>

# # d.bark() # --> calling the function

# print(cl.add_one(5))

# from typing_extensions import Self


# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name

#     def get_age(self,age):
#         return self.age

#     def set_age(self,age):
#         self.age = age

# d = student('Sarvar',36)
# d.set_age(23)
# print(d.get_age(22))


# class Item:
#     pass # --> passing, creating any class without getting errors after 

# How to create an instance of a class
# item1 = Item()

# # Assign attributes:
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

# print(type(item1.name)) # --> str

# random_str = 'aaa'
# print(random_str.upper()) # how to do same with self made methods? the answer is with class

# class Item:
#     def calculate_total_price(self, x, y): # function inside class calls method
#         return x * y
#         pass

# # How to create an instance of a class
# item1 = Item()

# # # Assign attributes:
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# # item1.calculate_total_price() # --> TypeError: Item.calculate_total_price() takes 0 positional arguments but 1 was given
# print(item1.calculate_total_price(item1.price,item1.quantity))

# item2 = Item()
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3
# print(item2.calculate_total_price(item2.price,item2.quantity))


#---------------------------------# Creating __init__ function
# class Item:
#     def __init__(self,name):
#         # print("I have created")
#         print(f"An instance created: {name}")

# # How to create an instance of a class
# item1 = Item("Phone")

# # # Assign attributes:
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

# item2 = Item("Laptop")
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3

#---------------------------------# Creating __init__ function (2)
# class Item:
#     def __init__(self,name):
#         self.name = name # after writing it, we can delete <item1.name = "Phone"> and <item2.name = "Laptop">
#         print(f"An instance created: {name}")

# # How to create an instance of a class
# item1 = Item("Phone")

# # # Assign attributes:

# item1.price = 100
# item1.quantity = 5

# item2 = Item("Laptop")
# item2.price = 1000
# item2.quantity = 3

# #---------------------------------# Clases, Assigning attributes dynamically
# class Item:
#     def __init__(self,name):
#         self.name = name # after writing it, we can delete <item1.name = "Phone"> and <item2.name = "Laptop">
        

# # How to create an instance of a class
# item1 = Item("Phone")

# # # Assign attributes:

# item1.price = 100
# item1.quantity = 5

# item2 = Item("Laptop")
# item2.price = 1000
# item2.quantity = 3

# print(f"An instance created: {item1.name}")
# print(f"An instance created: {item2.name}")

# #---------------------------------# Clases, Assigning <price> and <quantity> attributes dynamically
# class Item:
#     def __init__(self,name,price, quantity):
#         self.name = name # after writing it, we can delete <item1.name = "Phone"> and <item2.name = "Laptop">
#         self.price = price
#         self.quantity = quantity

# # How to create an instance of a class
# item1 = Item("Phone",100,5) # adding atributes 

# item2 = Item("Laptop",1000,3) # adding atributes 

# print(f"For the first item {item1.name}, the price is {item1.price} with the quantity of {item1.quantity}") # assigning to the atributes of item 1 dynamically
# print(f"For the second item {item2.name}, the price is {item2.price} with the quantity of {item2.quantity}") # assigning to the atributes of item 1 dynamically

#---------------------------------#  Clases, Assigning default value to <price> and <quantity>
# class Item:
#     def __init__(self,name,price, quantity=1):
#         self.name = name # after writing it, we can delete <item1.name = "Phone"> and <item2.name = "Laptop">
#         self.price = price
#         self.quantity = quantity

# # How to create an instance of a class
# item1 = Item("Phone",100) # adding atributes 

# item2 = Item("Laptop",1000) # adding atributes 

# print(f"For the first item {item1.name}, the price is {item1.price} with the quantity of {item1.quantity}") # assigning to the atributes of item 1 dynamically
# print(f"For the second item {item2.name}, the price is {item2.price} with the quantity of {item2.quantity}") # assigning to the atributes of item 1 dynamically



#---------------------------------#  Clases, Calculating price of item
# class Item:
#     def __init__(self,name,price, quantity):
#         self.name = name 
#         self.price = price
#         self.quantity = quantity
#     def calculate_total_price(self): # function inside class calls method
#         return self.price * self.quantity

# item1 = Item("Phone",100,5) # adding atributes 
# item2 = Item("Laptop",1000,3) # adding atributes 

# print(f"The price of item {item1.name} is {item1.calculate_total_price()}")
# print(f"The price of item {item2.name} is {item2.calculate_total_price()}")

#---------------------------------# Putting type expectation (restriction)
# class Item:
    # def __init__(self,name: str,price: float, quantity=0): #                                                          <--<
#         self.name = name 
#         self.price = price
#         self.quantity = quantity
#     def calculate_total_price(self): # function inside class calls method
#         return self.price * self.quantity

# item1 = Item(1,100,5) # adding atributes 
# item2 = Item("Laptop",1000,3) # adding atributes 

# print(f"The price of item {item1.name} is {item1.calculate_total_price()}")
# print(f"The price of item {item2.name} is {item2.calculate_total_price()}")

#---------------------------------# Run validations to the received arguments
# class Item:
#     def __init__(self,name: str,price: float, quantity=0):
#                                                                                       # Run validations to the received arguments
#         assert price >= 0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        
#         # Assign to self object
#         self.name = name 
#         self.price = price
#         self.quantity = quantity
#     def calculate_total_price(self): # function inside class calls method
#         return self.price * self.quantity

# item1 = Item(1,100,5) # adding atributes 
# item2 = Item("Laptop",1000,3) # adding atributes 

# print(f"The price of item {item1.name} is {item1.calculate_total_price()}")
# print(f"The price of item {item2.name} is {item2.calculate_total_price()}")

#---------------------------------# Applying discount method
# class Item:
#     pay_rate = 0.8                                                          # adding local for the class variable
#     def __init__(self,name: str,price: float, quantity=0):
        
#         # Assign to self object
#         self.name = name 
#         self.price = price
#         self.quantity = quantity
#     def calculate_total_price(self): # function inside class calls method
#         return self.price * self.quantity

#     def apply_discount (self):                                              #Creating discount method
#         self.price = self.price * Item.pay_rate

# item1 = Item(1,100,5) # adding atributes 
# # item2 = Item("Laptop",1000,3) # adding atributes 
# item1.apply_discount()
# print(item1.price)

# # print(Item.pay_rate)                                                          # accessing class atribute (class level)
# # print(item1.pay_rate)                                                           # accessing class variable thought instanse

#---------------------------------# Applying different discount method to utem2 instance
# class Item:
#     pay_rate = 0.8                                                          # adding local for the class variable
#     def __init__(self,name: str,price: float, quantity=0):
        
#         # Assign to self object
#         self.name = name 
#         self.price = price
#         self.quantity = quantity
#     def calculate_total_price(self): # function inside class calls method
#         return self.price * self.quantity

#     def apply_discount (self):                                              #Creating discount method
#         # self.price = self.price * Item.pay_rate                             # we are getting same discount because of this 
#         self.price = self.price * self.pay_rate                                 # after changing this line everything works ok

# item1 = Item(1,100,5) # adding atributes 
# item1.apply_discount()
# print(item1.price)

# item2 = Item("Laptop",1000,3) # adding atributes                            
# item2.pay_rate = 0.7                                                          # # Applying different discount method to utem2 instance 
# item2.apply_discount()
# print(item2.price)

#---------------------------------# Creating instances in a list
# class Item:
#     all = []                                                                # creating list for all instances
#     pay_rate = 0.8                                                          
#     def __init__(self,name: str,price: float, quantity=0):
        
#         # Assign to self object
#         self.name = name 
#         self.price = price
#         self.quantity = quantity

#         Item.all.append(self)                                               # Adding all instanses to the list <all>

#     def calculate_total_price(self): # function inside class calls method
#         return self.price * self.quantity

#     def apply_discount (self):                                              #Creating discount method
#         # self.price = self.price * Item.pay_rate                             # we are getting same discount because of this 
#         self.price = self.price * self.pay_rate                                 # after changing this line everything works ok
#                                                                             # Adding new instances 
#     def __repr__(self):
#         return f"Item('{self.name}', {self.price}, {self.quantity})"        #Outputing elelments in the list of instances 
    
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)

#---------------------------------# Creating instances in a CSV file
import csv                                                                  # in order to use csv file we need to import csv library 
class Item:
    all = []                                                                # creating list for all instances
    pay_rate = 0.8                                                          
    def __init__(self,name: str,price: float, quantity=0):
        
        # Assign to self object
        self.name = name 
        self.price = price
        self.quantity = quantity

        Item.all.append(self)                                               # Adding all instanses to the list <all>

    def calculate_total_price(self): # function inside class calls method
        return self.price * self.quantity

    def apply_discount (self):                                              #Creating discount method
        # self.price = self.price * Item.pay_rate                             # we are getting same discount because of this 
        self.price = self.price * self.pay_rate                                 # after changing this line everything works ok
                                                                            # Adding new instances 
    @classmethod
    def instantiate_form_csv(cls):                              #creating methos to open and read from csv file
        with open('items.csv', 'r') as f:                           # openning csv file with read mode and saving data to the <f> file
            reader = csv.DictReader(f)                                  # openning csv file in dictionary 
            items = list(reader) 

    # DEMOSTRATION OF LIST CONTENT 
        for item in items:
            print(item)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"        #Outputing elelments in the list of instances 
    
Item.instantiate_form_csv()



print(Item.all)
