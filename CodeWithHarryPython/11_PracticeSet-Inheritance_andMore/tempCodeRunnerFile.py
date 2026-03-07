# class Vector :
#     def __init__(self,l):
#         self.vec = l
#     def __add__(self,other):
#         new_list = [x + y for x, y in zip(self.vec, other.vec)]
#         return Vector(new_list)
#     def __mul__(self, other):
#         new_list = [x*y for x,y in zip(self.vec,other.vec)]
#         return sum(new_list)
#     def __str__(self):