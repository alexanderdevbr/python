import pyautogui
import time
import random

for z in range(1,10000):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pyautogui.moveTo(x, y)

    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)

    print('Move #'+ str(z) +' at ' + str(result) + ' [' + str(x) + ',' + str(y) + ']')
    time.sleep(15)