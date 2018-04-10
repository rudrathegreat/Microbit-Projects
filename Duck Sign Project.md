# BBC Micro:bit Projects
## The Duck Sign Project
### Abstract

The Duck Sign Project plans to prevent people from feeding ducks due to overpopulation and to instead make people fascinated by the different species of ducks. The first part of the project is to make signs showing the population of ducks at the particular location.

If it shows a red LED on, then that means that there is too many ducks. If it shows a yellow LED on, that means that there are still a lot of ducks but not that many. If a green light is being shown then that means that the number of ducks are nearly plausible and when a blue light is being shown, then that means that the number of ducks are now plausible enough. We don't want them to go extinct!


```Python

from microbit import *

def Red_LED(Pin1_Value = None, Pin2_Value = None):
  pin8.write_digital(Pin1_Value)
  pin12.write_digital(Pin2_Value)

while True:
  if button_a.is_pressed():
    def Red_LED(1, 0)
    display.show('1')
    sleep(1000)
  if button_b.is_pressed():
    DEF Red_LED(0, 0)
    display.show('0')
    sleep(1000)
    
  display.show('-')
  
```

### Design and Features

> Interactive Display
> Educational for Everyone
> System cannot be damaged
> Can Easily Be Modified

### Techonlogies Used

> LED's
> Raspberry Pi, Mu Editor
> BBC Microbit, Motor Driver Board
> And more
