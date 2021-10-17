class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):  # Changes the name of the User.
        self.name = name
        #print("Your name has been changed to", self.name)

    def change_pin(self, pin):  # Changes the PIN of the User.
        self.pin = pin
        #print("Your pin has been changed to", self.pin)

    def change_password(self, password):  # Changes the password of the User.
        self.pin = password
        #print("Your pin has been changed to", self.password)


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = float(0)

    def show_balance(self):

        print(f"{self.name} has an account balance: of ${self.balance}")

    def withdraw(self, amount):

        if self.balance < amount:
            print("You dont have",  amount, "in your account", self.balance)
            return
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, amount, other_user):
        print(f"You are transferring ${amount} to {other_user.name}")
        print("Authentication required.")

        while True:
            pin = int(input("Enter your PIN: "))
            if pin == self.pin:
                self.balance -= amount
                other_user.balance += amount
                print("Transfer Authorized")
                print(f"Transferring ${amount} to {other_user.name}...")
                return
            else:
                print("Invalid pin. Transaction cancelled!")
                break

    def request_money(self, amount, other_user):
        print(f"You are requesting ${amount} from {other_user.name}")
        print("User authentication required...")
        if other_user.balance < amount:
            print(f"{other_user.name} doesn't have ${amount} in their account")
            return

        while True:
            pin = int(input(f"Enter {other_user.name}'s PIN: "))
            if pin == other_user.pin:
                password = str(input(f"Enter your password: "))
                if password == self.password:
                    self.balance += amount
                    other_user.balance -= amount
                    print("Request Authorized")
                    print(f"Bob sent ${amount}")
                    return
                else:
                    print("Invalid Password Transaction is cancelled")
                    return
            else:
                print("Invalid pin. Transaction cancelled!")
                return

 # Check instation input


def check_value(value):
    if (isinstance(value, (int, float))) != True:
        print("Please use vaild input (Only integers and floats allowed),")

    elif(value < 0):
        print("Please use valid input(Input must be positive)",)

    else:
        return value


'''Driver Code for Task 1'''
# user = User("Bob", 1234,"password")
# print(user.name,user.pin,user.password)

'''Driver Code for Task 2'''

""" user = User("Bob", 1234,"password")
print(user.name,user.pin,user.password)

user.change_name("Bobby")
user.change_pin("4321")
user.change_password("newpassword")
print(user.name,user.pin,user.password) """

""" Driver Code for Task 3"""
# bankuser1 = BankUser("Bob", 3432, "bestpassword")
# print(bankuser1.name,bankuser1.pin,bankuser1.password, bankuser1.balance)

'''Driver Code for Task 4'''
# bankuser1 = BankUser("Bob", 3432, "bestpassword")
# bankuser1.show_balance()
# bankuser1.deposit(-10)
# bankuser1.show_balance()
# bankuser1.withdraw(-500)
# bankuser1.show_balance()

'''Driver Code for Task 5'''

bankuser1 = BankUser("Alice", 1111, "password")
bankuser1.deposit(5000)
bankuser2 = BankUser("Bob", 3432, "bestpassword")
bankuser1.show_balance()
bankuser2.show_balance()
print(" ")
bankuser1.transfer_money(500, bankuser2)
print(" ")
bankuser1.show_balance()
bankuser2.show_balance()
print(" ")
bankuser1.request_money(250, bankuser2)
print(" ")
bankuser1.show_balance()
bankuser2.show_balance()
