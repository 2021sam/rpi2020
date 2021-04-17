# MQTT Subscriber with Audio (Bluetooth) speaker Alert Notification
# Sam Portillo
# 10/26/2020
#	Notepad++ →	Settings	→	Preferences	→	Languages	→	Tab Settings	→	Python	Use default value


import time, json
import paho.mqtt.client as paho
from subprocess import call

# from playsound import playsound
#playsound('graham_low.wav')

# broker="10.0.0.11"	# Wired
broker="10.0.0.12"	# Wireless
port			= 1883
# user			= "mqtt"
# password		= "z"

contact = ""


#define callback
def on_message(client, userdata, message):
	global contact

	print("Topic " + str( message.topic ))
	d_string = message.payload.decode("utf-8")
	print( type( d_string ) )
	print("received message = ", d_string )
	d = json.loads( d_string )
	print( type( d ) )
	c = d['contact']
	print( c )
	if contact != c:
		contact = c
		call(["aplay", "ebcrosby.wav"])       # Raspberry Pi
		# playsound('graham_low.wav')


client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
# client.username_pw_set( user, password=password)
#####
print("connecting to broker ",broker)
# client.connect( broker_address, port = port )
client.connect(broker)	#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("zigbee2mqtt/Man Cave")	#subscribe
# time.sleep(2)
# print("publishing ")
# client.publish("cool", "Stunt")#publish

while True:
	time.sleep(1)

client.disconnect() #disconnect
client.loop_stop() #stop loop
