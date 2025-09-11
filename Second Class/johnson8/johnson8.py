import random

class Account:
    # This class represents a bank account.
    # It contains methods to create an account, deposit, withdraw, and check balance.
    def __init__(self, first_name, last_name, ssn):
        self.account_number = random.randint(10000000, 99999999)
        self.owner_first_name = first_name
        self.owner_last_name = last_name
        self.social_security_number = ssn
        self.pin = f"{random.randint(0, 9999):04d}"
        self.balance = 0
    
    def getAccountNumber(self):
        return self.account_number

    def getOwnerFirstName(self):
        return self.owner_first_name

    def getOwnerLastName(self):
        return self.owner_last_name

    def getSocialSecurityNumber(self):
        # Return the last 4 digits of the social security number
        return self.social_security_number[-4:]

    def getPIN(self):
        return self.pin

    def setPIN(self, pin):
        # Set the PIN if it is a 4-digit number
        if len(pin) == 4 and pin.isdigit():
            self.pin = pin

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

class Bank:
    def __init__(self):
        self.accounts = []

    def addAccountToBank(self, account):
        self.accounts.append(account)
        return True

    def removeAccountFromBank(self, account):
        # Remove an account from the bank
        # Check if the account exists in the bank
        if account in self.accounts:
            self.accounts.remove(account)
            return True
        return False

    def findAccount(self, account_number):
        # Find an account by its account number
        # Check if the account number exists in the bank
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def addMonthlyInterest(self, percent):
        # Add monthly interest to all accounts
        # Check if the interest percentage is valid
        if percent <= 0:
            print("Invalid interest percentage.")
            return
        monthly_rate = percent / 100 / 12 
        for acc in self.accounts:
            interest = acc.balance * monthly_rate
            acc.balance += interest


class CoinCollector:
    def __init__(self):
        self.coins = []

    # This class is used to collect coins and calculate their total value.
    # It contains a method to parse the coins and calculate their total value.
    def parseChange(coins):
        # This method takes a string of coins and calculates the total value in cents.
        values = {
        'P': 1,    
        'N': 5,    
        'D': 10,   
        'Q': 25,   
        'H': 50,   
        'W': 100   
        }
        total = sum(values.get(c.upper(), 0) for c in coins)
        return total

    
class BankUtility:
    def __init__(self):
        self.coinCollector = CoinCollector()
    # Methods to check if a string is numeric .        
    def isNumeric(numberToCheck):
        try:
            float(numberToCheck)
            return True
        except ValueError:
            return False
    
    def promptUserForPositiveNumber(self, prompt):
        # Prompt the user for a positive number
        # Check if the input is a valid number
        while True:
            user_input = input(f"{prompt} ")
            if BankUtility.isNumeric(user_input):
                value = float(user_input)
                if value > 0:
                    return value
                else:
                    print("Amount cannot be negative. Try again.")
            else:
                print("Invalid input. Please enter a valid number.")

class BankManager:  
    def __init__(self):
        self.bank = Bank()

    def promptForAccountNumberAndPIN(self, bank):
        # Prompt the user for account number and PIN
        # Check if the account number is valid
        try:
            account_number = int(input("Enter your account number: "))
        except ValueError:
            print("Invalid account number format.")
            return None

        account = bank.findAccount(account_number)
        if account is None:
            print(f"Account not found for account number: {account_number}")
            return None

        input_pin = input("Enter your PIN: ")   
        if len(input_pin) != 4 or not input_pin.isdigit():
            print("Invalid PIN format. Must be 4 digits.")
            return None

        return account

