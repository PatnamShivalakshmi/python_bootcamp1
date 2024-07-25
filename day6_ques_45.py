#***multilevel inheritance****
class Animal:
    def Speak():
        return "animal is speaking"
    #single inheritance:
class Dog(Animal):
    def Bark():
        return "Bow..."
class puppy(Dog):
    def Bark():
        return "Bow......"   
obj1=Animal
obj2=Dog
obj3=puppy
print(obj1.Speak())
print(obj2.Bark())
print(obj3.Bark())
