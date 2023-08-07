class User:
    def __init__(self, name, age, gender, ID_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.ID_number = ID_number
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, ID Number: {self.ID_number}"

    @classmethod
    def get_user_details(cls):
        name = input("Enter your name --> ")
        age = input("Enter your age --> ")
        gender = input("Enter your Gender --> ")
        ID_number = input("Enter your ID number --> ")
        return cls(name, age, gender, ID_number)
    
def main():
    users = []

    while True:
        choice = input("Do you want to create a user (y/n)? ").lower()

        if choice == "y":
            user = User.get_user_details()
            users.append(user)
            print("User added successfully!")
        elif choice == "n":
            break
        else:
            print("Invalid choice")
    
    print("User information:")
    for user in users:
        print(user)

if __name__ == "__main__":
    main()
