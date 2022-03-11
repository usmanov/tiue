import random

#################################
## Абстрактный тип данных Cущества
#################################
# class Creature (object):
#     def __init__(self, age):
#         self.age = age
#         self.name = None
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
#     def set_age(self, newage):
#         self.age = newage
#     def set_name(self, newname=""):
#         self.name = newname
#     def __str__(self):
#         return "существо:"+str(self.name)+":"+str(self.age)
#
# print("\n---- тестирование класса существ ----")
# a = Creature(4)
# print(a)
# print(a.get_age())
# a.set_name("пушистый")
# print(a)
# a.set_name()
# print(a)

#
#
# #################################
# ## Пример наследования
# #################################
# class Cat(Creature):
#     def speak(self):
#         print("мяу")
#     def __str__(self):
#         return "cat:"+str(self.name)+":"+str(self.age)

# print("\n---- тест класса кошка ----")
# c = Cat(5)
# c.set_name("пушистый")
# print(c)
# c.speak()
# print(c.get_age())
# a.speak() # ошибка из-за отсутствия метода speak для класса Creature


# #################################
# ## Пример наследования
# #################################
# class Person(Creature):
#     def __init__(self, name, age):
#         Creature.__init__(self, age)
#         self.set_name(name)
#         self.friends = []
#     def get_friends(self):
#         return self.friends
#     def speak(self):
#         print("Привет")
#     def add_friend(self, fname):
#         if fname not in self.friends:
#             self.friends.append(fname)
#     def age_diff(self, other):
#         diff = self.age - other.age
#         print(abs(diff), "разница в годах")
#     def __str__(self):
#         return "человек:"+str(self.name)+":"+str(self.age)
# #
# print("\n---- тест человека ----")
# p1 = Person("Сарвар", 30)
# p2 = Person("Усман", 25)
# print(p1.get_name())
# print(p1.get_age())
# print(p2.get_name())
# print(p2.get_age())
# print(p1)
# p1.speak()
# p1.age_diff(p2)
#
#
# #################################
# ## Пример наследования
# #################################
# class Student(Person):
#     def __init__(self, name, age, major=None):
#         Person.__init__(self, name, age)
#         self.major = major
#     def __str__(self):
#         return "Студент:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
#     def change_major(self, major):
#         self.major = major
#     def speak(self):
#         r = random.random()
#         if r < 0.25:
#             print("у меня есть домашнее задание")
#         elif 0.25 <= r < 0.5:
#             print("мне нужно поспать")
#         elif 0.5 <= r < 0.75:
#             print("я должен поесть")
#         else:
#             print("я смотрю телевизор")
# # #
# print("\n---- тест студента ----")
# s1 = Student('Сарвар', 20, "разработка программного обеспечения")
# s2 = Student('Усман', 18)
# print(s1)
# print(s2)
# print(s1.get_name(),"говорит:", end=" ")
# s1.speak()
# print(s2.get_name(),"говорит:", end=" ")
# s2.speak()
#
#
#
# #################################
# ## Использование переменных класса
# #################################
# class Rabbit(Creature):
    # переменная класса, тег, общий для всех экземпляров
    # tag = 1
    # def __init__(self, age, parent1=None, parent2=None):
    #     Creature.__init__(self, age)
    #     self.parent1 = parent1
    #     self.parent2 = parent2
    #     self.rid = Rabbit.tag
    #     Rabbit.tag += 1
    # def get_rid(self):
        # zfill используется для добавления начальных нулей 001 вместо 1
    #     return str(self.rid).zfill(3)
    # def get_parent1(self):
    #     return self.parent1
    # def get_parent2(self):
    #     return self.parent2
    # def __add__(self, other):
        # возвращающий объект того же типа, что и этот класс
    #     return Rabbit(0, self, other)
    # def __eq__(self, other):
        # сравните идентификаторы своих и чужих родителей
        # не волнуйтесь о порядке родителей
        # обратная косая черта сообщает python, что я хочу разбить свою строку
    #     parents_same = self.parent1.rid == other.parent1.rid \
    #                    and self.parent2.rid == other.parent2.rid
    #     parents_opposite = self.parent2.rid == other.parent1.rid \
    #                        and self.parent1.rid == other.parent2.rid
    #     return parents_same or parents_opposite
    # def __str__(self):
    #     return "Кролик:"+ self.get_rid()

# print("\n---- Тест Кролика ----")
# print("---- тестирование создания кроликов ----")
# r1 = Rabbit(3)
# r2 = Rabbit(4)
# r3 = Rabbit(5)
# print("r1:", r1)
# print("r2:", r2)
# print("r3:", r3)
# print("r1 parent1:", r1.get_parent1())
# print("r1 parent2:", r1.get_parent2())
#
# print("---- тестирование добавления кролика ----")
# r4 = r1+r2   # r1.__add__(r2)
# print("r1:", r1)
# print("r2:", r2)
# print("r4:", r4)
# print("r4 parent1:", r4.get_parent1())
# print("r4 parent2:", r4.get_parent2())
#
# print("---- проверка равенства кроликов ----")
# r5 = r3+r4
# r6 = r4+r3
# print("r3:", r3)
# print("r4:", r4)
# print("r5:", r5)
# print("r6:", r6)
# print("r5 parent1:", r5.get_parent1())
# print("r5 parent2:", r5.get_parent2())
# print("r6 parent1:", r6.get_parent1())
# print("r6 parent2:", r6.get_parent2())
# print("r5 and r6 have same parents?", r5 == r6)
# print("r4 and r6 have same parents?", r4 == r6)
