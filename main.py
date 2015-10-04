#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import socket


UDP_IP = "192.168.1.250"
UDP_PORT = 5683

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

def sendUDP(ip, port, message):
	sock.sendto(message, (ip, port))

def receiveUPD(port = UDP_PORT):
	sock = socket.socket(socket.AF_INET, # Internet
	                     socket.SOCK_DGRAM) # UDP
	try:
		sock.bind(("", UDP_PORT))
	except socket.error:
		print("Caught")

	while True:
	    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	    print "received message:", data
	    break

def transcribe():
	r = sr.Recognizer()
	trans = []
	with sr.Microphone() as source:
	    r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
	    print("Say something!")
	    audio = r.listen(source)

	# recognize speech using Google Speech Recognition
	print("Done recording")
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    trans = r.recognize_google(audio)
	    print("Google Speech Recognition thinks you said " + trans)
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError:
	    print("Could not request results from Google Speech Recognition service")

	recieved = trans.split(" ")
	recieved = map(lambda each:each.strip("u'"), recieved)
	return recieved

object_dictionary = ["lights", "light", "lamp", "socket", "tv"]
command_dictionary = ["on", "off"]

for i in range(0, 5):
	# obtain audio from the microphone
	#recieved = transcribe()
	# for i in range(0, 2):
	recieved = ["turn", "off", "lights"]

	active_object = ""
	active_command = ""

	for word in recieved:
	    if word in object_dictionary:
	        active_object = word
	        break

	for word in recieved:
	    if word in command_dictionary:
	        active_command = word
	        break

	print("Command: " + active_object + " " + active_command)
	if (active_object == "lights" or active_object == "light"):
		if (active_command == "on"):
			sendUDP(UDP_IP, UDP_PORT, "H")
			receiveUPD()
		if (active_command == "off"):
			sendUDP(UDP_IP, UDP_PORT, "L")
			receiveUPD()
