#Chapter 6 Team Project
import os

def main():
    #calls menu to get choice
    #calls function according to choice
    pass
def menu():
    #displays menu
    #returns choice
    pass
def add():
    #opens file
    #takes input for contact information
    #writes it to contact.txt
    #outputs a confirmation message
    #closes file
    choice = 'y'
    infile = open("contact.txt", "a")
    while choice.lower() == 'y':
        print("Enter the contact information:\n")
        #get input
        name = input("Name: ")
        street_address = input("Street address: ")
        phone_number = input("Phone number: ")
        email_address = input("Email address: ")
        #write it to the text
        infile.write(name + '\n')
        infile.write(street_address + '\n')
        infile.write(phone_number + '\n')
        infile.write(email_address + '\n')
        choice = input("\nDo you wish to enter another contacts information? (y to continue): ")
    #close file
    infile.close()
    #confirm that it's written
    print("\nAll data appended to coffee.txt.")

def search():
    #Opens file
    #searches for name that is asked for
    #prints the values of the associated name
    #closes the file
    pass
def edit():
    #opens file
    #takes
    name = 'test'
    street_address = 'test'
    phone_adrress = 'test'
    email_address = 'test'
    
    contact_file = open('contact.txt', 'r')
    name = contact_file.readline
    street_address = 'test'
    phone_adrress = 'test'
    email_address = 'test'
    
    option = 0
    found = False
    search = input("Enter the name of the current contact: ")
    while option != 1 or 2 or 3:
        print("Here are your options:\n")
        print("Edit a street address(1)")
        print("Edit a phone number(2)")
        print("Edit a email address(3)")
        option = int(input("What option do you want to choose? "))
        if option != 1 or 2 or 3:
            print("That is not a valid option. Please try again.")
    
    
    temp_file = open('temp.txt', 'w')
    name = contact_file.readline()
    
    while name != '':
        #while there is a name
        if option == 1:
            #get new street address
            new_street_address = input("Enter the new street address: ")
            
            street_address = contact_file.readline()
            name = name.rstrip('\n')
            street_address = street_address.rstrip('\n')
            phone_number = phone_number.rstrip('/n')
            email_address = email_address.rstrip('/n')
            if search.lower() == name.lower():
                temp_file.write(name + '\n')
                temp_file.write(new_street_address + '\n')
                temp_file.write(phone_number + '/n')
                temp_file.write(email_address + '/n')
                found = True
            else:
                temp_file.write(name + '\n')
                temp_file.write(street_address + '\n')
                temp_file.write(phone_number + '/n')
                temp_file.write(email_address + '/n')
            name = contact_file.readline()
            
            
        elif option == 2:
            new_phone_number = input("Enter the new phone number: ")
            
            phone_number = contact_file.readline()
            name = name.rstrip('\n')
            street_address = street_address.rstrip('\n')
            phone_number = phone_number.rstrip('\n')
            email_address = email_address.rstrip('\n')
            
            if search.lower() == name.lower():
                temp_file.write(name + '\n')
                temp_file.write(new_phone_number + '\n')
                found = True
            else:
                temp_file.write(desc + '\n')
                temp_file.write(qty + '\n')
            desc = coffee_file.readline()
        elif option == 3:
             = contact_file.readline()
            desc = desc.rstrip('\n')
            qty = qty.rstrip('\n')
            
            if search.lower() == name.lower():
                temp_file.write(desc + '\n')
                temp_file.write(new_qty + '\n')
                found = True
            else:
                temp_file.write(desc + '\n')
                temp_file.write(qty + '\n')
            desc = coffee_file.readline()
    coffee_file.close()
    temp_file.close()
    os.remove('coffee.txt')
    os.rename('temp.txt', 'coffee.txt')
    
    if found == False:
        print("\nRecord not found.")
    else:
        print("The quantity for", search, "has been updated to", new_qty, "pounds.")
    
    if search.lower() != desc.lower():
        temp_file.write(desc + '\n')
        temp_file.write(qty + '\n')
    else:
        found = True
def delete():
    pass
def display():
    pass