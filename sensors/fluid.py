#!/usr/bin/env python3

import sys
import random
import time

def fluid_type():
  return 'no clue'

def ink_available():
  l = random.randint(0, 3) + random.random()
  return l


def consumption():
  ml = random.randint(0, 100)
  return ml

def main():
  if sys.argv and len(sys.argv) > 1:
    access_code = sys.argv[1]
    while True:
      type = fluid_type()
      ink = ink_available()
      ml = consumption()
      print(type, ink, ml)
      time.sleep(2)
  else:
    print("Usage: python3 fluid.py access_code")

if __name__ == '__main__':
    main()