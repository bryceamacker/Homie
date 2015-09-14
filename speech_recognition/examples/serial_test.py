import serial
import time

object_dictionary = ["lights", "lamp", "socket", "tv"]
command_dictionary = ["on", "off"]
print("Starting Serial")
ser = serial.Serial("COM5", 9600)
start = ser.read()
print(start)
while ser.read() is None:
	continue
ser.write("H")

# ser.close()
print("Sent H")

while ser.read() == "Recieved":
	ser.read()

time.sleep(5)
ser.close()