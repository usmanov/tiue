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

