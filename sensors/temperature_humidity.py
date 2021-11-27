#!/usr/bin/env python3

import sys
import random
import time
import os

# EwgZPbrg0ZCMTQ7i9FRr
# t0ribl0rddawhoFYYccw
# PNLCvQREWEG5gIYZkXDD

def temperature():
  celsius = random.randint(-10, 43)
  return '"{\"temperature\": ' + str(celsius) + '}"'

def humidity():
  percentage = random.randint(0, 100)
  return '"{\"humidity\": ' + str(percentage) + '}"'

def main():
  if sys.argv and len(sys.argv) > 1:
    access_code = sys.argv[1]

    cmd = 'curl -v -X POST -d '
    cmd2 = ' http://192.168.1.42:9090/api/v1/' + access_code + '/telemetry --header "Content-Type:application/json"'

    while True:
      msgTemp = temperature()
      msgHumi = humidity()
      os.system(cmd + msgTemp + cmd2)
      os.system(cmd + msgHumi + cmd2)
      time.sleep(3)
  else:
    print("Usage: python3 temperature_humidity.py access_code")

if __name__ == '__main__':
    main()