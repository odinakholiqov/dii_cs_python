"""
OOP: object oriented programming
    object
        properties / characteristics
        behaviors / methods

    
"""

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self.__age = new_age


odina = Employee('Odina', 30)
odina.age
print(odina.name)

print(odina.age)


