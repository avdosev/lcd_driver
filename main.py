# -*- coding: utf-8 -*-


import RPi.GPIO as gpio                 
import time                             
import lcd

try:  
  lcd.init()
  lcd.send(0000)
                        

except KeyboardInterrupt:
    print("Exit pressed Ctrl+C")        

finally:                    
    print("End of program")             