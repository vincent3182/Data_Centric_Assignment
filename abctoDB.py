import os
import mysql.connector #use mysqlconnector to insert data . sqlalchemy to insert to df 

ABC_ROOT = "abc_books"


# CONNECT TO DATABASE
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",    
        database="abc_music"
    )

# PARSE ABC FILES
def parse_abc(path, book):
    
    #Parse an ABC file and return a list of tunes.
    #book, tune_id, title, alt_title, tune_type, key_signature, notation
    
    Tunes = [] #empty list to store everythig
    current_tune = None
    header_done = False #fale unless pass K: -the header

    # Read file lines
    with open(path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    for line in lines: #go line by line
        if line.startswith("X:"):# Start a new tune when goin over X:

            if current_tune:
                Tunes.append(current_tune) #add the tunet to tunes[]

            # 
            current_tune ={
                "book": book[:4],   #book num
                "tune_id": line[2:], #evryting after x:
                "title": "", #T:
                "alt_title": "", #if another t: present
                "tune_type": "", #R:
                "key_signature": "", #k:
                "notation": "" #after k#
            }
            header_done = False  # reset for new tune

        # Main title and alternative titles
        elif line.startswith("T:") and current_tune:
            if current_tune["title"] == "":
                current_tune["title"] = line[2:]
            else:
                current_tune["alt_title"] += line[2:] + "; "

        # Tune type
        elif line.startswith("R:") and current_tune:
            current_tune["tune_type"] = line[2:]

        # Key signature signals the end of header
        elif line.startswith("K:") and current_tune:
            current_tune["key_signature"] = line[2:]
            header_done = True

        # Everything after the key is notation
        elif header_done and current_tune:
            current_tune["notation"] += line + " "

    # Add the last tune in the file
    if current_tune:
        Tunes.append(current_tune)

    return Tunes

# INSERT TUNE

def insert_tune(tunes):
    conn = get_connection()
    cursor = conn.cursor()

    for tune in tunes:
    # have to use string formating.....otherwise injection
        sql = f"""
        INSERT INTO tunes (book, tune_id, title, alt_title, tune_type, key_signature, notation)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            tune['book'],
            tune['tune_id'],
            tune['title'], 
            tune['alt_title'],
            tune['tune_type'], 
            tune['key_signature'], 
            tune['notation']
        ))
            

    conn.commit()
    conn.close()


# LOAD ALL ABC FILES

folders = os.listdir(ABC_ROOT)

def load_all_books():
    for folder in folders:
        folder_path = os.path.join(ABC_ROOT, folder)

        if os.path.isdir(folder_path) and folder.isdigit(): #folder location and has a digit at end 
            print("book number:", folder)#prints out which book is being processed 

            for file in os.listdir(folder_path):
                if file.endswith(".abc"):
                    path = os.path.join(folder_path, file)
                    print(file)
                    Tunes = parse_abc(path, folder)
                    insert_tune(Tunes)

if __name__ == "__main__":
    load_all_books()
    print("Done loading all books!")