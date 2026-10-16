import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT11(board.D4) # GPIO pin 4

while True:
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        
        humidity = dht_device.humidity
        
        print("Temperature: {:.1f}°C / {:.1f}°F   Humidity: {:.1f}%".format(temperature_c, temperature_f, humidity))
    except RuntimeError as error:  
        print(error.args[0])
        
    time.sleep(2.0)