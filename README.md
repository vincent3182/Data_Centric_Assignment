# Data_Centric_Assignment 2025
Vincent Mikalauskas
Student Number:C24498082

# ScreenShot of Main GUI Window
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/99007875-e24d-45a0-bcc3-c97118f9d3a9" />

# Screenshot of Parsing
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/402b615f-7d13-48d4-b77d-9317a69a1614" />


# Screen shot of Search features
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/8cc1237f-6506-4050-b657-95e20d69e810" />


# Description of the project 
For this assignment, I created an application in python that works with a collection of ABC music notation files and stores the extracted information in a MySQL database. My project includes a Tkinter graphical user interface that allows users to interact with the data in a more user-friendly way.

TheApp searches through folders containing .abc files , reads them, parses each tune and extracts details like :

Tune index, Book Number, Tune ID, Title, Alternative title, Tune type, Key signature

All parsed Tunes are then put into a MySQL database table. 
The GUI provides buttons and text inputs for users to :
  Load and parse ABC Files
  Search tunes by title 
  Search tunes by tune type 
  Search tunes by book number 

# instructions for use

#Set up Database - install and run MySQL
create a database "abc_books"
create table with tthe following columns :
      id, book_number, tune_id, title, alt_title, tune_type, key_signature, notation.

# Prep ABC Files
ensure folder is named abc_books- subfolders should be named with their book number 

# To run program 
    open script - must have mysql.connector , sqlalchemy, pandas , tkinter , os 
    run the User_interface.py file
    TKinter window will open automatically

# List of Files in the Project
abc_books/ |Folder containing abc files
images/  | Screenshots used in README
abctoDB.py  |reads parses and sends data to sql database
DbToDf.py  |  connects to DB , runs sql queries for searchcs
User_Interface.py  | simple UI for user to conduct searches

# References
| File Loading & Parsing  | [Website](https://realpython.com/read-write-files-python/) |
|File Loading & Parsing | [Youtube](https://www.youtube.com/watch?v=GWBWQnWNWBI)|
|TKinter GUI |  [Youtube](https://www.youtube.com/watch?v=0CXQ3bbBLVk)|
|Pandas SQL Reading |[Youtube](https://www.youtube.com/watch?v=DiQ5Hni6oRI)|[Youtube](https://www.youtube.com/watch?v=OjMDXTlVOYU)|

# What i am most proud of in this assignment
i am proud of turning the project into a working GUI app and getting the abc parser and database to work together. Having a clean GUI with Tkinter rather than a basic terminal was a great achievement for me.

# What I learned
i learned how to parse scructured .abc files into a MySQL database and have a simple GUI with Tkinter. This project helped me understand how different parts of an program bind together to make a full application.




>>>>>>> 353c211a23dba558be74420e556487c25535405b

