from microbit import *
import random

def computer_decides():
    for i in range(1):
        
        computer = random.randint(1,3)
        
        if computer == 1:
            display.scroll('You Win')
            display.show(Image.Happy)
            sleep(1000)
            pass
        if computer == 2:
            display.scroll('You Win')
            display.show(Image.Happy)
            sleep(1000)
            pass
        if computer == 3:
            display.scroll('You Win')
            display.show(Image.Happy)
            sleep(1000)
            pass
        pass
def quit(variable = None):
    while variable != 1:
        display.show('Q')
        if button_a.is_pressed():
            variable = 1
            
def gameplay():
    
    variable = 0

    while True:
        if accelerometer.was_gesture('face down'):
            quit(variable)
        if accelerometer.was_gesture('shake'):
            variable = 1
            display.clear()
            display.show(Image.SMILE)
                
            options = ['rock', 'paper', 'scissors']
            selection = 0
            scissors = Image('99009:99090:00900:99090:99009')
            paper = Image('09990:09990:09990:09990:09990')
            rock = Image('00000:09990:09990:09990:00000')
            
            if accelerometer.is_gesture('face down'):
                quit()
            while True:
                if button_b.is_pressed()
                    if selection >= 2:
                        selection = 0
                    else:
                        display.scroll(options[selection])
                    
                    if options[selection] == 'scissors':
                        display.show(scissors)
                    elif options[selection] == 'paper':
                        display.show(paper)
                    else:
                        display.show(rock)
                    
                    if button_a.is_pressed():
                        display.scroll(options[selection])
                        sleep(1000)
                        computer_decides()
                        gameplay()
                    if accelerometer.is_gesture('face down'):
                        quit()
                        
gameplay()