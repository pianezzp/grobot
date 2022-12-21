# decode a uart message sent by arduino nano on PowerManagement Hat from Waveshare
# Raspberry Pi and Arduino are linked through internal serial port through level shifter

from serial import Serial as aserial
from time import sleep,mktime
import datetime
import sqlite3
from sqlite3 import Error


            
conn = sqlite3.connect('grobo_system.db')  
print ("Opened database successfully")
    



ser = aserial('/dev/ttyS0',9600 )    #Open port with baud rate


while True:
    x=6
    date_time = datetime.datetime.now()   
    received_data = ser.read()              #read serial port
    sleep(.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    try:
        print (received_data.decode()) #print received data
        sql_insert=  "INSERT INTO Power (DATE,POWER,CURRENT) VALUES ("+str(mktime(date_time.timetuple()))+","+str(received_data.decode().splitlines()[1])+","+str(received_data.decode().splitlines()[0])+")"
        conn.execute(sql_insert);  
        conn.commit()
        ser.write(received_data)
        x=+1
    except:
        print(received_data)
