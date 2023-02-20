import bmpsensor #imports the bmpsensor module created by Matt Hawkins
import time
import bluetooth #imports pybluez moodule created by Albert Huang

address = input('What is the bluetooth address of the device you want to send the data to ?') #Input MAC address to bluetooth device you want to connect to 'XX:XX:XX:XX:XX:XX'

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM) # specifies that RFCOMM(Radio Frequency communication) protocol is being used to sned and receive packets

sock.connect((address, 1)) #'1' specifies what channel is being used, channels upto 79 can be used

while True:
    temp, pressure, altitude = bmpsensor.readBmp180() #fetching and parsing data from the bmp180 sensor
    tempz = ("Current Temp: ",temp)  # degC
    pressurez = ("Current Pressure ",pressure) # Pressure in Pa 
    altitudez = ("Current Altitude ",altitude) # Altitude in meters
    time.sleep(2)

    #data = f'The temperature is {tempz}. The pressure is {pressurez} and the Altitude is {altitudez}.' (It can be formatted as this rather than using .format and .encode to send data)
    data = '{} {} {}'.format(tempz, pressurez, altitudez) #parsing variable data which is converted into a single string
    sock.send(data.encode()) #encodes data as bytes before sending over socket

    sock.close()

    #Repositories used:
    #https://github.com/pybluez/pybluez
    #https://github.com/kitflix/raspberrypi-iot-codes