# This program will allow two or more BBC
# Microbit to transmit information
# This is the receiving end of the 
# transmitting system.

from microbit import *
import radio

def stop():
	pin8.write_digital(0)
	pin12.write_digital(0)
	pin0.write_digital(0)
	pin16.write_digital(0)

def move(time, state):
	if state == 1:
		pin8.write_digital(state)
		pin12.write_digital(0)
		pin0.write_digital(state)
		pin16.write_digital(0)
		sleep(time)
		stop()
	if state == 0:
		pin8.write_digital(state)
		pin12.write_digital(1)
		pin0.write_digital(state)
		pin16.write_digital(1)
		sleep(time)
		stop()

while True:
	
	incoming = radio.receive()
	
	if incoming == None:
		pass
	if incoming == 'F':
		display.show(incoming)
		move(1000, 1)
	if incoming == 'B':
		display.show(incoming)
		move(1000, 0)
	if incoming == 'S':
		display.show('S')
		stop()
		