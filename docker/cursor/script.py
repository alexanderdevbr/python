import pyautogui
import time
import random
from datetime import datetime

print("Iniciando Loop para mover cursor...")
i=0
while True:
    i += 1
    x=random.randint(100,500)
    y=random.randint(100,500)
    current_datetime = datetime.now()

    print(f"{i}\t{current_datetime}\t{x}\t{y}")

    pyautogui.moveTo(x, y, duration=1)
    time.sleep(5)
