import tkinter as tk 
from tkinter import ttk
import DbToDf as db

def homepage(): #home page
    global home  # visible outside this funct
    home = tk.Tk()  # main homepage window
    home.title("ABC Music")  # window title
    home.configure(bg = "black")
    
    home.geometry("600x500")  # Set window size (width x height)

    tk.Label(home, text="Home Page", font=("Science Gothic", 20)).pack(pady=1)#title label
    
    
    tk.Button(home, text="Search by Title", command=open_title_search, width=20, height=2).pack(pady=10)    # button opens title search page
    
  
    tk.Button(home, text="Search by Tune Type", command=open_tune_search, width=20, height=2).pack(pady=10)   # button opens tune search page 
    
    home.mainloop()  # Keep the window open 

def open_title_search():
    home.destroy()  # Close the homepage window
    title_search_page()  # Open title search

def open_tune_search():
    home.destroy()  # Close the homepage window
    tune_search_page()  # Open tune search

# titel search
def title_search_page():
    window = tk.Tk()  # new window for title search
    window.title("Search by Title")  # window title
    window.geometry("600x500")  #  window size
    window.configure(bg= "grey") #black backround
    
    tk.Label(window,text = "Title Search",font= ("Calibri" ,20)).pack()

    def search(): #search funct inside titleseaech window

        usersearch = entry.get()  # Get text that user typed
        
        results = db.search_by_title(usersearch)  # Search database by title
        
        text_results.delete(1.0, tk.END)  # Clear previous results

        for index, row in results.iterrows():  # Loop through each row, 
            # display title - tune_type ---------ADD book number later
            displayLine= "Book: " + str(row['book']) + " Title: " + row['title'] + " Tune: "+ row['tune_type'] + "\n" #convert book no to str
            
            text_results.insert(tk.END, displayLine)
    
    #go back funct must be inside the search funct
    def go_back_for_title():
        window.destroy()
        homepage()

    entry = tk.Entry(window, width=40)  #  text entry box
    entry.pack()  # Display the entry box
    
    tk.Button(window, text="Search", command=search).pack()  #  search button calls search()
    
    text_results = tk.Text(window, height=15, width=70)  # text box for results
    text_results.pack()  #text box
    
    # return button that closes this window and returns to homepage
    tk.Button(window, text="Back to Home", command=go_back_for_title).pack(pady=10)
    
    window.mainloop()  # Keep the window open

# search by tunetype
def tune_search_page():
    window = tk.Tk()  #new window for tune type search
    window.title("Search by Tune Type")  #window title
    window.geometry("600x500")  #window size
    window.configure(bg = "grey")

    tk.Label(window,text = "Tune Search",font= ("Calibri" ,20)).pack()


    def search():
        search_term = entry.get()  # reterieve text that user typed in the entry box
        results = db.search_by_tune_type(search_term)  # Search database by tune type


        text_results.delete(1.0, tk.END)  # delete previous results from text box

        for index, row in results.iterrows():  # Loop through each result row
            # Insert each result into the text box (tune_type - title)
            displayLine= "Book: " + str(row['book']) + " Tune: "+ row['tune_type'] + " Title: " + row['title']+ "\n" #convert book no to str
            text_results.insert(tk.END, displayLine)

    def go_back_for_tune():#goback inside corresponding funct
        window.destroy()
        homepage()
    
    entry = tk.Entry(window, width=40)  #text entry box
    entry.pack()  # Display entry box
    
    tk.Button(window, text="Search", command=search).pack()  #search button that calls search()
    
    text_results = tk.Text(window, height=20, width=60)  # text box for results
    text_results.pack()  # Display text
    
    # back button that closes window, returns to homepage
    tk.Button(window, text="Back to Home", command=go_back_for_tune).pack(pady=10) #redirect to homes
    
    window.mainloop()  # Keeps window open

#def go_back_for_title(window):
 #   title_search_page.destroy  # Close title window
  #  homepage()  # Open homepage

#def go_back_for_tune(window):
 #   tune_search_page.destroy  # Close tune window
  #  homepage()  # homepage again

# Start
homepage()  # Launch by opening homepage