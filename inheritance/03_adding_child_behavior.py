# Inheritence is not only about reusing things.

# A child can also add its own behavior.

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

dog = Dog()

dog.eat()
dog.bark()
