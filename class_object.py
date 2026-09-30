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