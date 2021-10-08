from donations_pkg.homepage import show_homepage
from donations_pkg.user import login, register, donate, show_donations
database = {"admin": "password123"}
donations = []
authorized_user = ""


while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print("Logged in as", authorized_user)

    choice = (input("Choose an Option: "))

    print("")
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
        if authorized_user != "":
            print("Welcome back", authorized_user)
    elif choice == "2":
        username = input("Enter username to register: ")
        database = register(database, username)
    elif choice == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
            print("Thank you for your donation!")
    elif choice == "4":
        show_donations(donations)
    elif choice == "5":
        print("Leaving DonateMe...")
        break
    else:
        print("Please enter a valid choice")
