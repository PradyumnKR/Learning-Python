class vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class vector3d(vector2d):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
    def show(self):
        print(f"x : {self.x}i , y : {self.y}j , z : {self.z}k")

vec = vector3d(2,3,4)
vec.show()