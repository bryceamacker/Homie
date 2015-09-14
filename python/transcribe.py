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