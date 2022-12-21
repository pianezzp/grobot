#!/usr/bin/python  
  
import sqlite3  

def initdb():
    conn = sqlite3.connect('grobo_system.db')  
    print ("Opened database successfully")  
      
    conn.execute('''CREATE TABLE Power 
           (ID INT PRIMARY KEY NOT NULL, 
           DATE INT NOT NULL, 
           CURRENT INT NOT NULL, 
           POWER INT NOT NULL)''')  
    print ("Table created successfully")  
      
    conn.close()  
