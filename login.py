from classes import Admin, Customer 

def login():
    "Habdle user login for customer or admin"
    userR = True
    while userR:
        role = input("Are you an Admin or Customer? (AC): ").strip().upper()
        if role == 'C':
            name = input("Please enter name: ").strip()
            current_user = Customer(name)
            print(f"Welcome, {name}!")
            return current_user
        elif role == 'A':
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if username == 'Admin' and password == '1234':
                current_user = Admin(username)
                print("Admin login successful")
                return current_user
            else:
                print("Invalid password. If you forget the password, contact system adminitrator to reset it")
        else:
            print("Invalid choice")