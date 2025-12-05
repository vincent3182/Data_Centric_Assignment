import os
import pandas as pd 
import sqlalchemy #preferred over sqllite3 and sqlconnector

def get_engine():
    return sqlalchemy.create_engine('mysql+mysqlconnector://root:@localhost/abc_music')

#SqlQuery = "SELECT * FROM tunes"
#df = pd.read_sql(SqlQuery,engine)

#new adiidtions 
def get_all_tunes():
    #Returns a DataFrame with all tunes from the database
    engine = get_engine() #uses the get engine funct
    sqlquery = "SELECT * FROM tunes" #query selects everything , df alters data searches rather than multiple sql queries
    df = pd.read_sql(sqlquery, engine)
    return df

#search by title
def search_by_title(search_term):
    #Search tunes by title
    df = get_all_tunes()
    return df[df['title'].str.contains(search_term, case=False, na=False)]

#search by tune
def search_by_tune_type(search_term):
    #Search tunes by tune type
    df = get_all_tunes()
    return df[df['tune_type'].str.contains(search_term, case=False, na=False)] #make searches not case sensitive , also dont incl null 

#search by tune
def search_by_book_number(search_term):
    #Search tunes by tune type
    df = get_all_tunes()
    return df[df['book']== int(search_term)] #make sure its an integr search


#print(df[['book','title']])