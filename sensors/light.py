#!/usr/bin/env python3

import sys
import random
import time

def lightPower():
  light_status = random.choice(['on', 'off'])
  return light_status

def lightIntensity():
  light_level = random.randint(0, 100)
  return light_level

def lightStatus():
  light_status = random.choice(['on', 'off'])
  return light_status

def main():
  if sys.argv and len(sys.argv) > 1:
    access_code = sys.argv[1]
    while True:
      light_power = lightPower()
      light_level = lightIntensity()
      light_status = lightStatus()
      print(light_power, light_level, light_status)
      time.sleep(2)
  else:
    print("Usage: python3 light.py access_code")

if __name__ == '__main__':
    main()