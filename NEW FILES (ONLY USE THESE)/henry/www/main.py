import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
print("WORKED")
def talk():
	ser.write(b'1')
try:
	talk()
finally:
	ser.close()

		
