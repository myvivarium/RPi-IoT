![Logo](https://github.com/myvivarium/RPi-IoT/blob/main/images/IoT_graphical_abstract-mod.webp)

# RPi-IoT for MyVivarium

A stand-alone Raspberry Pi-enabled IoT system to monitor near-realtime sensor data in a MyVivarium web app. This system can also be used on its own to monitor near-realtime sensor data.


![til](./images/IOTsensors1.gif)
![til](./images/IOTsensors2.gif)
![til](./images/IOTsensors3.gif)

Demo interactive snapshot: **[Link](https://snapshots.raintank.io/dashboard/snapshot/BS9oMWCz8rpT2H3xoGVoHyDHSobyJrrW)**

## Table of Contents
- [Features](#features)
- [Materials](#materials)
- [Pre-requirements](#pre-requirements)
- [Pi Configuration Steps](#pi configuration steps)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Powered by Raspberry Pi
- Multiple I<sup>2</sup>C sensors
- Data visualization using Grafana
- Event alerts via Google chat webhook app

## Materials
- Raspberry Pi-related
    - Raspberry Pi 4 Model B - 2 GB RAM (validated with the 2 GB RAM version, but 1 GB should also work)
    - 128 GB micro SD card
    - Raspberry Pi 4 case with fan, passive heat-sinks, and power supply
    - Micro HDMI to HDMI Cable, keyboard, mouse, monitor (only required for initial Pi configuration)
- I<sup>2</sup>C sensors
    - SHT30 Temperature And Humidity Sensor: **[Link](https://www.adafruit.com/product/5064)**
    - Adafruit VEML7700 Lux Sensor: **[Link](https://www.adafruit.com/product/4162)**
    - Adafruit VL53L1X Time of Flight Distance Sensor: **[Link](https://www.adafruit.com/product/3967)**
- Wires and connectors
    - STEMMA QT / Qwiic JST SH 4-pin Cable with Premium Female Sockets: **[Link](https://www.adafruit.com/product/4397)**
    - STEMMA QT / Qwiic JST SH 4-Pin Cable: **[Link](https://www.adafruit.com/product/5385)**
    - Female/Male Jumper Wires: **[Link](https://www.adafruit.com/product/1952)**

## Pre-requirements
- Raspberry Pi Imager: **[Link](https://www.raspberrypi.com/software/)**
- Internet access at deployment location
- 


Note: this setup utilizes three sensors with distinct I2C addresses. If >2 sensors with the same address are needed, a [multiplexer] can solve the issue.
