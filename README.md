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
| `Main`    |               |  author     |
| ------------------ | ------------- | ------------ |
| `argument:type`    | takes input from the user for ____  |              |
| `time:integer`     | calculates ______  | outputs ____             |
| `name:string`      | takes input for name ___ | returns total |
***
| `Menu`    |               |  author     |
| ------------------ | ------------- | ------------ |
| `argument:type`    | takes input from the user for ____  |              |
| `time:integer`     | calculates ______  | outputs ____             |
| `name:string`      | takes input for name ___ | returns total |
***
| `Add`    |               |  Riley Ternes     |
| ------------------ | ------------- | ------------ |
| `recieves no arguments`    | takes input from the user for name, street address, phone number, and email address|
| `time:integer`     | writes the contact information to contact.txt |  outputs, "The contact information has been written. |
***
| `Search`    |               |  author     |
| ------------------ | ------------- | ------------ |
| `argument:type`    | takes input from the user for ____  |              |
| `time:integer`     | calculates ______  | outputs ____             |
| `name:string`      | takes input for name ___ | returns total |
***
| `Edit`    |               |  Riley Ternes     |
| ------------------ | ------------- | ------------ |
| `recieves no arguments`    | takes input from the user for the contact information it would like to edit|              |
|      | edits the contact information to be the contact information given by the user |
|       | writes it to contact.txt |
***
| `Delete`    |               |  author    |
| ------------------ | ------------- | ------------ |
| `recieves no arguments`    | takes input from the user for ____  |              |
| `time:integer`     | calculates ______  | outputs ____             |
| `name:string`      | takes input for name ___ | returns total |
***
| `Display`    |               |  author     |
| ------------------ | ------------- | ------------ |
| `argument:type`    | takes input from the user for ____  |              |
| `time:integer`     | calculates ______  | outputs ____             |
| `name:string`      | takes input for name ___ | returns total |
***
