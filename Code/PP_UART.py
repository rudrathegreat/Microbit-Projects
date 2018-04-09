uart.init(baudrate=4800, bits=8, parity=None, stop=1, tx=pin2, rx=pin1) 

        
while True: 
    if uart.any():
        sleep(500)
        buffer = uart.readall()
        buf = str(buffer)

        if buf.find("cond") == 2:
            for i in buf:
                if i.isdigit() or i==".":
                    message = message + i
            message = "cond " + message
            radio.send(message)
            display.scroll(message, delay=50)
            buf = ""
            message = ""
            buffer = ""

        if buf.find("temp") == 2:
            for i in buf:
                if i.isdigit() or i==".":
                    message = message + i
            message = "temp " + message
            radio.send(message)
            display.scroll(message, delay=50)
            buf = ""
            message = ""
            buffer = ""