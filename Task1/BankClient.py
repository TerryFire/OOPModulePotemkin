class Client:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Client Name: {self.name}, Balance: {self.balance}"

class Bank:
    def __init__(self):
        self.clients = []

    def add_client(self, name):
        client = Client(name)
        self.clients.append(client)

    def find_client(self, name):
        for client in self.clients:
            if client.name == name:
                return client

    def save_data_to_file(self, file_name):
        try:
            with open(file_name, 'w') as file:
                for client in self.clients:
                    file.write(f"{client.name},{client.balance}\n")
            print(f"Data saved to {file_name}")
        except FileNotFoundError:
            print(f"Error: File not found - {file_name}")
        except IOError:
            print(f"Error: Could not write to {file_name}")

    def load_data_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    name, balance = line.strip().split(',')
                    balance = float(balance)
                    self.add_client(name)
                    client = self.find_client(name)
                    if client:
                        client.balance = balance
            print(f"Data loaded from {file_name}")
        except FileNotFoundError:
            print(f"Error: File not found - {file_name}")
        except IOError:
            print(f"Error: Could not read from {file_name}")

# Приклад використання
bank = Bank()
bank.add_client("Sam")
bank.add_client("Alex")

# Зберегти дані в файл
bank.save_data_to_file("bank_data.txt")

# Завантажити дані з файлу
bank.load_data_from_file("bank_data.txt")

# Знайти клієнта
client = bank.find_client("John")
print(client)
