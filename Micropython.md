# BBC Micro:bit Projects
## Micropython Itself

Micropython is an implementation of Python made by a guy in C. Its main aim was for mirocontrollers and is mainly used in BBC Microbits. Although Micropython is an implementation of Python and that everything should be the same, there some changes. 

For one, time isn't a separate library and is part of the microbit module - :astonished:

```Python

from microbit import *

display.show(Image.HAPPY)
sleep(500)
display.clear()

```

Secondly, the amount of time you give to the BBC Microbit to sleep is in milliseconds. So 500 milliseconds equals half a second.

:hushed:

On the other hand, there are some benefits with Micropython.

:sweat_smile:

One of them is that you can display stuff on the 5x5 LED display -

```Python

from microbit import *

display.show(Image.HAPPY)

```
And many more surprises.

One editor by the name of Mu supports Micropython and can easily be downloaded onto any system.

:smile:

### More Info

If you want more info or if you want to download these two 'things' which we have been talking about (Micropython and Mu), then you can go to these websites -

https://micropython.org/
http://microbit-micropython.readthedocs.io/en/latest/
https://codewith.mu/
