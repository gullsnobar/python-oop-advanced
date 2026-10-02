# 🐍 Python OOP & Advanced Concepts

A practical learning repository covering **Python Object-Oriented Programming (OOP)** and important advanced Python concepts through simple, working examples.

The goal of this repository is not just to learn the syntax, but to understand **what each concept solves, why it is used, and where it is useful in real applications.**

---

## 📚 Topics Covered

### 1. 🏗️ Classes

**What problem does it solve?**

A class provides a blueprint for creating objects with related data and behavior.

```text
CLASS
  ↓
Blueprint for creating objects
  ↓
Defines data + behavior
```

---

### 2. 📦 Objects

**What is an instance?**

An object is an actual instance created from a class.

```text
CLASS
  ↓
Creates
  ↓
OBJECT / INSTANCE
```

---

### 3. ⚙️ `__init__()`

**Why is it used?**

`__init__()` initializes an object's data when the object is created.

```text
Object Creation
      ↓
   __init__()
      ↓
Initial Object State
```

---

### 4. 👤 `self`

**What does it refer to?**

`self` refers to the **current object/instance**.

It allows each object to access and modify its own data.

```text
self.name
self.email
self.age
```

---

### 5. 🧩 Instance Attributes

**What are they?**

Instance attributes contain **object-specific data**.

Different objects can have different values.

```text
User 1 → name = "Gull"
User 2 → name = "Ali"
```

---

### 6. 🏛️ Class Attributes

**What are they?**

Class attributes belong to the class and can be **shared by its instances**.

```text
Class
  ↓
Shared Class Data
  ↓
Multiple Objects
```

---

### 7. 🏷️ `classmethod`

**What is it used for?**

A class method works with the **class itself** rather than a specific object.

It receives `cls` as its first parameter.

```python
@classmethod
def method(cls):
    ...
```

---

### 8. 🔧 `staticmethod`

**What is it used for?**

A static method does not need access to the instance or class state.

```python
@staticmethod
def method():
    ...
```

It is useful for utility/helper functionality related to a class.

---

# 🔗 Inheritance & Polymorphism

### 9. 🌳 Inheritance

**What problem does it solve?**

Inheritance allows a child class to **reuse and extend behavior** from a parent class.

```text
Parent Class
     ↓
Child Class
     ↓
Reuses + Extends Behavior
```

---

### 10. 🔄 Method Overriding

**What does it do?**

Method overriding allows a child class to provide its **own implementation** of a method inherited from the parent.

```text
Parent Method
     ↓
Inherited by Child
     ↓
Child Changes Implementation
```

---

### 11. 🧬 `super()`

**Why is it used?**

`super()` allows a child class to access functionality from its parent class.

```text
Child Class
     ↓
super()
     ↓
Parent Implementation
```

It is commonly used when extending a parent's `__init__()` or another method.

---

# 🔁 Iteration & Generators

### 12. 🔄 Iterable

**What is an iterable?**

An iterable is an object whose values can be accessed one by one, usually using a `for` loop.

Examples:

```python
list
tuple
string
dictionary
set
```

```text
ITERABLE
   ↓
Can be iterated
   ↓
for loop
```

---

### 13. ➡️ Iterator

**What is an iterator?**

An iterator produces values one at a time using `next()`.

```text
ITERABLE
   ↓
iter()
   ↓
ITERATOR
   ↓
next()
   ↓
Next Value
```

---

### 14. ⚡ Generator

**What problem does it solve?**

A generator produces values **lazily**, meaning values are generated only when needed.

Generators use the `yield` keyword.

```text
GENERATOR
    ↓
yield
    ↓
One Value at a Time
    ↓
Memory Efficient
```

---

# 📝 Python Expressions & Functions

### 15. 📋 List Comprehension

**What is it used for?**

List comprehensions provide a concise way to create lists from existing iterables.

Instead of writing:

```python
numbers = []

for number in range(10):
    numbers.append(number * 2)
```

You can write:

```python
numbers = [number * 2 for number in range(10)]
```

```text
LIST COMPREHENSION
        ↓
Concise List Creation
```

---

### 16. 🎨 Decorator

**What problem does it solve?**

A decorator allows us to **wrap and enhance the behavior of a function** without directly changing its original code.

```text
Original Function
       ↓
   Decorator
       ↓
Enhanced Function
```

Example:

```python
@decorator
def my_function():
    pass
```

---

# ⚙️ Concurrency & Parallelism

### 17. 🧵 Thread

**When is it useful?**

Threads are especially useful for handling **I/O-bound tasks**, where the program spends time waiting for operations such as:

* API requests
* Network operations
* File operations
* Database operations

```text
THREAD
   ↓
I/O-Bound Work
   ↓
Waiting can overlap
```

---

### 18. ⚡ Process

**When is it useful?**

Processes are useful for **CPU-bound work**, where the program needs significant CPU computation.

Examples include:

* Heavy calculations
* CPU-intensive data processing
* Image processing
* Computational tasks

```text
PROCESS
   ↓
CPU-Bound Work
   ↓
Parallel CPU Execution
```

---

# 🗺️ Learning Roadmap

The concepts in this repository follow this progression:

```text
                    PYTHON
                       │
                       ▼
                   CLASS
                       │
                       ▼
                    OBJECT
                       │
                       ▼
                  __init__()
                       │
                       ▼
                     self
                       │
              ┌────────┴────────┐
              ▼                 ▼
      INSTANCE ATTRIBUTE   CLASS ATTRIBUTE
              │                 │
              └────────┬────────┘
                       ▼
                classmethod
                       │
                       ▼
                staticmethod
                       │
                       ▼
                 INHERITANCE
                       │
                       ▼
                  OVERRIDING
                       │
                       ▼
                    super()
                       │
                       ▼
                  ITERABLE
                       │
                       ▼
                  ITERATOR
                       │
                       ▼
                  GENERATOR
                       │
                       ▼
             LIST COMPREHENSION
                       │
                       ▼
                  DECORATOR
                       │
              ┌────────┴────────┐
              ▼                 ▼
            THREAD           PROCESS
              │                 │
           I/O-Bound         CPU-Bound
```

---

# 📁 Repository Structure

Each major concept is demonstrated in its own Python file.

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
│
├── decorators.py
├── threading.py
└── multiprocessing.py
```

Each file contains **working Python code** demonstrating the related concept with practical examples.

---

# Learning Goals

By completing this repository, I aim to understand:

* How classes and objects work
* How object state is managed
* The difference between instance and class attributes
* How `classmethod` and `staticmethod` work
* How inheritance enables code reuse
* How method overriding changes inherited behavior
* How `super()` accesses parent implementations
* The difference between iterables and iterators
* How generators produce values lazily
* How list comprehensions simplify list creation
* How decorators modify or extend function behavior
* When to use threads for I/O-bound tasks
* When to use processes for CPU-bound tasks

---

## Goal

> **Understand the concept → Write the code → Run it → Experiment with it → Apply it in real projects.**

This repository is focused on **practical understanding rather than memorizing Python syntax**.
