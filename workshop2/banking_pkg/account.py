'''
Task 4
-------
Account Functions.


'''

#Show function
def show_balance(balance):
    balance = float(balance)
    return balance

#Deposit Function
def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance = amount + balance
    return balance

#Witdraw Function
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

#Bonus Task 3 (Check withdrawal function)
    while True:
        if amount > balance:
                    print("Where are you going to get that kind of money?")
                    break
        else:
            balance = balance - amount

    return balance

#Logout Function
def logout(name):
    print("Goodbye", name + "!")
