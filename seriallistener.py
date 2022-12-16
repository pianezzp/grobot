# decode a uart message sent by arduino nano on PowerManagement Hat from Waveshare

from serial import Serial as aserial
from time import sleep

ser = aserial('/dev/ttyS0',9600 )    #Open port with baud rate

while True:
    received_data = ser.read()              #read serial port
    sleep(.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    try:
        print (received_data.decode())                   #print received data
        ser.write(received_data)
    except:
        print(received_data)
