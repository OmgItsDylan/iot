#!/usr/bin/env python3

import sys
import random
import tkinter as tk
import os

# q08AYTqfJFfTMlxsaK9f
# YK14PpD43PisMRF6RP6l
# 6gs9AOtSSP2QtUhLzmiw

def ink_available():
  l = random.randint(0, 5) + random.random()
  global var_total
  var_total.set("Total amount: " + str(l))
  return '{"total": ' + str(l) + '}'


def consumption():
  ml = random.randint(0, 250)
  global var_cons
  var_cons.set("Consumption rate: " + str(ml))
  return '{"consumption": ' + str(ml) + '}'


def loop():
  msgTotal = ink_available()
  msgCons = consumption()
  os.system(cmd + msgTotal + cmd2)
  os.system(cmd + msgCons + cmd2)
  win.update_idletasks()
  win.after(3000, loop)


def main():
  global win
  global var_total
  global var_cons
  win = tk.Tk()
  win.geometry("700x350")
  var_total = tk.StringVar()
  var_total.set('Unknown')
  var_cons = tk.StringVar()
  var_cons.set('Unknown')
  label1 = tk.Label(win, textvariable=var_total).pack()
  label2 = tk.Label(win, textvariable=var_cons).pack()
  win.after(1000, loop)
  win.mainloop()


if __name__ == '__main__':
  if sys.argv and len(sys.argv) > 1:
    access_code = sys.argv[1]
    cmd = "echo -n '"
    cmd2 = "' | coap post coap://localhost/api/v1/" + access_code + "/telemetry"
    main()
  else:
    print("Usage: python3 fluid.py access_code")
