from flask import Flask, render_template, redirect
import subprocess
app = Flask(__name__)

@app.route('/')
def run_script():
	subprocess.run(["python3", "main.py"])
	return redirect("http://192.168.137.71:8080/")
if __name__ == '__main__':
	app.run(host='192.168.137.71', port=5000, debug=True)
