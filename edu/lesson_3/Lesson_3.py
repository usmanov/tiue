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

# fam = ['liz',0,'jahn',67,'micke',34]
# name = 'usmanov', 'sarvar'
# name = 'usmanov sarvar'


# print(len(fam)) #-->  6
# print(len(name)) #--> 2
