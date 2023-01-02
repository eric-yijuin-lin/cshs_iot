import network
import urequests as requests
import time

# 設定 wifi SSID 名稱、wifi 密碼與伺服器網址
WIFI_SSID = ''
WIFI_PASSWORD = ''

# 建立 wifi 連線
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)
while True:
    if not wifi.isconnected():
        print('connecting to wifi...')
        time.sleep(1)
    else:
        print('wifi connected！')
        break
    
# 發送 http 請求



