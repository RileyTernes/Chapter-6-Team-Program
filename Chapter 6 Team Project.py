#Chapter 6 Team Project

def main():
    #main recieves no arguements
    #runs all of the programs 
    #outputs a thank you message
    choice = int(menu())

    while choice < 1 and choice > 5:
        print("Invalid response")
    while choice != 6:
        if choice == 1:
            add()
        if choice == 2:
            search()
        if choice == 3:
            edit()
        if choice == 4:
            delete()
        if choice == 5:
            display()
        choice = int(menu())
    print("Have a good day.")

def menu():
    #menu recieves no arguements
    #displays all of the options
    #returns choice

    print("Hello")
    print("1) Add a contact")
    print("2) Search a contact")
    print("3) Edit a contact")
    print("4) Delete a contact")
    print("5) Display all contacts")
    print("6) Exit")

    choice = int(input("Select and option: "))

    return choice


def add():
    #opens file
    #takes input for contact information
    #writes it to contact.txt
    #outputs a confirmation message
    #closes file
    
    
def edit():
    #opens file
    #takes

def delete():

    
def display():