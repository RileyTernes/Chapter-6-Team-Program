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
    
def edit():
    #opens file
    #takes

def delete():

    
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
        