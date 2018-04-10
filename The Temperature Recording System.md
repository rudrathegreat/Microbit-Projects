# BBC Micro:bit Projects
## The Temperature Recording System
### Abstract

The Temperature Recording System

Ever want a system where you can know the temperature and that the predictions are s accurate as they can be? Introducing, the temperature recording system.

The system allows you to find out the temperature at a particular location. It will then process this data onto Scratch for a visual display of the temperature.

This may be useful for forecasters if they want to find patterns in the temperature so they can use the system and the visual display on Scratch to see those patterns very easily.

Read the other documentations to find out more about the system.

### Design and Features

> Remote
>
> Graph Can Be Shown On Scratch
>
> Efficient
>
> Long Lasting

### Technologies Used

> BBC Micro:bit, Motor Driver Board
>
> Raspberry Pi, Mu Editor
>
> Temperature Sensor
>
> 4 Lithium Ion Batteries

### More Info

The temperature sensor is behind all of the sensing. Attached to a BBC Microbit to transmit the data and for power, the temperature sensor just sits there and senses the temperature.

The BBC Microbit with the attached sensor receives the data and then transmits it to the other BBC Microbit via radio. But the input the BBC Microbit with the attached sensor is receiving is in a form of an integer. So the BBC Microbit translates that integer into a string for it to be sent.

```Python

from microbit import *
import radio

radio.config(channel = 76)
radio.on()

temperature = 20.523

while True:
  if button_a.is_pressed():
    radio.send(str(temperature))
    display.scroll('Sent')
    sleep(1000)
  
  display.show('-')

```

When the BBC Microbit without the sensor recevies the data, it then processes it onto Scratch. But first, it needs to be transferred back into an integer.

```Python

from microbit import *
import radio

radio.config(channel = 76)
radio.on()

while True:
  incoming == radio.receive():
  
  if incoming == None:
    display.show('-')
    pass
  else:
    display.scroll(incoming)
    print(int(incoming))
  
  display.show('-')
  
```

This data is then passed into this program aka intepreter to then be processed onto Scratch. It goes through a program which puts this data in several variables to then be passed onto Scratch.
