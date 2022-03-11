#################
## ПРИМЕР: простой класс координат
#################
# class Coordinate(object):
#     """ Координата, состоящая из значений x и y """
#     def __init__(self, x, y):
#         """ Устанавливает значения x и y """
#         self.x = x
#         self.y = y
#     def __str__(self):
#         """ Возвращает строковое представление self """
#         return "<" + str(self.x) + "," + str(self.y) + ">"
#     def distance(self, other):
#         """ Возвращает евклидово расстояние между двумя точками """
#         x_diff_sq = (self.x-other.x)**2
#         y_diff_sq = (self.y-other.y)**2
#         return (x_diff_sq + y_diff_sq)**0.5
# c = Coordinate(3,4)
# origin = Coordinate(0,0)
# print(c.x, origin.x)
# print(c.distance(origin))
# print(Coordinate.distance(c, origin))
# print(origin.distance(c))
# print(c)