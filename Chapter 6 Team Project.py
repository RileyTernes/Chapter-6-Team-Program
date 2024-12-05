#Chapter 6 Team Project
import os
def main():
    #calls menu to get choice
    #calls function according to choice

def menu():
    #displays menu
    #returns choice
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
<<<<<<< Updated upstream
=======
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
>>>>>>> Stashed changes
    
def edit():
    #opens file
    #takes

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
        