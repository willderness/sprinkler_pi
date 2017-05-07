from flask import Flask,request
import tasks 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/zone/<int:zone>', methods=['POST', 'GET'])
def zone_x(zone): 
    print(zone)
    if zone > 0 and zone <= 3:
        tasks.water_zone_now.delay(zone, 600)
    return "OK"

