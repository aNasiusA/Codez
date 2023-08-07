class Person:
    def __init__(self,name,age,gender,ID_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.ID_number = ID_number

    def get_user_details(self):
        self.name = input("Enter your name-->")
        self.age = input("Enter your age-->")
        self.gender = input("Enter your Gender-->")
        self.ID_number = input("Enter your ID number-->")
        
    def show_user_info(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Gender :", self.gender)
        print("ID_number :", self.ID_number)

    def create_user(self):
        while True:
            create = input("Do you want to create user (y/n)")
            if create == "y":
                Person1.get_user_details()
                Person1.show_user_info()
            else:
                break
Person1 = Person("User", 00, "Gender",0)
Person2 = Person1.create_user()
print(Person2)
