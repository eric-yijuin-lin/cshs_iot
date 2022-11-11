import time
from dht import DHT11
from machine import Pin, ADC, SoftI2C
from esp8266_i2c_lcd import I2cLcd

# 建立用來感測溫濕度的工具變數
d5 = Pin(14) # 使用 D5 接角準備接收溫溼度感測器的數據
dht = DHT11(d5) # 使用 D5 接腳建立溫溼度感測工具的變數
adc = ADC(0) # 使用 A0 接腳建立「類比（Analog）」訊號接腳變數

# 建立用來操縱 LCD 顯示器的工具變數
i2c_addr = 0x27 # 顯示器的 I2C 通訊介面位址
soft_i2c = SoftI2C(scl=Pin(5), sda=Pin(4)) # 建立 I2C 通訊工具 
lcd = I2cLcd(soft_i2c, i2c_addr, 2, 16) # 建立 2 x 16 格的 LCD 顯示器工具

# 自訂義的函式，函式名稱為 lcd_show，並可以傳入兩個參數：text 與 clear
# def 關鍵字用來告訴 Python，我們要開始定義函式了
# lcd_show 是函式名稱，也可以自由的取成其他名字
# text 參數代表要顯示的文字
# clear 參數決定顯示文字之前，要不要先清空畫面
def lcd_show(text, clear=True):
    if clear:
        lcd.clear() # lcd.clear() 會清空畫面
    lcd.move_to(0, 0) # lcd.move_to(x, y) 會把游標移動到 LCD 顯示器的 x, y 位置上
    lcd.putstr(text) # lcd.putstr("文字") 會把 "文字" 秀在 LCD 顯示器上

while True:
    try:
        dht.measure()
        humidity = dht.humidity()
        temperature = dht.temperature()
        soil_moisture = adc.read()
        
        print(f"相對溼度：{humidity}", end=", ")
        print(f"氣溫：{temperature}", end=", ")
        print(f"土壤濕度：{soil_moisture}")
        lcd_show(f"RH:{humidity} T:{temperature}C \nSoil:{soil_moisture}")
    except Exception as ex:
        print(ex)
    time.sleep(1)
    

