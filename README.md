# IOT Architecture 
An IoT project where we need to emulate and manage multiple devices. Then process massive data sent from these various devices. For the project, thingsboard platforme was used. 
ThingsBoard is an open-source IoT platform for device management, data collection, processing and visualization for your IoT projects


## Emulated Devices
3 different IOT Device Types:
  1. Light Sensor: On/Off with location Sensor. Bidirectional protocol.
  - App to simulate a light light intensity and light status.
  - Sends random Data to the server every 3 seconds
  - Uses MQTT protocol
  2. Temperature & Humidity with location Sensor.
  - App to simulate temperature and humidity of a location.
  - Sends random Data to the server every 3 seconds
  - Uses HTTP protocol
  3. Fluid Sensor with location Sensor
  - App to simulate the total liquid available in litters and the consumption of said liquid in ml.
  - Sends random Data to the server every 3 seconds
  - Uses CoAP protocol

How to use:

`python3 light.py {access_code}`

This launches the app to simulate the light sensor.

`python3 temperature_humidity.py {access_code}`

This launches the app to simulate the temperature and humidity sensor.

`python3 fluid.py {access_code}`

This launches the app to simulate the fluid sensor.

## Thingsboard


### Device Profiles


### Dashboards


### Rule Chains
