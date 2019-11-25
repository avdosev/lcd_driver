# -*- coding: utf-8 -*-

import time
import lcd

try:
    lcd.init()
    lcd.show_line("Hello, brow")
except KeyboardInterrupt:
    print("Exit pressed Ctrl+C")
finally:
    print("End of program")
