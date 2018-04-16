from microbit import *
import random

class RPS:
    
    def lose():
        display.scroll('You Lose')
        display.show(Image.SAD)
        sleep(1000)
        
    def win():
        display.scroll('You Win')
        display.show(Image.HAPPY)
        sleep(1000)
        
    def draw():
        display.scroll('Draw')
        display.show(Image.MEH)
        sleep(1000)
        
    def computer_decides(choice = None):
        
        options = ['rock', 'paper', 'scissors']
        number = random.randint(0,2)
        computer = options[number]
        display.scroll('Computer Chose ' + computer)
        sleep(1000)
        
        if choice == 'rock':
            
            for i in range(1):
                
                if computer == 'paper':
                    RPS.lose()
                elif computer == 'scissors':
                    RPS.win()
                else:
                    RPS.draw()
                
        if choice == 'scissors':
            
            for i in range(1):
                
                if computer == 'rock':
                    RPS.lose()
                elif computer == 'paper':
                    RPS.win()
                else:
                    RPS.draw()
                pass
                
        if choice == 'paper':
            
            for i in range(1):
                
                if computer == 'scissors':
                    RPS.lose()
                elif computer == 'rock':
                    RPS.win()
                else:
                    RPS.draw()
                pass
                
    def quit():
        display.show('Q')
        sleep(2000)
        display.off()
        while True:
            if button_a.is_pressed():
                RPS.game()
    
    def turn_display_on():
        if display.is_on():
            display.clear()
        else:
            display.on()

    def game():
        sleep(1000)
        RPS.turn_display_on()
        display.show(Image.HAPPY)
        
        while True:
            if button_b.is_pressed():
                RPS.quit()
            elif button_a.is_pressed():
                RPS.turn_display_on()
                display.scroll('Start')
                
                scissors = Image('99009:99090:00900:99090:99009')
                paper = Image('09990:09990:09990:09990:09990')
                rock = Image('00000:09990:09990:09990:00000')
                while True:           
                    if accelerometer.was_gesture('left'):
                        display.show(rock)
                        for i in range(1000):
                            # Confirming from the user
                            if accelerometer.was_gesture('shake'):
                                display.scroll('Rock')
                                sleep(1000)
                                RPS.computer_decides('rock')
                                RPS.game()
                            sleep(10)
                    elif accelerometer.was_gesture('up'):
                        display.show(scissors)
                        for i in range(1000):
                            # Confirming from the user
                            if accelerometer.was_gesture('shake'):
                                display.scroll('Scissors')
                                sleep(1000)
                                RPS.computer_decides('scissors')
                                RPS.game()
                            sleep(10)
                    elif accelerometer.was_gesture('right'):
                        # Confirming from the user
                        display.show(paper)
                        for i in range(1000):
                            if accelerometer.was_gesture('shake'):
                                display.scroll('Paper')
                                sleep(1000)
                                RPS.computer_decides('paper')
                                RPS.game()
                            sleep(10)
                    elif button_b.is_pressed():
                        RPS.quit()
                        
RPS.game()