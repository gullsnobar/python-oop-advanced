# combine everything into something closer to real application code.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

    def work(self):
        print(f"{self.name} is working")


class Developer(Employee):

    def write_code(self):
        print(f"{self.name} is writing code")


class Manager(Employee):

    def work(self):
        print(f"{self.name} is managing the team")


developer = Developer("Gull", 100000)
manager = Manager("Ali", 150000)

developer.display_info()
developer.work()
developer.write_code()

print()

manager.display_info()
manager.work()

