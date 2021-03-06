#!flask/bin/python
from flask import Flask
from switch import statusPull, switchLight
import datetime
from config import intervalMinute
app = Flask(__name__)
startMinute = datetime.datetime.now().minute
status = [
    0,
    0,
    0,
    0,
    0
]

initFlag = [0]

@app.route('/homeswitch/status/<int:device_id>', methods=['GET'])
def get_status(device_id):
    #every <intervalMinute> login for polling status while only create new session from 0 to 12 second to reduce multiple sessions
    if initFlag[0] == 0:
        newStatus = statusPull()
        for n in range(2,5):
            status[n] = newStatus[n]
        initFlag[0] = 1
    print str( (datetime.datetime.now().minute - startMinute) % intervalMinute)
    if (datetime.datetime.now().minute - startMinute) % intervalMinute == 0 and datetime.datetime.now().second < 2:
        newStatus = statusPull()
        for n in range(2,5):
            status[n] = newStatus[n]
    return str(status[device_id])

@app.route('/homeswitch/controller/<int:device_id>/<action>', methods=['GET'])
def qurey_action(device_id,action):
    switchLight(device_id,action)
    status[device_id] = 0 if action[1] == "F" else 1
    return str(status[device_id])

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
