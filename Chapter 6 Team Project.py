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

def search():
    #Opens file
    #searches for name that is asked for
    #prints the values of the associated name
    #closes the file
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
            #you were copying Mr. hayes code.
    
    
    
    
def edit():
    #opens file
    #takes

def delete():

    
def display():