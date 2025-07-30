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
import pygetwindow as gw

tempoEspera    = 30
hwnd           = 0
z              = 0
inicioExecucao = time.time()

target_window  = gw.getWindowsWithTitle("Teams")
if target_window:
    my_window = target_window[0]
    my_window.moveTo(0,0)

    try:
        my_window.activate()
        time.sleep(0.5)
        my_window.maximize()
    except Exception as e:
        print("Erro ao maximizar janela do Teams.")
    
else:
    print(f"Janela do Teams não encontrada.")
    time.sleep(5)
    quit()

while True:
    my_window.moveTo(0,0)
    my_window.maximize()

    x = random.randint(0, 500)
    y = random.randint(0, 500) 
    z += 1
    pyautogui.moveTo(x, y, duration=1)

    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)

    totalSegundos = time.time() - inicioExecucao
    dias, segundos = divmod(totalSegundos, 86400)
    horas, segundos = divmod(totalSegundos, 3600)
    minutos, segundos = divmod(totalSegundos, 60)

    print(f"{dias:02.0f}d, {horas:02.0f}h:{minutos:02.0f}m:{segundos:02.0f}s - Move #{z:04d} at {result} [{x:03d},{y:03d}]")
    time.sleep(tempoEspera)
