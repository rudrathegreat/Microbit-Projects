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