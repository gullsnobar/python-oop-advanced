# Itertors

# First: What problem does an iterator solve?

# Sometimes we want to go through data one value at a time.

# For example:

numbers = [10, 20, 30, 40]

# Instead of getting everything at once, an iterator lets Python keep track of:

# "Where am I currently in this sequence?"

# So the core idea is:

# Iterable
#    ↓
# iter()
#    ↓
# Iterator
#    ↓
# next()
#    ↓
# Next value


# Get values using next()

# Now we can manually get values:

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# Creating Your Own Iterator

# This is the next important level.

# An iterator object normally implements:

# __iter__()

# and:

# __next__()



class Count:

    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number

        raise StopIteration            


numbers = Count(3)

print(next(numbers))
print(next(numbers))
print(next(numbers))    


# Why __iter__() and __next__()?

# Remember just this:

# __iter__()
#    ↓
# Returns the iterator


# __next__()
#    ↓
# Returns the next value

# For an object to behave as an iterator, it implements both.


# A generator is a type of iterator.

# Iterator
#    │
#    └── Generator

# A generator automatically handles the iterator machinery for you.


# Practical Example

class CountDown:

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= 1:
            number = self.current
            self.current -= 1
            return number

        raise StopIteration

counter = CountDown(5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))