import board
import busio
import adafruit_bme280
import datetime
import time
import sys

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x77)

date = str(datetime.date.today())
current_time = str(datetime.datetime.now().time())
unix_time = str(time.time())
temp = str(bme280.temperature)
hum = str(bme280.humidity)
pressure = str(bme280.pressure)

DEVICE_NAME = 'basement'

line = DEVICE_NAME + '\t' +date + '\t' + current_time + '\t' + str(unix_time) + '\t' + temp + '\t' + hum + '\t' + pressure + '\n'
with open('/home/pi/all_data.tsv','a') as file:
	file.write(line)

with open('/home/pi/most_recent_data.tsv','w') as file:
	file.write(line)
