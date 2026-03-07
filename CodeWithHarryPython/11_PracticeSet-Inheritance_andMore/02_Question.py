class Animal:
    pass
class Pets(Animal):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("Woof!")

doggy = Dog()
doggy.bark()