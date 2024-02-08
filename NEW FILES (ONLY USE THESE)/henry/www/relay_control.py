import serial
import time

# Replace 'your_port' with the actual port where Arduino is connected
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def toggle_relay():
    ser.write(b'toggle_relay')

try:
    while True:
        # Your Raspberry Pi code logic goes here
        time.sleep(1)  # Add any additional logic or delay if needed

except KeyboardInterrupt:
    ser.close()
