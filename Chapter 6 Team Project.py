#Chapter 6 Team Project
import os
<<<<<<< HEAD
=======

>>>>>>> a9682b216da9c205b562a09456b53b846f17687c
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
<<<<<<< HEAD
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
=======

def search():
    #Opens file
    #searches for name that is asked for
    #prints the values of the associated name
    #closes the file
    
>>>>>>> a9682b216da9c205b562a09456b53b846f17687c
def edit():
    #opens file
    #takes

def delete():

    
def display():