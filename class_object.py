#    What is class?

# Think of a class as a blueprint.

# For Example

    #           User class
    #               │
    #     ┌─────────┴─────────┐
    #     │                   │
    #   data               behavior
    #     │                   │
    #  name                 login()
    #  email                logout()
    #  age                  update()


#     What is an object?

# An object is an actual instance created from a class.
# You can create many objects from the same class:


# Class vs Object

# This distinction is very important.

# Think about a car factory.

# Car design
#     ↓
# CLASS

# Actual cars
#     ↓
# OBJECTS



# Similarly:

# class User:
#pass

# is the blueprint.

# And:

# user1 = User()
# user2 = User()

# are actual objects.

# So:

# Class = definition/blueprint
# Object = actual instance of that class


class User:
    pass

user1 = User()

user1.name = "Gull"
user1.email = "gullsnobar9098@gmail.com"

print(user1.name)
print(user1.email)

# __init__() very imp

# __init__() allows us to initialize an object when it is created.


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

 # self refers to the current object.
 # self is not a python keyword.
 # self ia a convention.


 # Attributes is the data associated with an object.

class User:

 def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age       

user = User(
    "Gul",
    "gull@gmail.com",
    34
)

print(user.name)
print(user.email)
print(user.age)


#   Methods
## A method is function inside a class is generally called a method.

class User:

    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, {self.name}") 

# create an object

user = User("Gull")
user.greet()


# Methods can modify the objects

class User:
    def __init__(self, name):
        self.name = name
    def change_name(self, new_name):
        self.name = new_name

user = User("Gull")

print(user.name)

user.change_name("Gull Khan")

print(user.name)


# Object = Data + Behavior