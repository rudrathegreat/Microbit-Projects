# This program is the method used to find the sequence

def fibonacci(x):
	a = 0
	b = 1
	for i in range(x-2):
		c = b
		b = a + b
		a = c
	return b

def sequence(number):
	a = 0
	b = 1
	for i in range(x-2):
		c = b
		b = a + b
		a = c
	return i + 3