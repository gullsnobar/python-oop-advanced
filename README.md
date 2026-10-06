# Python OOP and Advanced Concepts

This repository contains my hands-on practice with Python Object-Oriented Programming and advanced Python concepts.

The purpose of this repository is to understand the concepts through code and keep a reference that I can use later for revision and interview preparation.

## Topics Covered

### Object-Oriented Programming

* Classes and Objects
* `__init__()`
* `self`
* Instance Attributes
* Class Attributes
* Instance Methods
* Class Methods
* Static Methods
* Inheritance
* Method Overriding
* `super()`

### Advanced Python

* Iterables
* Iterators
* Generators
* List Comprehensions
* Decorators
* Multithreading
* Multiprocessing

---

## Concepts

### 1. Classes and Objects

A class is a blueprint used to create objects.

An object is an instance of a class that contains its own data and behavior.

```python
class User:
    def __init__(self, name):
        self.name = name


user = User("Gull")

print(user.name)
```

**Key points:**

* Class defines the structure and behavior.
* Object is an instance of that class.
* Multiple objects can be created from the same class.

File: `classes_objects.py`

---

### 2. `__init__()` and `self`

`__init__()` is used to initialize an object's data when the object is created.

`self` refers to the current object.

```python
class User:
    def __init__(self, name):
        self.name = name
```

Here, `self.name` is an instance attribute belonging to the current object.

File: `instance_attributes.py`

---

### 3. Instance Attributes

Instance attributes belong to individual objects.

```python
user1.name = "Gull"
user2.name = "Ali"
```

Each object can have different values.

File: `instance_attributes.py`

---

### 4. Class Attributes

Class attributes belong to the class and can be shared by its objects.

```python
class User:
    role = "User"
```

Class attributes are useful when the same value or configuration should be available to multiple objects.

File: `class_attributes.py`

---

### 5. Class Methods

A class method works with the class rather than a specific object.

It uses `cls` instead of `self`.

```python
class User:

    @classmethod
    def create_guest(cls):
        return cls("Guest")
```

Class methods can also be used as alternative constructors.

File: `classmethod.py`

---

### 6. Static Methods

A static method does not automatically receive `self` or `cls`.

It is useful for utility functionality related to a class.

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
```

File: `staticmethod.py`

---

### 7. Inheritance

Inheritance allows a child class to reuse functionality from a parent class.

```python
class Employee:
    def work(self):
        print("Working")


class Developer(Employee):
    def code(self):
        print("Writing code")
```

`Developer` inherits the `work()` method from `Employee`.

File: `inheritance.py`

---

### 8. Method Overriding

Method overriding happens when a child class provides its own implementation of a method that already exists in the parent class.

```python
class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")
```

The child implementation replaces the inherited behavior when called on a `Developer` object.

File: `overriding.py`

---

### 9. `super()`

`super()` is used to access functionality from the parent class.

It is commonly used when a child class needs to extend the parent's constructor or method.

```python
class Employee:

    def __init__(self, name):
        self.name = name


class Developer(Employee):

    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
```

File: `super.py`

---

## Advanced Python Concepts

### 10. Iterables

An iterable is an object that can be iterated over.

Examples include:

* Lists
* Tuples
* Strings
* Dictionaries
* Sets

An iterable can be passed to `iter()` to obtain an iterator.

File: `iterables.py`

---

### 11. Iterators

An iterator produces values one at a time.

Important functions and methods:

```python
iter()
next()
__iter__()
__next__()
```

When there are no more values, the iterator raises `StopIteration`.

Example:

```python
numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

File: `iterators.py`

---

### 12. Generators

A generator produces values one at a time instead of creating all values at once.

Generators use `yield`.

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Generators are useful when working with large amounts of data because values can be generated when they are needed.

File: `generators.py`

---

### 13. List Comprehensions

List comprehensions provide a concise way to create lists.

Instead of:

```python
numbers = []

for number in range(5):
    numbers.append(number * 2)
```

We can write:

```python
numbers = [number * 2 for number in range(5)]
```

They can also include conditions:

```python
even_numbers = [number for number in range(10) if number % 2 == 0]
```

File: `list_comprehensions.py`

---

### 14. Decorators

A decorator is a function that adds behavior to another function without changing its original implementation.

Basic structure:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        # additional behavior
        result = function(*args, **kwargs)
        return result

    return wrapper
```

It can then be used with:

```python
@decorator
def my_function():
    pass
```

Decorators are commonly used for logging, authentication, permissions, and timing functions.

File: `decorators.py`

---

### 15. Multithreading

Multithreading allows multiple threads to perform tasks concurrently within a process.

It is particularly useful for I/O-bound tasks where the program spends time waiting.

Examples:

* Network requests
* File operations
* API calls
* Downloading files

Basic structure:

```python
import threading

thread = threading.Thread(target=my_function)

thread.start()
thread.join()
```

Important methods:

* `start()` starts the thread.
* `join()` waits for the thread to finish.

File: `threading_basics.py`

---

### 16. Multiprocessing

Multiprocessing allows multiple processes to execute independently.

It is useful for CPU-bound tasks that require significant processing power.

Examples:

* Large calculations
* Data processing
* Image processing
* Video processing

Basic structure:

```python
import multiprocessing

if __name__ == "__main__":

    process = multiprocessing.Process(target=my_function)

    process.start()
    process.join()
```

Important methods:

* `start()` starts the process.
* `join()` waits for the process to finish.

File: `multiprocessing_basics.py`

---

## Multithreading vs Multiprocessing

| Multithreading                       | Multiprocessing                      |
| ------------------------------------ | ------------------------------------ |
| Uses multiple threads                | Uses multiple processes              |
| Threads share process memory         | Processes have separate memory       |
| Generally useful for I/O-bound tasks | Generally useful for CPU-bound tasks |
| Lightweight compared to processes    | More resource-intensive              |

Simple rule:

```text
I/O-bound  → Multithreading
CPU-bound  → Multiprocessing
```

---

## Repository Structure

```text
python-oop-advanced/
│
├── README.md
│
├── classes_objects.py
├── instance_attributes.py
├── class_attributes.py
├── classmethod.py
├── staticmethod.py
│
├── inheritance.py
├── overriding.py
├── super.py
│
├── iterables.py
├── iterators.py
├── generators.py
├── list_comprehensions.py
├── decorators.py
├── threading_basics.py
└── multiprocessing_basics.py
```

Each topic is implemented in a separate Python file so it can be studied and executed independently.

---

## Purpose

This repository is mainly for:

* Strengthening Python fundamentals
* Practicing OOP concepts
* Understanding advanced Python features
* Keeping code examples for future revision
* Preparing for Python technical interviews

The focus is on understanding **what a concept does, why it is used, and how to implement it in Python**.
