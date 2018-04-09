# This code will only run on the BBC Microbit
# This code will enable you to turn your BBC
# Microbit into a dice

from microbit import *
import random

num1 = Image('00900:09090:00900:00900:09990')
num2 = Image('09900:90090:00900:09000:99990')
num3 = Image('09990:00090:09990:00090:99900')
num4 = Image('00990:09090:99999:00090:00090')
num5 = Image('99990:90000:99900:00090:99900')
num6 = Image('09990:90000:99900:90090:09900')

while True:
	if accelerometer.was_gesture('shake'):
		display.clear()
		number = random.randint(1,6)
		
		if number == 1:
			display.show(num1)
			sleep(2000)
			pass
		if number == 2:
			display.show(num2)
			sleep(2000)
			pass
		if number == 3:
			display.show(num3)
			sleep(2000)
			pass
		if number == 4:
			display.show(num4)
			sleep(2000)
			pass
		if number == 5:
			display.show(num5)
			sleep(2000)
			pass
		if number == 6:
			display.show(num6)
			sleep(2000)
			pass