#  Now imagine the child wants to use the parent's implementation and then add something extra.

class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def make_sound(self):
        super().make_sound()
        print("Dog says: Woof!")

dog = Dog()
dog.make_sound()