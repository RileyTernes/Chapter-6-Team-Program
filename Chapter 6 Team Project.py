#Chapter 6 Team Project

def main():
    choice = int(menu())
    
    while choice < 1 or choice > 5:
        print("INVALID")
        choice = int(menu())
    
    while choice != 6:
        if choice == 1:
            add()
        elif choice == 2:
            search()
        elif choice == 3:
            edit()
        elif choice == 4:
            delete()
        elif choice == 5:
            display()
        choice = int(menu())
    print("Have a good day!")
    
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

    choice = int(input("Select an option: "))

    return choice


def add():
    #opens file
    #takes input for contact information
    #writes it to contact.txt
    #outputs a confirmation message
    #closes file
    print('1')
    
def search():
    print('5')
    
    
def edit():
    #opens file
    #takes
    print('2')

def delete():
    print('3')
    
def display():
    print('4')