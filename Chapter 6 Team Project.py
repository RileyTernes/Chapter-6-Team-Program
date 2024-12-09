#Chapter 6 Team Project
import os

def main():
    #main recieves no arguements
    #runs al of the programs
    #outputs a thank you message
    choice = int(menu())
    
    while choice < 1 or choice > 6:
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

    pass


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


    try:
        enter = 'y'
        while enter.lower() != "n":
            found = False
            search = input("Enter the name of the person that you are looking for: ")
            contact_file = open("contact.txt", 'r')
            name = contact_file.readline()
            while name != '':
                street = contact_file.readline()
                phone = contact_file.readline()
                email = contact_file.readline()
                name = name.rstrip("\n")
                
                if name.lower() == search.lower():
                    print("\n---Record found!---")
                    print(f"Name: {name}")
                    print(f"Street Address: {street}")
                    print(f"Phone Number: {phone}")
                    print(f"Email Address: {email}")
                    found = True
                    enter = input("Would you like to continue? (y/n) ")
                    break
                name = contact_file.readline()
            contact_file.close()
            if not found:
                print("Record not found")
                enter = input("Would you like to continue? (y/n) ")
    except Exception as err:
        print(err)
    
def edit():
    #edit recieves no arguements 
    #opens file
    found = False
    
    search = input("Enter the name to modify: ")
    new_street = input("Enter the new street address: ")
    new_phone = input("Enter the new phone number: ")
    new_email = input("Enter the new email address: ")
    
    contact_file = open('contact.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    name = contact_file.readline()
    while name != '':
        street = contact_file.readline()
        phone = contact_file.readline()
        email = contact_file.readline()
        name = name.rstrip('\n')
        street = street.rstrip('\n')
        phone = phone.rstrip('\n')
        email = email.rstrip('\n')
        if search.lower() == name.lower():
            temp_file.write(name + '\n')
            temp_file.write(new_street + '\n')
            temp_file.write(new_phone + '\n')
            temp_file.write(new_email + '\n')
            found = True
            break
        else:
            temp_file.write(name + '\n')
            temp_file.write(street + '\n')
            temp_file.write(phone + '\n')
            temp_file.write(email + '\n')
            
        name = contact_file.readline()
        
    contact_file.close()
    temp_file.close()
    
    os.remove('contact.txt')
    os.rename('temp.txt', 'contact.txt')
    
    if found == False:
        print("\nRecord not found.")
    else:
        print(f"The contacts for {search} has been updated.")
    
def delete():

    try:
        enter = 'y'
        while enter.lower() != "n":
            found = False
            search = input("Please enter the name of the person's record you wish to delete: ")
            contact_file = open("contact.txt", "r")
            temp_file = open("temp.txt", "w")
            name = contact_file.readline()
            while name != '':
                street = contact_file.readline()
                phone = contact_file.readline()
                email = contact_file.readline()
                
                name = name.rstrip("\n")
                street = street.rstrip('\n')
                phone = phone.rstrip('\n')
                email = email.rstrip('\n')
                
                if search.lower() != name.lower():
                    temp_file.write(name + '\n')
                    temp_file.write(street + '\n')
                    temp_file.write(phone + '\n')
                    temp_file.write(email + '\n')
                else:
                    found = True
                name = contact_file.readline()
            contact_file.close()
            temp_file.close()
            
            os.remove("contact.txt")
            os.rename("temp.txt", "contact.txt")
            
            if not found:
                print("Record not found.")
                enter = input("Would you like to continue? (y/n) ")
            else:
                print(f"{search} had been deleted from coffee.txt")
                enter = input("Would you like to continue? (y/n) ")
    except Exception as err:
        print(err)
    
def display():
    #display recieves no arguements
    #it displays all of the contacts
    
    if os.path.exists("contact.txt"):
        contact_file = open('contact.txt', 'r')
    else:
        print("file not found")
        print("\n")
        return
    name = contact_file.readline()
    
    while name != '':
        street = contact_file.readline()
        phone = contact_file.readline()
        email = contact_file.readline()
        name = name.rstrip('\n')
        street = street.rstrip('\n')
        phone = phone.rstrip('\n')
        email = email.rstrip('\n')
        print("----------------------------")
        print(f"Name: {name}")
        print(f"Street Address: {street}")
        print(f"Phone Number: {phone}")
        print(f"Email Address: {email}")
        name = contact_file.readline()
    print("----------------------------")
    contact_file.close()
    print("\nAll records retrieved.")
<<<<<<< HEAD
        

=======
main()
>>>>>>> 4b79edf1dc37cda6984c98dbf1e959b56bc7a8fa
