#!/usr/bin/env python3

import sys
import random
import time
import os

# q08AYTqfJFfTMlxsaK9f
# YK14PpD43PisMRF6RP6l
# 6gs9AOtSSP2QtUhLzmiw

def ink_available():
  l = random.randint(0, 3) + random.random()
  return '{"total": ' + str(l) + '}'


def consumption():
  ml = random.randint(0, 100)
  return '{"consumption": ' + str(ml) + '}'


def main():
  if sys.argv and len(sys.argv) > 1:
    access_code = sys.argv[1]

    cmd = "echo -n '"
    cmd2 = "' | coap post coap://localhost/api/v1/" + access_code + "/telemetry"

    while True:
      msgTotal = ink_available()
      msgCons = consumption()
      os.system(cmd + msgTotal + cmd2)
      os.system(cmd + msgCons + cmd2)
      time.sleep(3)
  else:
    print("Usage: python3 fluid.py access_code")

if __name__ == '__main__':
    main()