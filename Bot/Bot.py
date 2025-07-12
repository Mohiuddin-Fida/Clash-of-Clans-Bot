import cv2
import numpy as np
import pyautogui
import random
import math
import time
import keyboard
import win32gui
import win32con

def bring_forward(partial_title):
    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if partial_title.lower() in title.lower():
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(hwnd)
                time.sleep(0.3)  # Wait briefly for focus
                pyautogui.press('f11')
                print(f"[INFO] Brought '{title}' forward and pressed F11.")
    win32gui.EnumWindows(enum_handler, None)

def Verify_Attack():
    time.sleep(0.2)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Attack.jpg", cv2.IMREAD_GRAYSCALE)
    result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(result)[1] >= 0.8

def Verify_Find_match():
    time.sleep(0.2)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Find_Match.jpg", cv2.IMREAD_GRAYSCALE)
    result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(result)[1] >= 0.8

def Verify_Edrag():
    time.sleep(0.2)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Edrag.jpg", cv2.IMREAD_GRAYSCALE)
    result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(result)[1] >= 0.8

def Verify_connection():
    time.sleep(0.2)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Connection_Lost.jpg", cv2.IMREAD_GRAYSCALE)
    result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(result)[1] >= 0.8

def Verify_Quit():
    time.sleep(0.2)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Quit.jpg", cv2.IMREAD_GRAYSCALE)
    result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(result)[1] >= 0.8

def Verify_End_Battle():
    time.sleep(0.2)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    template = cv2.imread("End_Battle.jpg", cv2.IMREAD_GRAYSCALE)
    result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(result)[1] >= 0.8

def Verify_Surrender():
    time.sleep(0.2)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Surrender.jpg", cv2.IMREAD_GRAYSCALE)
    result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(result)[1] >= 0.8

def Verify_Okay():
    time.sleep(0.2)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
    template = cv2.imread("Okay.jpg", cv2.IMREAD_GRAYSCALE)
    result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(result)[1] >= 0.8

def Verify_Return_Home():
    time.sleep(0.2)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Return_Home.jpg", cv2.IMREAD_GRAYSCALE)
    result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(result)[1] >= 0.8

def Try_again():
    time.sleep(0.2)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Try_Again.jpg")
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

def End_Battle():
    time.sleep(0.2)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread("End_Battle.jpg")
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

def Surrender():
    time.sleep(0.2)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Surrender.jpg")
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

def Return_Home():
    time.sleep(0.2)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Return_Home.jpg")
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

def Okay():
    time.sleep(0.2)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Okay.jpg")
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

def Quit():
    time.sleep(0.2)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread("Quit.jpg")
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

def Attack():
    time.sleep(0.2)
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

def Find_match():
    time.sleep(0.2)
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

def Edrag():
    time.sleep(0.2)
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
    time.sleep(0.2)
    lines = [(interpolate(A, B, t), interpolate(D, C, t)) for t in [i / (num_lines - 1) for i in range(num_lines)]]
    start, end = random.choice(lines)
    points = spaced_points(start, end, spacing, point_count)
    for x, y in points:
        pyautogui.click(x, y)
        time.sleep(0.1)

def main():
    bring_forward("LDPlayer")
    time.sleep(0.5)
    while not keyboard.is_pressed('q'):
        if Verify_connection():
            Try_again()
            time.sleep(8)
        if Verify_Attack():
            if Verify_Okay():
                Okay()
            if Verify_Quit():
                Quit()
            Attack()
            time.sleep(1)
            if Verify_Find_match():
                Find_match()
                time.sleep(5)
                pyautogui.keyDown("ctrl")
                pyautogui.scroll(-500)
                pyautogui.keyUp("ctrl")
                x, y = pyautogui.size()
                pyautogui.moveTo(x // 2, y // 2, 0.2)
                pyautogui.dragTo(200, 800, duration=0.2, button='left')
                if Verify_Edrag():
                    while Verify_Edrag() == True:
                        Edrag()
                        Deploy_Troops()
                time.sleep(50)
                if Verify_connection():
                    Try_again()
                if Verify_Surrender():
                    Surrender
                    time.sleep(2)
                if Verify_End_Battle():
                    End_Battle()
                if Verify_Okay():
                    Okay()
                    time.sleep(2)
                if Verify_Return_Home():
                    Return_Home()
                    time.sleep(5)
main()