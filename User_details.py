class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Age: {self.age}"
