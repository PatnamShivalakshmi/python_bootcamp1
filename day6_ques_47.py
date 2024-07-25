#polymorphism: method over riding 
class Animal:
    def Speak():
        return "Speaking...."
class Tiger:
    def Speak():
        return "Tiger is speaking"
class Cub:
    def Speak():
        return "cub is speaking"
obj2=Tiger
print(obj2.Speak())