SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
def to_subscript(text):
    return text.translate(SUB)

# print("e" + to_subscript("1") + "")  # Output: H₂O   

class Vector :
    def __init__(self,l):
        self.vec = l
    def __add__(self,other):
        new_list = [x + y for x, y in zip(self.vec, other.vec)]
        return Vector(new_list)
    def __mul__(self, other):
        new_list = [x*y for x,y in zip(self.vec,other.vec)]
        return sum(new_list)
    def __str__(self):
        # result = ""
        if len(self.vec) == 3:
            return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
        
        # Build the string for n-dimensions
        parts = []
        for index, value in enumerate(self.vec, start=1):
            parts.append(f"{value}e{to_subscript(str(index))}")
        
        return " + ".join(parts) # This joins all parts with a " + "
    def __len__(self):
        return len(self.vec)

v1 = Vector([3,4,5,4,6,7,7])
v2 = Vector([1,2,3,8,3,2,5])
v3 = v1 + v2
print(v3)
print(v1*v2)
print(len(v1))
        


        
