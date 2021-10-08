from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")



print("          === Automated Teller Machine ===          ")
balance = 0

#Bonus Task: Checking for maximum length
while True:
    name = input("Enter name to register: ")
    if len(name) < 10:
        break
    else:
        print("The maximum name length is 10 characters.")

#Bonus Task: Checking for required PIN length
while True:
    pin = (input("Enter PIN: "))
    if len(pin) == 4:
        break
    else:
        print("PIN must contain 4 numbers")


print(name," has been registered with a starting balance of $"+str(0),"\n")


while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    
    name_to_validate = input("Enter name to login: ")
    pin_to_validate = (input("Enter PIN: "))
    if name_to_validate == name and pin_to_validate ==pin:
        
        print("Login successful! \n")
        break
    else:
        print("Invalid credentials! \n")

#Task 5 Using Banking Package: ATM Menu Options
while True:
        atm_menu(name)
        option = input("Chooose an option:")
        if option =="1":
            
           account.show_balance(balance)
            
            
        elif option =="2":
            balance = account.deposit(balance)
           
            
        elif option =="3":
            balance = account.withdraw(balance)
            

            

        else:
            account.logout(name)
            break

        print("Current Balance: $"+str(balance)+ "\n")