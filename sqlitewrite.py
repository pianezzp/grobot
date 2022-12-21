#!/usr/bin/python  
  
import sqlite3
import datetime
from time import sleep,mktime
date_time = datetime.datetime.now()
dt = mktime(date_time.timetuple())
print(dt)
conn = sqlite3.connect('grobo_system.db')  
print ("Opened database successfully") 
connstr=  "INSERT INTO Power (ID,DATE,POWER,CURRENT) VALUES ("+str(4)+","+str(mktime(date_time.timetuple()))+","+str(1)+","+str(1)+")"
conn.execute(connstr);  
  

conn.commit()  
print ("Records inserted successfully")  
conn.close()  