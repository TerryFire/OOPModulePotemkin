from Task3.Descriptors.UsernameDescriptor import UsernameDescriptor
from Task3.Descriptors.PinDescriptor import PinDescriptor


class User:
    username = UsernameDescriptor()
    pin_code = PinDescriptor()

    def __init__(self, name, pin_code, balance=0.0):
        self._username = ""
        self._pin_code = ""
        self.username = name
        self.pin_code = pin_code
        self.balance = balance

    def check_username(self, input_username):
        return input_username == self.username

    def check_pin_code(self, input_pin):
        return input_pin == self.pin_code

    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw_money(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def check_balance(self):
        return self.balance

class ATM:
    def __init__(self):
        self.users = {}
        self.load_data()

    def register_user(self, name, pin_code):
        if name not in self.users:
            if self.users[name].username == name and self.users[name].pin_code == pin_code:
                print(f"User {name} registered successfully.\n")
                self.save_data()
                return True
        print("User registration failed. Incorrect username or PIN.\n")
        return False

    def login_user(self, name, pin_code):
        if name in self.users:
            if self.users[name].username == name and self.users[name].pin_code == pin_code:
                print("Login successful!")
                return self.users[name]
        print("Login failed. Incorrect username or PIN.")
        return


    def save_data(self):
        with open("users.txt", "w") as file:
            for name, user in self.users.items():
                file.write(f"{name},{user.pin_code},{user.balance}\n")

    def load_data(self):
        try:
            with open("users.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    name, pin_code, balance = line.strip().split(",")
                    self.users[name] = User(name, pin_code, float(balance))
        except FileNotFoundError:
            pass
