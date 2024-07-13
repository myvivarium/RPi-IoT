![Logo](https://github.com/myvivarium/RPi-IoT/blob/main/images/IoT_graphical_abstract-mod.webp)

# RPi-IoT for MyVivarium

A stand-alone Raspberry Pi-enabled IoT system to monitor near-realtime sensor data in a MyVivarium web app. This system can also be used on its own to monitor near-realtime sensor data.


![til](./images/IOTsensors1.gif)
![til](./images/IOTsensors2.gif)
![til](./images/IOTsensors3.gif)

Demo interactive snapshot: **[Link](https://snapshots.raintank.io/dashboard/snapshot/BS9oMWCz8rpT2H3xoGVoHyDHSobyJrrW)**

## Table of Contents
- [Features](#features)
- [Pre-requirements](#pre-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Powered by Raspberry Pi
- Multiple I<sup>2</sup>C sensors
- Data visualization using Grafana
- Event alerts via Google chat webhook app

## Pre-requirements
- Raspberry Pi Imager: **[Link](https://www.raspberrypi.com/software/)**
- 

## Materials
- Raspberry Pi 4B
- I2C sensors
- Note: this setup utilizes three sensors with distinct I2C addresses. If >2 sensors with the same address are needed, a [multiplexer] can solve the issue.
