class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    pass

dog = Dog()

dog.eat()
dog.sleep()

# The imp idea

# Parent
#  ├── eat()
#  └── sleep()
#        ↓
#      Child
#        ↓
#  Can use both