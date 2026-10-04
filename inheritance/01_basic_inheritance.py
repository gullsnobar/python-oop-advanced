#  Inheritance allows a child class to reuse functionality from an existing class.

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()  # Dog inherits from Animal