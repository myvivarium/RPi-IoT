#!/usr/bin/python3

import os
import sys
import time
import board
import adafruit_sht31d
import adafruit_vl53l1x
import adafruit_veml7700
import requests

#Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA

#Define the different sensors and parameters
#Temperature-Humidity Sensor SHT31D
sht31 = adafruit_sht31d.SHT31D(i2c)

#Distance or proximity sensor VL53L1X
vl53 = adafruit_vl53l1x.VL53L1X(i2c)

#VL53 parameters: distance_mode = 2 is for long-distance, set to 1 for short-distance; timing_budget is time required by the sensor to make one distance measurement in ms
vl53.distance_mode = 2
vl53.timing_budget = 100
#Initialize VL53 ranging
vl53.start_ranging()

#Light or illuminance sensor VEML7700
veml7700 = adafruit_veml7700.VEML7700(i2c)

#Define template for influxdb database
DATA_TEMPLATE = """\
temperature,sensor=SHT31D value={temperature:.1f} {time}
humidity,sensor=SHT31D value={humidity:.1f} {time}
illuminance,sensor=VEML7700 value={illuminance:.1f} {time}
proximity,sensor=VL53L1X value={proximity:.1f} {time}"""

#Define headers for CSV file which will contain all sensor data
headers = ['Temperature (C)', 'Relative Humidity (%)', 'Illuminance (lux)', 'Proximity to sensor (cm)', 'Date', 'Timestamp']

#Post all sensor data to influxdb database titled multisensors
while True:
    temperature, humidity, illuminance, proximity = sht31.temperature, sht31.relative_humidity, veml7700.lux, vl53.distance
    if temperature is not None and humidity is not None and illuminance is not None and proximity is not None:
        requests.post("http://127.0.0.1:8086/write?db=multisensors", data=DATA_TEMPLATE.format(
            temperature=temperature,
            humidity=humidity,
            illuminance=illuminance,
            proximity=proximity,
            time=int(time.time()*1e9),
        ))
        print("Temp={0:0.1f}C Humidity={1:0.1f}% Illuminance={2:0.1f} lux Proximity={3:0.1f} cm".format(temperature, humidity, illuminance, proximity))
        #log temperature and humidity data to a CSV file with current date as file name
        filename1 = time.strftime("%Y-%m-%d")
        file = open(filename1+".csv","a")
        if os.stat(filename1+".csv").st_size == 0:  # If file is empty
            file.write(','.join(headers) + '\n')  # Write headers
        file.write("{0:0.1f},{1:0.1f},{2:0.1f},{3:0.1f}".format(temperature,humidity,illuminance, proximity))
        file.write(time.strftime(","+'%Y-%m-%d'+"," '%H:%M:%S')+"\n")
        file.close()
    else:
        print("Sensor failure. Check wiring.", (humidity, temperature, illuminance, proximity))
    time.sleep(60) #Sensor data read interval = 60 s. Lesser intervals may cause sensor malfunction
