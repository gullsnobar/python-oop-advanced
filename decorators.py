# Now we move from List Comprehensions → Decorators.

# 1. What problem do decorators solve?

# Suppose you already have a function:

def login():
    print("User logged in")

# Later, you want to add extra behavior:

# Log when the function runs
# Check authentication
# Measure execution time
# Check permissions

# You could modify every function, but that creates duplicate code.

# Decorator lets you add extra behavior to an existing function without changing its original code.



# Decorators are also called higher order function
# A function that takes another function, adds some behavior, and returns a new function.


# Think:

# Original Function
#        ↓
#    Decorator
#        ↓
# Function + Extra Behavior


# In python you can store a function in a variable

def say_hello():
    print("Hello")

my_function = say_hello

my_function()


# You can also pass a function to another function

def say_hello():
    print("Hello")

def execute(function):
    function()    

execute(say_hello)



# Create decorator


def my_decorator(function):

    def wrapper():
        print("Before Function")

        function()

        print("After function")

    return wrapper    




#  Apply decorator manually

def say_hello():
    print("Hello")


def my_decorator(function):

    def wrapper():
        print("Before function")

        function()

        print("After function")

    return wrapper


say_hello = my_decorator(say_hello)

say_hello()