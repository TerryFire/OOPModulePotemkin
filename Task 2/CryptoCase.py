class USD_Price:
    def __get__(self, instance, owner):
        value = instance.value.get(instance.coin_name)
        amount = instance.coin.get(instance.coin_name)
        if value is not None and amount is not None:
            return amount * value
        else:
            return None

class Portfolio:

    def __init__(self, person_name):
        self.name = person_name
        self.coin = {}
        self.value = {}
        self.usd_price = USD_Price()
        self.coin_name = None

    def add_coin(self, coin_name, amount):
        if coin_name in self.coin:
            self.coin[coin_name] += amount
        else:
            self.coin[coin_name] = amount

    def del_coin(self, coin_name):
        if coin_name in self.coin:
            del self.coin[coin_name]
        else:
            raise ValueError(f"Coin {coin_name} not found in portfolio\n")

    def convert_to_usd(self):
        print(f'Portfolio of investor {self.name} converted to USD using current rate\n')

    def show_portfolio(self):
        print(f"Portfolio of investor: {self.name}")
        for coin_name, num in self.coin.items():
            self.coin_name = coin_name
            usd_value = self.usd_price.__get__(self, self.__class__)
            print(f"{coin_name}: Coins - {num}, USD value = {usd_value} USD")

    def sort_portfolio(self):
        sorted_portfolio = sorted(self.coin.items(), key=lambda x: self.value[x[0]], reverse=True)
        print(f"Portfolio of investor {self.name} sorted in USD:")
        for coin_name, num in sorted_portfolio:
            self.coin_name = coin_name
            usd_value = self.usd_price.__get__(self, self.__class__)
            print(f'{coin_name}: {num} coins = {usd_value} USD')

    def main_menu(self):
        while True:
            print("""Crypto Portfolio Management System
            1. Show Portfolio
            2. Add Coin
            3. Delete Coin
            4. Convert to USD
            5. Sort Portfolio
            6. Exit""")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_portfolio()
            elif choice == "2":
                coin_name = input("Enter coin name: ")
                amount = int(input("Enter amount: "))
                value = int(input("Enter it's USD rate: "))
                self.add_coin(coin_name, amount)
                self.value = {coin_name:value}
            elif choice == "3":
                coin_name = input("Enter coin name: ")
                self.del_coin(coin_name)
            elif choice == "4":
                self.convert_to_usd()
            elif choice == "5":
                self.sort_portfolio()
            elif choice == "6":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

# Приклад використання без меню для тесту
# p = Portfolio('Sam')
# p.value = {"BTC": 45620, "ETH": 2510}
# p.add_coin("BTC", 10)
# p.add_coin("ETH", 40)
# p.convert_to_usd() #метод шредінгера
# p.show_portfolio()
# p.sort_portfolio()
