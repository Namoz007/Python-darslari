import pyautogui
import time
from emoji import emojize
import clipboard


time.sleep(0)
for i in range(100000):
    text = "Nima qilyapsan"
    clipboard.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")