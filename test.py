import serial
gps = serial.Serial("/dev/ttyACM0" , baudrate = 9600)

print(gps)