def main():
    # Main function to run the bank program
    bank = Bank()
    bankManager = BankManager()
    bankUtility = BankUtility()

    while True:
        print("===================================")
        print("Welcome to Python Bank!")
        print("===================================")
        print("1. Open An Account")
        print("2. Get Account Information and Balance")
        print("3. Change Account PIN")
        print("4. Deposit Money")
        print("5. Transfer Money between Accounts")
        print("6. Withdraw Money from Account")
        print("7. ATM Withdrawal")
        print("8. Deposit Change")
        print("9. Close an Account")
        print("10. Add Monthly Interest to All Accounts")
        print("11. Exit")
        print("===================================")
        
        # print all accounts    
        print("      ======All Accounts=====      ")
        for account in bank.accounts:
            print(f"Account #: {account.getAccountNumber()} | Account Owner: {account.getOwnerFirstName()} {account.getOwnerLastName()} | Balance: ${account.getBalance():.2f} | PIN: {account.getPIN()}")
        print("===================================")
        try:
            choice = int(input("Please select an option: "))
            match choice:

                case 1:
                    # Open a new account
                    print("===Open Account===")
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    ssn = input("Enter social security number: ")

                    if not BankUtility.isNumeric(ssn) or len(ssn) != 9:
                        print("Social Security Number must be 9 digits.")
                        print("===================================")
                        continue
                    new_account = Account(first_name, last_name, ssn)
                    bank.addAccountToBank(new_account)
                    print(f"Account #: {new_account.getAccountNumber()} | Account Owner: {new_account.getOwnerFirstName()} {new_account.getOwnerLastName()} | Balance: ${new_account.getBalance():.2f} | PIN: {new_account.getPIN()} | SSN: XXX-XX-{new_account.getSocialSecurityNumber()}")
                    print("===================================")

                case 2:
                    # Get account information
                    print("===Get Account Information===")
                    account = bankManager.promptForAccountNumberAndPIN(bank)
                    print("===================================")
                    if account:
                        print(f"Account #: {account.getAccountNumber()} | Account Owner: {account.getOwnerFirstName()} {account.getOwnerLastName()} | Balance: ${account.getBalance():.2f} | PIN: {account.getPIN()} | SSN: XXX-XX-{account.getSocialSecurityNumber()}")
                        print("===================================")

                    else:
                        print("Account not found.")
                        print("===================================")

                case 3:
                    # Change account PIN
                    print("===Change Account PIN===")
                    account = bankManager.promptForAccountNumberAndPIN(bank)
                    print("===================================")
                    if account:
                        new_pin = input("Enter new PIN: ")
                        double_check_new_pin = input("Enter new PIN again to confirm: ")
                        if new_pin != double_check_new_pin:
                            print("PINs do not match. Try again.")     
                            print("===================================")
                        else:
                            account.setPIN(new_pin)
                            print(f"PIN for account {account.getAccountNumber()} changed successfully.")
                            print("===================================")
                    else:
                        print("Account not found.")
                        print("===================================")
                        
                case 4:
                    # deposit money into account
                    print("===Deposit Money===")
                    account = bankManager.promptForAccountNumberAndPIN(bank)
                    print("===================================")
                    if account:
                        try:    
                            amount = bankUtility.promptUserForPositiveNumber("Enter amount to deposit:")
                            print("===================================")
                            if account.deposit(amount):
                                print(f"Deposited ${amount:.2f} into account {account.getAccountNumber()}.")
                                print(f"New balance: ${account.getBalance():.2f}")
                                print("===================================")
                            else:
                                print("Deposit failed.")
                                print("===================================")
                        except ValueError:
                            print("Invalid amount. Please enter a valid number.")
                            print("===================================")
                    else:
                        print("Account not found.")
                        print("===================================")

                case 5:
                    # Transfer money between accounts
                    print("===Transfer Money===")
                    print("Account to Transfer From:")
                    print("===================================")

                    from_account = bankManager.promptForAccountNumberAndPIN(bank)
                    print("===================================")
                    if from_account:
                        print("Account to Transfer money To:")
                        print("===================================")
                        to_account = bankManager.promptForAccountNumberAndPIN(bank)
                        print("===================================")
                        if to_account:
                            try:
                                amount = bankUtility.promptUserForPositiveNumber("Enter amount to transfer in dollars and cents (e.g. 2.57):")
                                if from_account.withdraw(amount) and to_account.deposit(amount):
                                    print(f"Transferred of ${amount:.2f} from account {from_account.getAccountNumber()} to account {to_account.getAccountNumber()} Complete.")
                                    print(f"New balance in account: {from_account.getAccountNumber()} is ${from_account.getBalance():.2f}")
                                    print(f"New balance in account: {to_account.getAccountNumber()} is ${to_account.getBalance():.2f}")
                                    print("===================================")
                                else:
                                    print("Transfer failed.")
                                    print("===================================")
                            except ValueError:
                                print("Invalid amount. Please enter a valid number.")
                                print("===================================")
                        else:
                            print("Recipient account not found.")
                            print("===================================")

                    else:
                        print("Your account not found.")
                        print("===================================")

                case 6:
                    # Withdraw money from account
                    print("===Withdraw Money===")
                    account = bankManager.promptForAccountNumberAndPIN(bank)
                    print("===================================")
                    if account:
                        try:
                            amount = bankUtility.promptUserForPositiveNumber("Enter amount to withdraw:")

                            print("===================================")
                            if amount > account.getBalance():
                                print("Insufficient funds.")
                                print("===================================")
                                continue
                            
                            if account.withdraw(amount):
                                print(f"Withdrew ${amount:.2f} from account {account.getAccountNumber()}.")
                                print(f"New balance: ${account.getBalance():.2f}")
                                print("===================================")

                            else:
                                print("Withdrawal failed.")
                            print("===================================")
                        except ValueError:
                            print("Invalid amount. Please enter a valid number.")
                            print("===================================")
                    else:
                        print("Account not found.")
                        print("===================================")

                case 7:
                    # ATM withdrawal
                    print("===ATM Withdrawal===")
                    account = bankManager.promptForAccountNumberAndPIN(bank)
                    print("===================================")
                    if account:
                        try:
                            amount = bankUtility.promptUserForPositiveNumber("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000):")
                            if amount % 5 != 0 or amount > 1000:
                                print("Invalid amount. Must be a multiple of $5 and not exceed $1000.")
                                continue
                            twenty_dollar_bills = int(input("Enter number of $20 bills: "))
                            ten_dollar_bills = int(input("Enter number of $10 bills: "))
                            five_dollar_bills = int(input("Enter number of $5 bills: "))
                            total_withdrawn = (twenty_dollar_bills * 20) + (ten_dollar_bills * 10) + (five_dollar_bills * 5)
                            if total_withdrawn != amount:
                                print(f"Total withdrawn (${total_withdrawn}) does not match requested amount (${amount:.1f}).")
                                print("===================================")
                                continue
                            if account.getBalance() < total_withdrawn:
                                print("Insufficient funds in account.")
                                print("===================================")
                                continue
                            if account.withdraw(amount):
                                print(f"Withdrew ${amount:.2f} from account {account.getAccountNumber()}.")
                                print(f"New balance: ${account.getBalance():.2f}")
                                print("===================================")
                            else:
                                print("Withdrawal failed.")
                                print("===================================")
                        except ValueError:
                            print("Invalid amount. Please enter a valid number.")
                            print("===================================")
                    else:
                        print("Account not found.")
                        print("===================================")

                case 8:
                    # Deposit change
                    print("===Deposit Change===")
                    account = bankManager.promptForAccountNumberAndPIN(bank)
                    print("===================================")
                    if account:
                        print("P = Pennies, N = Nickels, D = Dimes, Q = Quarters, H = Half Dollars, W = Whole Dollars")
                        print("Coins format example -> PNNDDQQHHWW")
                        coins = input("Enter coins (P, N, D, Q, H, W): ").upper()
                        valid_coins = {'P', 'N', 'D', 'Q', 'H', 'W'}
                        invalid_found = False
                        for coin in coins:
                            if coin not in valid_coins:
                                print(f"Invalid coin: {coin}")
                                invalid_found = True
                        if invalid_found:
                            print("Invalid coins found. Please try again.")
                            continue
                        total_cents = CoinCollector.parseChange(coins)
                        dollars = total_cents / 100
                        try:
                            if dollars <= 0:
                                print("No valid coins entered. Please try again.")
                                continue
                                
                            if account.deposit(dollars):
                                print(f"${dollars:.2f} in coins deposited into account {account.getAccountNumber()}.")
                                print(f"New balance: ${account.getBalance():.2f}")
                                print("===================================")

                            else:
                                print("Deposit failed.")
                            print("===================================")
                        except ValueError:
                            print("Invalid amount. Please enter a valid number.")
                            print("===================================")
                    else:
                        print("Account not found.")
                        print("===================================")

                case 9:
                    # Close an account
                    print("===Close Account===")
                    account = bankManager.promptForAccountNumberAndPIN(bank)
                    print("===================================")

                    if account:
                        if account.getBalance() > 0:
                            print("Account has a positive balance. Cannot close account. PLEASE WITHDRAW OR TRANSFER FUNDS FIRST.")
                            print("===================================")
                            continue
                        if bank.removeAccountFromBank(account):
                            print(f"Account {account.getAccountNumber()} closed successfully.")
                            print("===================================")
                        else:
                            print("Failed to close account.")
                            print("===================================")
                    else:
                        print("Account not found.")
                        print("===================================")
                case 10:
                    # Add monthly interest to all accounts
                    print("===Add Monthly Interest===")
                    percent = float(input("Enter interest percentage: "))

                    #if you have no accounts, you cannot add interest try again
                    if len(bank.accounts) == 0:
                        print("No accounts found. Cannot add interest.")
                        print("===================================")
                        continue
                 
                    if percent > 0:
                        bank.addMonthlyInterest(percent)
                        print(f"Added {percent}% interest to all accounts.")
                        for account in bank.accounts:
                            print(f"Deposited interest: ${account.getBalance() * (percent / 100 / 12):.2f} into account {account.getAccountNumber()}, new balance: ${account.getBalance():.2f}")
                            print("===================================")
                    else:
                        print("Invalid interest percentage.")
                        print("===================================")
                case 11:
                    print("Exiting the program.")
                    print("===================================")
                    break
                case _:
                    print("Invalid option. Please try again.")
                    print("===================================")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()