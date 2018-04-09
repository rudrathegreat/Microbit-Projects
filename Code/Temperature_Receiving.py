# This program uses Micro-Python, not real Python

from microbit import * 
import radio

radio.config(channel=76)
radio.on()

while True:
	incoming = radio.receive()
	if incoming = None:
		display.show('-')
		pass
	else:
		display.scroll(incoming)
		temperature = incoming
		print(temperature)
		# When it will be transferred to the program, it will then
		# be put back into an integer so that it can be used in Scratch.