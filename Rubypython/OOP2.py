# Create a class called Person
#3 attributes name, age, gender
#constructor method and object
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
        print(f"My name is {self.name} and my age is {self.age} and my gender is {self.gender}")

Obj1 = Person("Jack", 29, "Male")
Obj2= Person("Angel", 35, "Female")
obj3= Person("Rian", 39, "Male")
Obj1.display()
Obj2.display()
Obj3.display()


