# BBC Microbit Projects
## The Dice Program
### Abstract

If you don't have a dice, that is ok. You can use this dice program on your BBC Microbit to make a dice for your favourite game!

This app uses simple Micropython with some logic of randomising the number. It uses some libraries including 'random'. It also uses the BBC Microbit display to show which number has been 'rolled'. it also uses the shake command so that when shaked, it can pick a random number.

### Design and Features

> Uses accelerometer chip. When shaken the BBC Microbit will choose a random number and display it.
> Simple
> Display Features
> Uses a BBC Microbit

### Code Explained

First, you have to import the necessary libraries in order for the program to work. If you want to make a dice program, you have to keep in mind that the number that is being randomly chosen has to be completely random and not in a predictable pattern. You can use the random module to simulate this -

```Python

from microbit import *
import random

```

Then, we need to display the numbers. We can use the display to do so -

```Python

from microbit import *

while True:
  if button_a.is_pressed():
    display.scroll('Hello World')

```

Then we add flow control and combine it together -

```Python

from microbit import *
import random

while True:
	if accelerometer.was_gesture('shake'):
		display.clear()
		number = random.randint(1,6)
		
		display.show(str(number))
		sleep(2000)
		pass
    
```

And that's it!
----------------------------------------------------------------------------------------------------------------------------------------

