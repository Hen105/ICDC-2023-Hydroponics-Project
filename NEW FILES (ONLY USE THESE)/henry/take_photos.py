import subprocess
import os
from datetime import datetime
from glob import glob
import time

def download_snapshot(url, output_directory, num_snapshots):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Initialize counter
    
    counter = 1

    for _ in range(num_snapshots):
        # Get current date and time
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Form the output file name with the counter and date/time
        output_file = os.path.join(output_directory, f'snapshot_{current_datetime}_{counter}.jpg')

        # Run wget command
        command = f'wget {url} -O {output_file}'
        subprocess.run(command, shell=True)

        print(f'Snapshot downloaded: {output_file}')

        # Increment counter for the next snapshot
        time.sleep (1)
        counter += 1

def create_timelapse(input_directory, output_file, framerate=30):
    # Use glob to get all jpg files in the input directory
    input_files = os.path.join(input_directory, '*.jpg')

    # Run ffmpeg command to create the timelapse video
    command = f'ffmpeg -framerate {framerate} -pattern_type glob -i "{input_files}" -c:v libx264 -pix_fmt yuv420p {output_file}'
    subprocess.run(command, shell=True)

    print(f'Timelapse video created: {output_file}')

if __name__ == "__main__":
    # Specify the URL, output directory, number of snapshots, and timelapse parameters
    snapshot_url = 'http://localhost:8080/?action=snapshot'
    output_directory = 'snapshots'
    num_snapshots = 9999999999

    # Run the snapshot download function
    download_snapshot(snapshot_url, output_directory, num_snapshots)

    # Get current date and time for timelapse video naming
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    timelapse_output_file = f'timelapse_video_{current_datetime}.mp4'
    timelapse_framerate = 1

    # Run the timelapse creation function
    create_timelapse(output_directory, timelapse_output_file, timelapse_framerate)
