# This code will only run on the BBC Microbit
# This code will enable you to turn your BBC
# Microbit into a dice

from microbit import *
import random

while True:
	if accelerometer.was_gesture('shake'):
		display.clear()
		number = random.randint(1,6)
		
		display.show(str(number))
		sleep(2000)
		pass