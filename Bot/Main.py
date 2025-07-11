import cv2
import numpy as np
import pyautogui
import random
import math
import time
def attack():
    time.sleep(0.5)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Attack.jpg")
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.8:
        match_top_left = max_loc
        center_x = match_top_left[0] + w // 2
        center_y = match_top_left[1] + h // 2
        pyautogui.moveTo(center_x, center_y, duration=0.2)
        pyautogui.click()
        print(f"Clicked at: ({center_x}, {center_y})")

def Find_match():
    time.sleep(0.5)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Find_Match.jpg")
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.8:
        match_top_left = max_loc
        center_x = match_top_left[0] + w // 2
        center_y = match_top_left[1] + h // 2
        pyautogui.moveTo(center_x, center_y, duration=0.2)
        pyautogui.click()
        print(f"Clicked at: ({center_x}, {center_y})")

def Edrag():
    time.sleep(0.5)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Edrag.jpg")
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.8:
        match_top_left = max_loc
        center_x = match_top_left[0] + w // 2
        center_y = match_top_left[1] + h // 2
        pyautogui.moveTo(center_x, center_y, duration=0.2)
        pyautogui.click()

def Deploy_Troops():
    A = (932, 16)
    B = (840, 84)
    C = (1641, 712)
    D = (1733, 644)
    num_lines=20
    spacing=120
    point_count=9
    def interpolate(p1, p2, t):
        return (p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t)
    def distance(p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1] - p1[1])
    def spaced_points(p_start, p_end, spacing, count):
        total_length = distance(p_start, p_end)
        if total_length < spacing * (count - 1):
            raise ValueError("Line too short for spacing.")
        offset = random.uniform(0, total_length - spacing * (count - 1))
        return [interpolate(p_start, p_end, (offset + i * spacing) / total_length) for i in range(count)]
    time.sleep(1)
    lines = [(interpolate(A, B, t), interpolate(D, C, t)) for t in [i / (num_lines - 1) for i in range(num_lines)]]
    start, end = random.choice(lines)
    points = spaced_points(start, end, spacing, point_count)
    for x, y in points:
        pyautogui.click(x, y)
        time.sleep(0.1)

def main():
    attack()
    Find_match()
    time.sleep(5)
    pyautogui.keyDown("ctrl")
    pyautogui.scroll(-500)
    pyautogui.keyUp("ctrl")
    x, y = pyautogui.size()
    pyautogui.moveTo(x // 2, y // 2, 0.2)
    pyautogui.dragTo(200, 800, duration=0.2, button='left')
    Edrag()
    Deploy_Troops()

main()
