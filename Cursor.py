'''
# Funciona apenas em Windows
############################
Instalacao biblioteca pyautogui
1) sudo apt-get install scrot python3-tk python3-dev
2) python3 -m venv .venv
3) source .venv/bin/activate
4) python3 -m pip install --upgrade pip
5) python3 -m pip install --upgrade Pillow
6) python3 -m pip install pyautogui
'''
import pyautogui
import time
import random

#for z in range(1,10000):
z=0
while True:
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    z += 1
    pyautogui.moveTo(x, y)

    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)

    print('Move #'+ str(z) +' at ' + str(result) + ' [' + str(x) + ',' + str(y) + ']')
    time.sleep(30)