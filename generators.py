# What problem do generators solve?

# Imagine you need numbers from 1 to 1,000,000.

# A normal list:

numbers = list(range(1, 1_000_001))

# creates and stores all those numbers in memory.

# A generator can produce:

# 1 → when needed
# 2 → when needed
# 3 → when needed
# ...

# So the core idea is:

# A generator produces values one at a time instead of creating/storing all values at once.



#  Generator vs Normal Function


# Normal function
#       ↓
# return
#       ↓
# Function finishes


# Generator
#       ↓
# yield
#       ↓
# Pause
#       ↓
# Give value
#       ↓
# Resume later



# In Genertors Values are generated when needed.

# This is called lazy evaluation.

# Remember:

# Generator = lazy production of values.


#  Example

# A generator function uses yield:

def numbers():
    yield 10
    yield 20
    yield 30

values = numbers()    

print(next(values))
print(next(values))
print(next(values))

# You should understand why the output is:

# 10
# 20
# 30

# And what happens if you call:

# next(values)

# one more time.

# Answer: it raises StopIteration because the generator has no more values.


#  example using generators

def even_numbers(limit):
    for number in range(2, limit + 1):
        if number % 2 == 0:
            yield number


numbers = even_numbers(10)

for number in numbers:
    print(number)


#     Why limit + 1?

# Because the ending value of range() is not included.

# For:

# range(2, 10)

# we get:

# 2 3 4 5 6 7 8 9

# So we use:

# range(2, limit + 1)

# to include 10.