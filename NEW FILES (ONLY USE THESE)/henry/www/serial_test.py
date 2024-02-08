#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import os
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
while True:
    if ser.in_waiting > 0:
        lin = ser.readline().decode('utf-8').rstrip()
        line=lin
            
            
        # Your Python variable
        Sensor_reading = "Sensor Reading=  " + line
        if line >= "6":
            relay = "Relay Status: Off"
        elif line <= "6":
            relay = "Relay Status: On"
        

        # Configure Jinja2 environment

        template_dir = os.path.dirname(os.path.abspath(__file__))  # assuming script and template are in the same directory

        env = Environment(loader=FileSystemLoader(template_dir))

        # Load the template

        template = env.get_template('template.html')

        # Render the template with your data

        rendered_html = template.render(p={'first_header': Sensor_reading})
        tworendered_html = template.render(p={'two_header': relay})

        # Save the rendered HTML to a file

        output_file_path = '/usr/local/share/mjpg-streamer/www/output.html'

        with open(output_file_path, 'w') as output_file:

            output_file.write(rendered_html + tworendered_html)

        print(f"File '{output_file_path}' created successfully.")
        print(Sensor_reading)
        print(relay)
        

        time.sleep(1)
