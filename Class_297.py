from flask import Flask, render_template

from paho.mqtt import client as mqtt_client

app = Flask(__name__)
broker='broker.emqx.io'
port=1883
topic="topicName/iot"




client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client
#Define the first page of the web application
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/main', methods=['POST'])
def main():
    return render_template('main.html')

@app.route('/1', methods=['POST'])
def release():
    release_test()
    return render_template('1.html')
def release_test():
    client = connect_mqtt()
    client.loop_start()

@app.route('/2', methods=['POST'])
def engine():
    engine_test()
    return render_template('3.html')
def engine_test():
    client = connect_mqtt()
    client.loop_start()

@app.route('/3', methods=['POST'])
def hydrogen():
    hydrogen_test()
    return render_template('3.html')
def hydrogen_test():
    client = connect_mqtt()
    client.loop_start()

@app.route('/4', methods=['POST'])
def engineign():
    engineign_test()
    return render_template('4.html')
def engineign_test():
    client = connect_mqtt()
    client.loop_start()

@app.route('/5', methods=['POST'])
def hydventarm():
    hydventarm_test()
    return render_template('5.html')
def hydventarm_test():
    client = connect_mqtt()
    client.loop_start()

@app.route('/6', methods=['POST'])
def srbign():
    srbign_test()
    return render_template('6.html')
def srbign_test():
    client = connect_mqtt()
    client.loop_start()
if __name__ == "__main__":
    app.run(port=5001)

#Define the button page of the web application

#Define the Release Orbital Arm button and connect with MQTT server

#Define the Main Engine Test button and connect with MQTT server

#Define the Activate Hydrogen button and connect with MQTT server

#Define the Main Engine Ignite button and connect with MQTT server

#Define the Hydrogen Vent Arm button and connect with MQTT server

#Define the Ignite both SRB's button and connect with MQTT server

if __name__ == "__main__":
    app.run(port=5001)





