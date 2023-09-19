from CryptoCase import Portfolio

if __name__ == '__main__':
    name = input("Enter investor's name: ")
    portfolio = Portfolio(name)
    portfolio.main_menu()