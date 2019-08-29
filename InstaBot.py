import pyautogui

print(pyautogui.position())

pyautogui.moveTo(644, 527)
pyautogui.click()
pyautogui.click()

for i in range(8):
    pyautogui.scroll(-1050)
    pyautogui.click(button='right')
    pyautogui.click()
    pyautogui.click()