#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import serial
import speech_recognition as sr

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
ser = serial.Serial("COM5", 9600)

for i in range(0, 5):
	# obtain audio from the microphone
	recieved = transcribe()
	# for i in range(0, 2):


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
			ser.write("H")
		if (active_command == "off"):
			ser.write("L")


# while True:
# 	continue

