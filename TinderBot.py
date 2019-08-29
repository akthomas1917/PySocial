import pyautogui
import time

#print(pyautogui.position())

numswipes = 50

i = 0
while i <= numswipes:
    pyautogui.click(1281, 854)
    time.sleep(0.5)
    i += 1