#!/usr/bin/env python3

import sys
import random
import time
import os

# 9KoWvn7JUZ1xeoVUJPtr
# 8lDJcqe7waDWdpnp56Ye
# VhB5McEIlaOY4YQorCnB

def lightIntensity(status):
  if status == "on":
    light_level = random.randint(0, 100)
  else:
    light_level = 0
  return '{"intensity":' + str(light_level) + '}'

def lightStatus():
  light_status = random.choice(['on', 'off', 'on', 'on', 'on'])
  return '{"status":' + light_status + '}', light_status

def main():
  if sys.argv and len(sys.argv) > 1:
    access_code = sys.argv[1]
    cmd = 'mosquitto_pub -d -q 1 -h "192.168.1.42" -p "1883" -t "v1/devices/me/telemetry" -u "' + access_code + '" -m '
    while True:
      msgStatus, status = lightStatus()
      msgIntensity = lightIntensity(status)
      os.system(cmd + msgStatus)
      os.system(cmd + msgIntensity)
      time.sleep(3)
  else:
    print("Usage: python3 light.py access_code")

if __name__ == '__main__':
    main()