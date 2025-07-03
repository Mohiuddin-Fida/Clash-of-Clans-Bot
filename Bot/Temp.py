import pyautogui
import time
import random

time.sleep(2)


def main():
    try:
        Attack = pyautogui.locateOnScreen("Attack.png", confidence=0.8)
        if Attack:
            pyautogui.leftClick(Attack)
    except:
        pass


main()
