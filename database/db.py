import psycopg2
 
import os

config = dotenv_values(".env")

#  Connect to an existing database
conn = psycopg2.connect(
        host="localhost",
        user="postgre",
        password="thushan2001",
        dbname="python",
        port=5432
    )

    
# error handling
 

# users columns : id (primary key), f_name , l_name , address , mobile , password
# articale  columns : artical_id (primary key), title ,artical_content ,artical_date , id (foreign key from users)
# user_comment columns : comment_id (primary key) , comment_content , c_date , review (bool) ,artical_id(foreign key) ,user_id(foreigen key)

cursor = conn.cursor()

class insert :
     
    # Insert data into table

    # query : INSERT INTO user VALUES (%s,%s,%s,%s,%d,%s)
    # values :  ('FE001', 'kamal', 'perera','Address',0775050880,'password')

    def  insert_data(self, query,values) :
        try :
            cursor.execute(query,values)
            conn.commit()
            return "inserted successfully."
        except Exception as e:
            return ""
        
# retrive data for the database : query is SQL query

class retrive :
    
    def select_data(self,query):
        try :
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except  Exception as e:
            return 'error'
        

# delete from data for the database
class delete :
   
    def delete_data(self,query):    
        try :
            cursor.execute(query)
            conn.commit()
            return "deleted Successfully"
        except Exception as e:
            return "error"
        
# create table
class create :
    def create_table(self,query):
        try :
            cursor.execute(query)
            return "create a table sucessfully"
        except Exception as e:
            return f"error"

# update  data into the database

class  update :
    def update_data(self,query):
        try :
            cursor.execute(query)
            conn.commit()
            return "{cursor.rowcount} rows affected."
        except Exception as e:
            return "error"
        

        









