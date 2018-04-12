# BBC Micro:bit Projects
## Rock Paper Scissors
### Abstract

----------------------------------------------------------------------------------------------------------------------------------------

Do you want a game right at your fingertips? This simple yet effecitive Rock Paper Scissors program should do the trick! Using the BBC Microbit and the Raspberry Pi, you can code your BBC Microbit to play an endless number of games with you, and when you want to stop, you can do so just by clicking a button.

This program has been programmed using an implementation of Python known as Micropython, which allows you to program Python-style and flashing it onto a small microcontroller. This program has also been edited on the 'Mu' Micropython editor which can be used by anyone and everyone.

This project aims to give poor families a chance to interact with small, affordable devices on which they can program their own games. This may also help others if they are trying to do the same project.

----------------------------------------------------------------------------------------------------------------------------------------

### Design and Features

----------------------------------------------------------------------------------------------------------------------------------------

> Uses Accelerometer Chip
>
> Interactive Display
>
> User Can Quit Whenever He Wants
>
> User Friendly
>
> etc.

----------------------------------------------------------------------------------------------------------------------------------------

### Technologies Used

----------------------------------------------------------------------------------------------------------------------------------------

> BBC Micro:bit
>
> Accelerometer Chip
>
> Raspberry Pi, Mu Editor

----------------------------------------------------------------------------------------------------------------------------------------

### The Code Explained

----------------------------------------------------------------------------------------------------------------------------------------

You now define a class with several methods in it. Many big programs and programmers use this concept and they tend to call it Object Oriented Programming or OOP for short -

```Python

from microbit ipmort *
import random

class RPS:
    
    def lose():
        display.scroll('You Lose')
        display.show(Image.SAD)
        sleep(1000)
        pass
        
    def win():
        display.scroll('You Win')
        display.show(Image.HAPPY)
        sleep(1000)
        pass
        
    def draw():
        display.scroll('Draw')
        display.show(Image.MEH)
        sleep(1000)
        pass
        
    def computer_decides(choice = None):
        
        options = ['rock', 'paper', 'scissors']
        
        if choice == 'rock':
            
            for i in range(1):
                
                number = random.randint(0,2)
                computer = options[number]
                if computer == 'paper':
                    RPS.lose()
                elif computer == 'scissors':
                    RPS.win()
                else:
                    RPS.draw()
                pass
        if choice == 'scissors':
            
            for i in range(1):
                
                number = random.randint(0,2)
                computer = options[number]
                if computer == 'rock':
                    RPS.lose()
                elif computer == 'paper':
                    RPS.win()
                else:
                    RPS.draw()
                pass
        if choice == 'paper':
            
            for i in range(1):
                
                number = random.randint(0,2)
                computer = options[number]
                if computer == 'scissors':
                    RPS.lose()
                elif computer == 'rock':
                    RPS.win()
                else:
                    RPS.draw()
                pass
    def quit(variable = None):
        while variable != 1:
            display.show('Q')
            if button_a.is_pressed():
                variable = 1

    def game():
        
        variable = 0

        while True:
            if button_b.is_pressed():
                RPS.quit(variable)
            if button_a.is_pressed():
                variable = 1
                display.clear()
                display.show(Image.SMILE)
                
                scissors = Image('99009:99090:00900:99090:99009')
                paper = Image('09990:09990:09990:09990:09990')
                rock = Image('00000:09990:09990:09990:00000')
                
                if button_b.is_pressed():
                    RPS.quit()
                
                sleep(1000)
                while True:           
                    display.clear()
                    if accelerometer.was_gesture('left'):
                        display.show(rock)
                        for i in range(1000):
                            if accelerometer.was_gesture('right'):
                                display.scroll('Rock')
                                sleep(1000)
                                RPS.computer_decides('rock')
                                RPS.game()
                                pass
                            sleep(10)
                    if accelerometer.was_gesture('up'):
                        display.show(scissors)
                        for i in range(1000):
                            if accelerometer.was_gesture('right'):
                                display.scroll('Scissors')
                                sleep(1000)
                                RPS.computer_decides('scissors')
                                RPS.game()
                                pass
                            sleep(10)
                    if accelerometer.was_gesture('shake'):
                        display.show(paper)
                        while True:
                            if accelerometer.was_gesture('right'):
                                display.scroll('Paper')
                                sleep(1000)
                                RPS.computer_decides('paper')
                                RPS.game()
                                pass
                            sleep(10)
                    if button_b.is_pressed():
                        RPS.quit()
                        
```

Now we use it and combine it together -

```Python

from microbit import *
import random

class RPS:
    
    def lose():
        display.scroll('You Lose')
        display.show(Image.SAD)
        sleep(1000)
        pass
        
    def win():
        display.scroll('You Win')
        display.show(Image.HAPPY)
        sleep(1000)
        pass
        
    def draw():
        display.scroll('Draw')
        display.show(Image.MEH)
        sleep(1000)
        pass
        
    def computer_decides(choice = None):
        
        options = ['rock', 'paper', 'scissors']
        
        if choice == 'rock':
            
            for i in range(1):
                
                number = random.randint(0,2)
                computer = options[number]
                if computer == 'paper':
                    RPS.lose()
                elif computer == 'scissors':
                    RPS.win()
                else:
                    RPS.draw()
                pass
        if choice == 'scissors':
            
            for i in range(1):
                
                number = random.randint(0,2)
                computer = options[number]
                if computer == 'rock':
                    RPS.lose()
                elif computer == 'paper':
                    RPS.win()
                else:
                    RPS.draw()
                pass
        if choice == 'paper':
            
            for i in range(1):
                
                number = random.randint(0,2)
                computer = options[number]
                if computer == 'scissors':
                    RPS.lose()
                elif computer == 'rock':
                    RPS.win()
                else:
                    RPS.draw()
                pass
    def quit(variable = None):
        while variable != 1:
            display.show('Q')
            if button_a.is_pressed():
                variable = 1

    def game():
        
        variable = 0

        while True:
            if button_b.is_pressed():
                RPS.quit(variable)
            if button_a.is_pressed():
                variable = 1
                display.clear()
                display.show(Image.SMILE)
                
                scissors = Image('99009:99090:00900:99090:99009')
                paper = Image('09990:09990:09990:09990:09990')
                rock = Image('00000:09990:09990:09990:00000')
                
                if button_b.is_pressed():
                    RPS.quit()
                
                sleep(1000)
                while True:           
                    display.clear()
                    if accelerometer.was_gesture('left'):
                        display.show(rock)
                        for i in range(1000):
                            if accelerometer.was_gesture('right'):
                                display.scroll('Rock')
                                sleep(1000)
                                RPS.computer_decides('rock')
                                RPS.game()
                                pass
                            sleep(10)
                    if accelerometer.was_gesture('up'):
                        display.show(scissors)
                        for i in range(1000):
                            if accelerometer.was_gesture('right'):
                                display.scroll('Scissors')
                                sleep(1000)
                                RPS.computer_decides('scissors')
                                RPS.game()
                                pass
                            sleep(10)
                    if accelerometer.was_gesture('shake'):
                        display.show(paper)
                        while True:
                            if accelerometer.was_gesture('right'):
                                display.scroll('Paper')
                                sleep(1000)
                                RPS.computer_decides('paper')
                                RPS.game()
                                pass
                            sleep(10)
                    if button_b.is_pressed():
                        RPS.quit()
                        
RPS.game()

```

And that's it!
----------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------------------------------
