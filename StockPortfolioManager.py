class StockPortfolioManager:
    def __init__(self):
        self.portfolios = {}
        self.available_balance = 10000

    def add_new_portfolio(self, portfolio_name):
        if portfolio_name not in self.portfolios:
            self.portfolios[portfolio_name] = {}
            print(f"New portfolio '{portfolio_name}' created.")
        else:
            print("Portfolio already exists.")

    def add_stock_to_portfolio(self, portfolio_name, stock_name, shares):
        if portfolio_name in self.portfolios:
            if stock_name not in self.portfolios[portfolio_name]:
                self.portfolios[portfolio_name][stock_name] = shares
                print(f"Stock '{stock_name}' added to portfolio '{portfolio_name}'.")
            else:
                print(f"Stock '{stock_name}' already in portfolio '{portfolio_name}'.")
        else:
            print(f"Portfolio '{portfolio_name}' does not exist.")

    def buy_shares(self, portfolio_name, stock_name, shares, price_per_share):
        cost = shares * price_per_share * 1.1  # Adding a 10% transaction fee
        if portfolio_name in self.portfolios:
            if self.available_balance >= cost:
                if stock_name in self.portfolios[portfolio_name]:
                    self.portfolios[portfolio_name][stock_name] += shares
                else:
                    self.portfolios[portfolio_name][stock_name] = shares
                self.available_balance -= cost
                print(f"Bought {shares} shares of '{stock_name}' for portfolio '{portfolio_name}'.")
            else:
                print("Not enough funds.")
        else:
            print(f"Portfolio '{portfolio_name}' does not exist.")

    def sell_shares(self, portfolio_name, stock_name, shares, price_per_share):
        if portfolio_name in self.portfolios:
            if stock_name in self.portfolios[portfolio_name]:
                if self.portfolios[portfolio_name][stock_name] >= shares:
                    self.portfolios[portfolio_name][stock_name] -= shares
                    self.available_balance += shares * price_per_share * 0.9  # Selling at 10% discount
                    print(f"Sold {shares} shares of '{stock_name}' from portfolio '{portfolio_name}'.")
                else:
                    print("Insufficient shares to sell.")
            else:
                print(f"Stock '{stock_name}' not found in portfolio '{portfolio_name}'.")
        else:
            print(f"Portfolio '{portfolio_name}' does not exist.")

    def deposit_money(self, amount):
        self.available_balance += amount
        print(f"Deposited ${amount} successfully. Available balance: ${self.available_balance}")

    def withdraw_money(self, amount):
        if self.available_balance >= amount:
            self.available_balance -= amount
            print(f"Withdrew ${amount} successfully. Available balance: ${self.available_balance}")
        else:
            print("Insufficient funds.")

    def display_available_balance(self):
        print(f"Available balance: ${self.available_balance}")

    def display_all_portfolios(self):
        print("All Portfolios:")
        for portfolio in self.portfolios:
            print(f"{portfolio}: {self.portfolios[portfolio]}")

    def display_specific_portfolio(self, portfolio_name):
        if portfolio_name in self.portfolios:
            print(f"Portfolio '{portfolio_name}': {self.portfolios[portfolio_name]}")
        else:
            print(f"Portfolio '{portfolio_name}' not found.")


def main():
    manager = StockPortfolioManager()

    while True:
        print("\nMenu:")
        print("1. Create new portfolio")
        print("2. Add stock to portfolio")
        print("3. Buy shares")
        print("4. Sell shares")
        print("5. Deposit money")
        print("6. Withdraw money")
        print("7. Display available balance")
        print("8. Display all portfolios")
        print("9. Display specific portfolio")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            portfolio_name = input("Enter portfolio name: ")
            manager.add_new_portfolio(portfolio_name)
        elif choice == "2":
            portfolio_name = input("Enter portfolio name: ")
            stock_name = input("Enter stock name: ")
            shares = int(input("Enter number of shares: "))
            manager.add_stock_to_portfolio(portfolio_name, stock_name, shares)
        elif choice == "3":
            portfolio_name = input("Enter portfolio name: ")
            stock_name = input("Enter stock name: ")
            shares = int(input("Enter number of shares to buy: "))
            price_per_share = float(input("Enter price per share: "))
            manager.buy_shares(portfolio_name, stock_name, shares, price_per_share)
        elif choice == "4":
            portfolio_name = input("Enter portfolio name: ")
            stock_name = input("Enter stock name: ")
            shares = int(input("Enter number of shares to sell: "))
            price_per_share = float(input("Enter price per share: "))
            manager.sell_shares(portfolio_name, stock_name, shares, price_per_share)
        elif choice == "5":
            amount = float(input("Enter amount to deposit: "))
            manager.deposit_money(amount)
        elif choice == "6":
            amount = float(input("Enter amount to withdraw: "))
            manager.withdraw_money(amount)
        elif choice == "7":
            manager.display_available_balance()
        elif choice == "8":
            manager.display_all_portfolios()
        elif choice == "9":
            portfolio_name = input("Enter portfolio name: ")
            manager.display_specific_portfolio(portfolio_name)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
