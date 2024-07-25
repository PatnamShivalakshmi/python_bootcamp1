#*****multiple inheritance******
class Father:
    def father_speak():
        return "Father Class"
class Mother:
    def mother_speak():
        return "Mother Class"
class kid(Father,Mother):
    def kid_speak():
        return "I am kid.I am having properties of mother and father"
obj1=kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())
