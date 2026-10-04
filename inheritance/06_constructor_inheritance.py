This connects inheritance with something you already learned:

__init__()

class User:

    def __init__(self, name):
        self.name = name

class Admin(User):
    pass

admin = Admin("Gull")
print(admin.name)