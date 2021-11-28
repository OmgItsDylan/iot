#!/usr/bin/env python3

import sys
import random
import os
import tkinter as tk

# EwgZPbrg0ZCMTQ7i9FRr
# t0ribl0rddawhoFYYccw
# PNLCvQREWEG5gIYZkXDD

def temperature():
  celsius = random.randint(-10, 43)
  global var_temp
  var_temp.set("Temperature: " + str(celsius))
  return '"{\"temperature\": ' + str(celsius) + '}"'

def humidity():
  percentage = random.randint(0, 100)
  global var_humi
  var_humi.set("Humidity: " + str(percentage))
  return '"{\"humidity\": ' + str(percentage) + '}"'


def loop():
  msgTemp = temperature()
  msgHumi = humidity()
  os.system(cmd + msgTemp + cmd2)
  os.system(cmd + msgHumi + cmd2)
  win.update_idletasks()
  win.after(3000, loop)


def main():
  global win
  global var_temp
  global var_humi
  win = tk.Tk()
  win.geometry("700x350")
  var_temp = tk.StringVar()
  var_temp.set('Unknown')
  var_humi = tk.StringVar()
  var_humi.set('Unknown')
  label1 = tk.Label(win, textvariable=var_temp).pack()
  label2 = tk.Label(win, textvariable=var_humi).pack()
  win.after(1000, loop)
  win.mainloop()

if __name__ == '__main__':
  if sys.argv and len(sys.argv) > 1:
    access_code = sys.argv[1]
    cmd = 'curl -v -X POST -d '
    cmd2 = ' http://192.168.1.42:9090/api/v1/' + access_code + '/telemetry --header "Content-Type:application/json"'
    main()
  else:
    print("Usage: python3 temperature_humidity.py access_code")