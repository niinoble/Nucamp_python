def login(database, username,password):
    
    if username not in database:
        print("User not found. Please register.")
        return ""
       
    elif database[username] == password:
        return username
    else:
        print("Incorrect password for ",username)
        return ""
   
def register(database, username):
    if username in database.keys():
        print("The Username",username, "is already registered.")
        return ""
    else:
        print("Username",username,"has been registered!")
        password = input("Please enter a password: ")
        database[username] = password
        print("Congratulations",username+". You're registered")
        return database

def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation = username," donated $"+ str(donation_amt)
    return donation

def show_donations(donations):
    print("\n     --- All Donations ---")
    if donations == []:
        print("Currently, there are no donations")
    else:
        for list in donations:
            print(list)