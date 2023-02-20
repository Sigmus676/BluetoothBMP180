# BluetoothBMP180
A simple python script that sends data from a BMP180 to a Bluetooth device  
In order to run this python file, the Smbus and Pybluez packages need to be installed using these commands:

1. sudo apt-get install python-smbus
2. sudo apt-get install libbluetooth-dev
3. sudo apt-get install python-dev
4. sudo pip install PyBluez

Utilizes the Pybluez library and the Smbus library, which is then converetd into variable data used from another python file which is imported as a module. The file can be fetched from the BMP180 Sensor folder from the Kitflix Repo : https://github.com/kitflix/raspberrypi-iot-codes/tree/master/BMP180%20Sensor.

Ensure you have the 'bmpsensor.py' file in the same folder as the BluetoothBMP180 python file.
