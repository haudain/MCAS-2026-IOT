import serial
import time 

ser = serial.Serial(
    port='/dev/serial0',  # 請根據實際情況修改
    baudrate=9600,  
    timeout=1
)

def send_data(data):
    if ser.is_open:
        ser.write(data.encode('utf-8'))
        print(f"已發送資料: {data}")

def receive_data():
    if ser.is_open:
        incoming_data = ser.readline().decode('utf-8').strip()
        if incoming_data:
            print(f"接收到資料: {incoming_data}")
            return incoming_data
    return None

#主程式
try:
    while True:
        # 發送資料
        send_data("Hello from Raspberry Pi!")
        time.sleep(1)  # 稍微停一下，避免畫面跳太快
        # 接收資料
        received = receive_data()
        time.sleep(1)  # 每2秒發送一次資料
except KeyboardInterrupt:
    print("\n程式中止")
finally:
    if ser.is_open:
        ser.close()
        print("序列埠已關閉")