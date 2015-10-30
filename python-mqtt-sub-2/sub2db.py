# -*- coding: utf-8 -*- 

import paho.mqtt.client as mqtt
import com_sensor

#
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe(topic="censors/temperature")
	client.subscribe(topic="item/#")

#
def on_message(client, userdata, msg):
	clsSen= com_sensor.sensorClass()
	print("on_message:topic=" + msg.topic+" ,pay="+str(msg.payload))
	clsSen.saveSensor( msg.topic, str(msg.payload))

if __name__ == "__main__":
#client = mqtt.Client()
    client = mqtt.Client(client_id="spam")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host="192.168.1.24", port=1883)
    client.loop_forever()
#client.connect(host="localhost", port=1883)

 

