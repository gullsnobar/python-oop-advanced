
# ============================================================
# PYTHON OOP: CLASSES AND OBJECTS
# ============================================================


# ============================================================
# 1. WHAT IS A CLASS?
# ============================================================

# A class is a blueprint or definition used to create objects.
#
# For example, an application may have many users:
#
# User 1:
# name: Gull
# email: gullsnobar09@gmail.com
#
# User 2:
# name: Ali Ijaz
# email: aliijaz67@gmail.com
#
# Instead of defining each user separately, we define
# a User class once.


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


# ============================================================
# 2. WHAT IS AN OBJECT?
# ============================================================

# If a class is the blueprint, an object is the actual
# instance created from that class.
#
# Example:
#
# User = class / blueprint
# user1 = object / instance


user1 = User("Gull", "gullsnobar09@gmail.com")
user2 = User("Ali Ijaz", "aliijaz67@gmail.com")

print(user1.name)
print(user2.name)


# ============================================================
# 3. WHAT IS AN INSTANCE?
# ============================================================

# An instance is an object that belongs to a particular class.
#
# Here:
#
# user1 is an instance of the User class.
# user2 is an instance of the User class.


print(isinstance(user1, User))
print(isinstance(user2, User))


# Output:
# True
# True


# ============================================================
# 4. WHY DO WE USE __init__()?
# ============================================================

# __init__() is used to initialize an object with starting data.
#
# When we create:
#
# User("Gull", "gull@example.com")
#
# Python automatically calls __init__().


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


customer = Customer("Gull", "gull@example.com")

print(customer.name)
print(customer.email)


# ============================================================
# 5. WHAT DOES self MEAN?
# ============================================================

# self refers to the current object.
#
# For example, when we create:
#
# user1 = User("Gull")
#
# self refers to user1.
#
# When we create:
#
# user2 = User("Ali")
#
# self refers to user2.


class Member:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")


user1 = Member("Gull")
user2 = Member("Ali")

user1.greet()
user2.greet()


# Output:
# Hello Gull
# Hello Ali


# ============================================================
# 6. WHAT IS AN ATTRIBUTE?
# ============================================================

# An attribute is data associated with an object or class.
#
# In this example:
#
# self.name
# self.email
#
# are instance attributes.


class Account:
    def __init__(self, name, email):
        self.name = name
        self.email = email


account = Account("Gull", "gull@example.com")

print(account.name)
print(account.email)


# ============================================================
# 7. WHAT IS A METHOD?
# ============================================================

# A method is a function defined inside a class.
#
# Methods usually represent the behavior of an object.
#
# In this example:
#
# greet()
#
# is a method of the User class.


class Profile:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")


profile = Profile("Gull")

profile.greet()


# ============================================================
# 8. PRACTICAL EXAMPLE
# ============================================================

# A more practical example combining:
#
# - Class
# - Object
# - Instance
# - __init__()
# - self
# - Attributes
# - Methods


class AppUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.is_logged_in = False

    def login(self):
        self.is_logged_in = True
        print(f"{self.name} logged in.")

    def logout(self):
        self.is_logged_in = False
        print(f"{self.name} logged out.")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Logged in: {self.is_logged_in}")


# Create an object / instance

user = AppUser(
    "Gull",
    "gull@example.com"
)


# Display initial state

user.display_info()


# Login

user.login()


# Display updated state

user.display_info()


# Logout

user.logout()


# Display final state

user.display_info()

