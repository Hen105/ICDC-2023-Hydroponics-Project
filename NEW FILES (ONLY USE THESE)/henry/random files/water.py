import serial
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
def send_water_command():
	ser.write(543)
if __name__ == "__main__":
	send_water_command()
	ser.close()
