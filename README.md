# Contact Program Chapter 6
Riley Ternes, Liam Dowell, Braxton Hartley
## Contact Program Description
The program will store the name, street adress, phone number, and email address of a person. It will be able to add contacts, search for a certain contacts info, edit that contacts info, delete a contact, and to display all of the contacts, along with an exit.
### Contact Program Flowchart
```mermaid
graph TD;
  Main-->Add_Contact;
  Main-->Search_Contact;
  Main-->Edit_Contact;
  Main-->Delete_Contact;
  Main-->Display_All_Contacts;
```
#### Function Diagrams
| `Main`    |               | Liam Dowell     |
| ------------------ | ------------- | ------------ |
| `Recieves no arguements`    | runs all of the programs such as menu, search, add, delete, and modify.  |  it outputs a thank you message            |

***
| `Menu`    |               |  Liam Dowell     |
| ------------------ | ------------- | ------------ |
| recieves no arguements    | takes input from the user for the program they want to run |   it outputs the choices you can choose from         |

***
| `Add`    |               |  Riley Ternes     |
| ------------------ | ------------- | ------------ |
| `recieves no arguments`    | takes input from the user for name, street address, phone number, and email address|
| `time:integer`     | writes the contact information to contact.txt |  outputs, "The contact information has been written. |
***
| `Search`    |               |  Braxton Hartley     |
| ------------------ | ------------- | ------------ |
| `argument: 1 input`    | takes input from the user for the contacts information that needs to be found  |   Will output the desired names info           |
***
| `Edit`    |               |  Riley Ternes      |
| ------------------ | ------------- | ------------ |
| `recieves no arguments`    | takes input from the user and changes the contacts information  |   outputs, "The contact information has been written.         |

***

| `Delete`    |               |  Braxton Hartley     |
| ------------------ | ------------- | ------------ |
| `argument: `    | takes input from the user for The name that they wish to be deleted  |   It will delete the desired one           |

***
| `Display`    |               |  Liam Dowell    |
| ------------------ | ------------- | ------------ |
| it recieves no arguements    | it takes no inputs  |  it outputs all of the contacts stored            |

***
