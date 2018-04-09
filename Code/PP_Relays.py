# all three Pololu relays working independently
# by Edmond Lascaris
# 14 Feb 2018
# Platypus project
# Replicated by Rudra

from microbit import *
# BBC Micro:bit motor driver board V2 H-bridge
def pin12RelayOff():
    pin8.write_digital(0)
    pin12.write_digital(0)
    
def pin12RelayOn():
    pin8.write_digital(0)
    pin12.write_digital(1) 
    
def pin16RelayOff():
    pin0.write_digital(0)
    pin16.write_digital(0)
    
def pin16RelayOn():
    pin0.write_digital(0)
    pin16.write_digital(1)     
    
# using button_b to control relay
def pin11RelayOn():
    pin11.write_digital(1)   
    
def pin11RelayOff():
    pin11.write_digital(0)
    
toggle = True    

while True:
    if button_a.is_pressed() and toggle==True:
        pin16RelayOn()
        pin12RelayOn()
        pin11RelayOn()
        toggle = False
        display.show("1")
        print(toggle)
        sleep(500)
        
    if button_a.is_pressed() and toggle==False:
        pin16RelayOff()
        pin12RelayOff()
        pin11RelayOff()
        toggle = True
        display.show("0")
        print(toggle)
        sleep(500)        
        