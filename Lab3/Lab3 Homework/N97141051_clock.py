import sys
import time
from pathlib import Path

import RPi.GPIO as GPIO


# 載入 Lab3 內附的 TM1637 驅動程式。
DRIVER_PATH = Path(__file__).resolve().parents[1] / "7segment_display" / "raspberrypi-tm1637"
sys.path.insert(0, str(DRIVER_PATH))

from tm1637 import TM1637


CLK = 23  # BCM GPIO 5，依照實際接線調整
DIO = 24  # BCM GPIO 4，依照實際接線調整

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
display = TM1637(CLK, DIO)
display.brightness(2)

colon_on = False

try:
	while True:
		current_time = time.localtime()
		colon_on = not colon_on
		display.numbers(current_time.tm_hour, current_time.tm_min, colon_on)
		time.sleep(1)

except KeyboardInterrupt:
	pass
finally:
	display.write([0, 0, 0, 0])
	GPIO.cleanup()
