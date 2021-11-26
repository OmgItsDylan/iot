#!/usr/bin/env python3

import sys
import random
import time

def temperature():
  celsius = random.randint(-10, 43)
  return celsius

def humidity():
  percentage = random.randint(0, 100)
  return percentage

def position():
  lat = random.randint(-90, 90)
  long = random.randint(-180, 80)
  return [lat + random.random(), long + random.random()]

def main():
  if sys.argv and len(sys.argv) > 1:
    access_code = sys.argv[1]
    while True:
      celsius = temperature()
      percentage = humidity()
      coordinates = position()
      print(celsius, percentage, coordinates)
      time.sleep(2)
  else:
    print("Usage: python3 temperature_humidity.py access_code")

if __name__ == '__main__':
    main()