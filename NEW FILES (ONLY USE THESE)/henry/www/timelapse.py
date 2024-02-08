
import cv2
import requests
import numpy as np
import time
from io import BytesIO

# MJPEG stream URL
mjpeg_url = "http://192.168.137.71:8080"

# Output folder for saving frames
output_folder = "/home/pi/Desktop/timelapse"

# Time interval between capturing frames (in seconds)
capture_interval = 10

# Number of frames to capture
num_frames = 100

def capture_frame():
	try:
		response = requests.get(mjpeg_url, stream=True, timeout=5)
		if response.status_code == 200:
			byte_data = b""
		for chunk in response.iter_content(chunk_size=1024):
			byte_data += chunk
			a = byte_data.find(b'\xff\xd8')
			b = byte_data.find(b'\xff\xd9')
			if a != -1 and b != -1:
				jpg_data = byte_data[a:b + 2]
				byte_data = byte_data[b + 2:]
				frame = cv2.imdecode(np.frombuffer(jpg_data, dtype=np.uint8), cv2.IMREAD_COLOR)
				return frame
	except Exception as e:
		print(f"Error capturing frame: {e}")
	return None

def main():
	for i in range(num_frames):
		frame = capture_frame()
		if frame is not None:
			filename = f"{output_folder}/frame_{i}.jpg"
			cv2.imwrite(filename, frame)
			print(f"Frame {i} captured")
		time.sleep(capture_interval)

if __name__ == "__main__":
	main()


