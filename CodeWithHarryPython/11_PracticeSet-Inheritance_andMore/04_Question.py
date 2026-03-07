class Complex:
    def __init__(self, i, j):
        self.i = i # Real part
        self.j = j # Imaginary part

    def __add__(self, other):
        return Complex(self.i + other.i, self.j + other.j)

    def __mul__(self, other):
        # Using the formula: (ac - bd) + (ad + bc)i
        real_part = (self.i * other.i) - (self.j * other.j)
        imag_part = (self.i * other.j) + (self.j * other.i)
        return Complex(real_part, imag_part)

    # Adding a __str__ method (Question 6 in your set!)
    def __str__(self):
        return f"{self.i} + {self.j}i"

c1 = Complex(3, 4)
c2 = Complex(5, 2)

print(f"Addition: {c1 + c2}")
print(f"Multiplication: {c1 * c2}")