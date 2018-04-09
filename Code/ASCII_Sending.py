# This script will allow to or more BBC
# Microbits to transmit data. This is the
# sending part of the system so it will 
# send data.

from microbit import *
import radio

commands = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
selection = 0

while True:
	if button_a.is_pressed():
		if selection >= 15 :
			selection = 0
		else:
			selection = selection + 1
		display.show(commands[selection])
		sleep(250)
	if button_b.is_pressed():
		radio.send(commands[selection])
		display.scroll('Sent')
		sleep(500)