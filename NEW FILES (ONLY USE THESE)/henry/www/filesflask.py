from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
# Specify the directory path you want to serve
DIRECTORY_PATH = '/home/pi/Desktop'

# Define the main function to run the server
def run_server():
    try:
        # Set up the HTTP server
        server_address = ('192.168.137.79', 8000)  # Change IP and port if needed
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

        # Change the current working directory to the specified directory
        os.chdir(DIRECTORY_PATH)

        # Print a message indicating that the server is running
        print(f"Server is running at http://{server_address[0]}:{server_address[1]}/")

        # Start the HTTP server
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Stop the server if the user interrupts with Ctrl+C
        httpd.server_close()
        print("\nServer stopped.")

if __name__ == '__main__':
    run_server()
