import pyautogui
import time
import keyboard
import random

time.sleep(5)

number = [1, 2]
bit = [7]
while keyboard.is_pressed('t') == False:
    if pyautogui.pixel(1577, 1027)[0] == 119:
        if range(random.choice(number) != 1):
            for i in range(random.choice(bit)):
                pyautogui.click(x=1664, y=1001)
            pyautogui.click(x=1577, y=1027)
        else:
            for i in range(random.choice(bit)):
                pyautogui.click(x=235, y=1010)
            pyautogui.click(x=361, y=1020)


            """
            import pyautogui
            pyautogui.displayMousePosition()
            """

