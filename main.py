import pyautogui
import time
import keyboard
import random

time.sleep(5)

number = [1, 2]
bit = [7]
while keyboard.is_pressed('t') == False:
    if pyautogui.pixel(1692, 720)[0] == 120:
        if range(random.choice(number) != 1):
            for i in range(random.choice(bit)):
                pyautogui.click(x=805, y=691)
            pyautogui.click(x=902, y=692)
        else:
            for i in range(random.choice(bit)):
                pyautogui.click(x=1754, y=694)
            pyautogui.click(x=1685, y=689)


            """
            import pyautogui
            pyautogui.displayMousePosition()
            """

