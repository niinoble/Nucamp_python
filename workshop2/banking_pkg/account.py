def show_balance(balance):
    balance = float(balance)
    return balance


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance = amount + balance
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    balance = balance - amount

    return balance


def logout(name):
    print("Goodbye", name + "!")
