# This program will not display each individual number on the
# microbit display. Instead, there is a different program to
# show those numbers. This program needs a BBC Microbit to run.

from microbit import *

def fibonacci(x):
	a = 0
	b = 1
	for i in range(x-2):
		c = b
		b = a + b
		a = c
	return i + 3
	
while True:

	if button_a.is_pressed():
	
		start_time = running_time()
		numbersGenerated = fibonacci(6844)
		end_time = running_time()
		time = end_time - start_time
		display.scroll('run time: ' + str(time) + 'ms')
	
	if button_b.is_pressed():
	
		display.scroll('Num Gen: ' + str(numbersGenerated))