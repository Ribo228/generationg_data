from machine import Pin, SoftI2C
from time import sleep
import BME280
from ssd1306 import SSD1306_I2C

i2c=SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128,64,i2c)
bme = BME280.BME280(i2c=i2c,address=119)

while True:
    tem = bme.temperature
    hum = bme.humidity
    p = bme.pressure
    print("Temperature: ", tem)
    print("Humidity: ", hum)
    print("Pressure: ", p)
    oled.fill(0)
    oled.text("Temprature:" + str(tem)+"C",0,2,1)
    oled.text("Humidity:" +str(hum) + "%", 0,20,1)
    oled.text("Pressure:" + str(p), 0,40,1)
    oled.show()
    sleep(1)