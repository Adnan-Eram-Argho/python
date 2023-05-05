import pyautogui
import time
i = 1
while i < 2:
    time.sleep(1)
    pyautogui.typewrite(
        'alabu {i}')
    pyautogui.press('enter')
    i += 1
