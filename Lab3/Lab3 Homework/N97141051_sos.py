import time

import RPi.GPIO as GPIO


LED_PIN = 16       # BOARD 實體腳位 11
BUZZER_PIN = 18    # BOARD 實體腳位 12，需依實際接線調整
BUZZER_FREQUENCY = 523
UNIT = 0.2         # 摩斯碼一個短音／短亮的時間（秒）

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
buzzer = GPIO.PWM(BUZZER_PIN, BUZZER_FREQUENCY)


def signal(duration):
	"""同步點亮 LED 並讓蜂鳴器發聲指定時間。"""
	GPIO.output(LED_PIN, GPIO.HIGH)
	buzzer.start(50)
	time.sleep(duration)
	buzzer.stop()
	GPIO.output(LED_PIN, GPIO.LOW)


try:
	while True:
		for letter_index, letter in enumerate(("...", "---", "...")):
			for signal_index, symbol in enumerate(letter):
				signal(UNIT if symbol == "." else UNIT * 3)

				if signal_index < len(letter) - 1:
					time.sleep(UNIT)

			if letter_index < 2:
				time.sleep(UNIT * 3)

except KeyboardInterrupt:
	pass
finally:
	buzzer.stop()
	GPIO.output(LED_PIN, GPIO.LOW)
	GPIO.cleanup()
