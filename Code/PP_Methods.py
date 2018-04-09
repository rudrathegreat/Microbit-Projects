def redLedOn():
    pin12.write_digital(1) 
    pin8.write_digital(0)  
    pin16.write_digital(0)
    pin0.write_digital(0)
    
def yellowLedOn():
    pin12.write_digital(0) 
    pin8.write_digital(1)  
    pin16.write_digital(0)
    pin0.write_digital(0)
 
def greenLedOn():
    pin12.write_digital(0) 
    pin8.write_digital(0)  
    pin16.write_digital(1)
    pin0.write_digital(0)

def blueLedOn():
    pin12.write_digital(0) 
    pin8.write_digital(0)  
    pin16.write_digital(0)
    pin0.write_digital(1)
    
def LedOff():
    pin12.write_digital(0) 
    pin8.write_digital(0)  
    pin16.write_digital(0)
    pin0.write_digital(0)