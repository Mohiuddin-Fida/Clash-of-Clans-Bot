import cv2
import numpy as np
import pyautogui
import random
import math
import time
import keyboard
import win32gui
import win32con

screen_width, screen_height = pyautogui.size()

def bring_forward(partial_title):
    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if partial_title.lower() in title.lower():
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(hwnd)
                time.sleep(0.3)
                window_rect = win32gui.GetWindowRect(hwnd)
                screen_width, screen_height = pyautogui.size()
                x, y, w, h = window_rect
                window_width = w - x
                window_height = h - y
                if abs(window_width - screen_width) > 5 or abs(window_height - screen_height) > 5:
                    pyautogui.press('f11')
    win32gui.EnumWindows(enum_handler, None)

class Error_Handling:
    
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

    def handle():
        handled = False
        while True:
            if Error_Handling.Verify_connection():
                Error_Handling.Try_again()
                time.sleep(8)
                if Error_Handling.Verify_connection():
                    handled = False
                else:
                    handled = True
                    continue
            if Error_Handling.Verify_Quit():
                Error_Handling.Quit()
                time.sleep(2)
                handled = True
                continue
            break
        return handled

class Main_Base_Attack:

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

    def Verify_Match_Found():
        time.sleep(0.2)
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
        template = cv2.imread("Match_Found.jpg", cv2.IMREAD_GRAYSCALE)
        result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
        return cv2.minMaxLoc(result)[1] >= 0.8

    def Verify_Edrag():
        time.sleep(0.2)
        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
        template = cv2.imread("Edrag.jpg", cv2.IMREAD_GRAYSCALE)
        result = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
        return cv2.minMaxLoc(result)[1] >= 0.6

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
        if max_val >= 0.6:
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

    def Start():
        if Main_Base_Attack.Verify_Attack():
            Main_Base_Attack.Attack()
            time.sleep(0.5)
            if Main_Base_Attack.Verify_Find_match():
                Main_Base_Attack.Find_match()
                start_time = time.time()
                while not Main_Base_Attack.Verify_Match_Found():
                    if time.time() - start_time > 10:
                        Main_Base_Attack.End()
                        return
                    time.sleep(1)
                time.sleep(0.5)
                pyautogui.keyDown("ctrl")
                pyautogui.scroll(-500)
                pyautogui.keyUp("ctrl")
                pyautogui.moveTo(screen_width//2, screen_height//2)
                time.sleep(0.5)
                pyautogui.mouseDown(button='left')
                pyautogui.moveRel(-300, 400, duration=1)
                pyautogui.mouseUp(button='left')
                time.sleep(0.5)
                if Main_Base_Attack.Verify_Edrag():
                    Main_Base_Attack.Edrag()
                while True:
                    Main_Base_Attack.Deploy_Troops()
                    time.sleep(0.5)
                    if Main_Base_Attack.Verify_Edrag():
                        break
                time.sleep(60)

    def End():
        if Main_Base_Attack.Verify_Surrender():
            Main_Base_Attack.Surrender()
        elif Main_Base_Attack.Verify_End_Battle():
            Main_Base_Attack.End_Battle()
        time.sleep(2)
        if Main_Base_Attack.Verify_Okay():
            Main_Base_Attack.Okay()
        time.sleep(2)
        if Main_Base_Attack.Verify_Return_Home():
            Main_Base_Attack.Return_Home()

def main():
    bring_forward("LDPlayer")
    time.sleep(1)
    while not keyboard.is_pressed('q'):
        Error_Handling.handle()
        Main_Base_Attack.Start()
        Error_Handling.handle()
        Main_Base_Attack.End()    
main()