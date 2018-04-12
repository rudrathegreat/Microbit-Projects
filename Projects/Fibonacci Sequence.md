# BBC Micro:bit Projects
## The Fibonacci Sequence
### Abstract

----------------------------------------------------------------------------------------------------------------------------------------

The Fibonacci Sequence is one of the most complicated sequences and it is based to do with some simple logic and that is -

Add the two previous numbers to get the next number.

But this starts to get difficult and maybe tedious when you start to add big numbers... but what about **COMPUTERS?** There are programs out there to show the fibonacci sequence, and I am also going to show you as well.

----------------------------------------------------------------------------------------------------------------------------------------

### Design and Features

----------------------------------------------------------------------------------------------------------------------------------------

> Display the Time Taken to Find the Numbers
>
> You can give the Input
>
> Interactive Displays
>
> etc.

----------------------------------------------------------------------------------------------------------------------------------------

### Code Explained

----------------------------------------------------------------------------------------------------------------------------------------

We need to define a method for finding the sequence -

```Python

def fibonacci(x):
  pass

```

Now, we add the logic -

```Python

def fibonacci(x):
  
  a = 0
  b = 1
  
  for i in range(x-2):
    
    c = b
    b = a + b
    a = c
  
  return b
  
```

Now we use this method, add time and combine it together -

```Python

import time

start_time = time.time()

def fibonacci(x):
	a = 0
	b = 1
	for i in range(x-2):
		c = b
		b = a + b
		a = c
	return b

numbers_to_generate = 500
numbersGenerated = fibonacci(numbers_to_generate)

end_time = time.time()
time = end_time - start_time
print(numbersGenerated)
print('run time: ' + str(time) + 's')

```

And that's it!
----------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------------------------------

### Technologies Used

----------------------------------------------------------------------------------------------------------------------------------------

> Raspberry Pi, Mu Editor, Python IDLE
>
> BBC Microbit

----------------------------------------------------------------------------------------------------------------------------------------
