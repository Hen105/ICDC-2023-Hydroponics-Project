from flask import Flask
app = Flask(__name__)

@app.route('/water-plants', methods=['GET'])
def water_plants():
    # Add your plant watering logic here
    print("Watering plants!")
    return 'Plants watered!'

if __name__ == '__main__':
    app.run(host='192.168.7.193', port=8080)