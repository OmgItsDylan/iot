#!/usr/bin/env python3

import sys
import random
import time
import os
import tkinter as tk

# 9KoWvn7JUZ1xeoVUJPtr
# 8lDJcqe7waDWdpnp56Ye
# VhB5McEIlaOY4YQorCnB

def lightIntensity(status):
  if status == "on":
    light_level = random.randint(0, 100)
  else:
    light_level = 0
  global var_int
  var_int.set("Light intensity: " + str(light_level))
  return '{"intensity":' + str(light_level) + '}'

def lightStatus():
  light_status = random.choice(['on', 'off', 'on', 'on', 'on'])
  global var_status
  var_status.set("Status: " + light_status)
  return '{"status":' + light_status + '}', light_status


def loop():
    msgStatus, status = lightStatus()
    msgIntensity = lightIntensity(status)
    os.system(cmd + msgStatus)
    os.system(cmd + msgIntensity)
    win.update_idletasks()
    win.after(3000, loop)


def main():
    global win
    global var_status
    global var_int
    win = tk.Tk()
    win.geometry("700x350")
    var_status = tk.StringVar()
    var_status.set('Unknown')
    var_int = tk.StringVar()
    var_int.set('Unknown')
    label1 = tk.Label(win, textvariable=var_status).pack()
    label2 = tk.Label(win, textvariable=var_int).pack()
    win.after(1000, loop)
    win.mainloop()


if __name__ == '__main__':
    if sys.argv and len(sys.argv) > 1:
        access_code = sys.argv[1]
        cmd = 'mosquitto_pub -d -q 1 -h "192.168.1.42" -p "1883" -t "v1/devices/me/telemetry" -u "' + access_code + '" -m '
        main()
    else:
        print("Usage: python3 light.py access_code")
