# Now comes one of the most important parts of inheritance.

# Suppose the parent says:

class Animal:
    def make_sounds(self):
        print("Animal makes a sound")


# But a dog should make its own sound.

# We can redefine the method:

class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def make_sound(self):
        print("Dog says: Woof!")

animal = Animal()
dog = Dog()

animal.make_sound()
dog.make_sound()


# This is called method overriding.

# The child replaces the inherited implementation with its own implementation.

# Parent
#   │
#   └── make_sound()
#           ↓
#         Child
#           │
#           └── make_sound()
#               ↑
#           overrides it
