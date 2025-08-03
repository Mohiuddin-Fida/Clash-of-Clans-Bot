import cv2
import numpy as np
import pyautogui
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
                time.sleep(0.3)
                window_rect = win32gui.GetWindowRect(hwnd)
                screen_width, screen_height = pyautogui.size()
                x, y, w, h = window_rect
                window_width = w - x
                window_height = h - y
                if abs(window_width - screen_width) > 5 or abs(window_height - screen_height) > 5:
                    pyautogui.press('f11')
    win32gui.EnumWindows(enum_handler, None)

def match_image(image_path):
    time.sleep(0.2)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2GRAY)
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print(f"[ERROR] Template not found: {image_path}")
        return None, None, None
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    return template, result, cv2.minMaxLoc(result)

class Error_Handling:

    def Verify_connection():
        _, _, (_, max_val, _, _) = match_image("images/Try_again.jpg")
        return max_val >= 0.8

    def Try_again():
        template, _, (_, max_val, _, max_loc) = match_image("images/Try_again.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)

    def Verify_Cross():
        _, _, (_, max_val, _, _) = match_image("images/Cross.jpg")
        return max_val >= 0.8

    def Cross():
        template, _, (_, max_val, _, max_loc) = match_image("images/Cross.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)

    def Handle():
        retries = 0
        while True:
            if Error_Handling.Verify_connection():
                Error_Handling.Try_again()
                retries += 1
            elif Error_Handling.Verify_Cross():
                Error_Handling.Cross()
                retries += 1
            else:
                break
            time.sleep(3)
            if retries >= 10:
                break

class Main_Base:

    def Attack():
        template, _, (_, max_val, _, max_loc) = match_image("images/Attack.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)

    def Find_match():
        template, _, (_, max_val, _, max_loc) = match_image("images/Find_match.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)

    def Match_found():
        _, _, (_, max_val, _, _) = match_image("images/Next.jpg")
        return max_val >= 0.8

    def Edrag():
        template, _, (_, max_val, _, max_loc) = match_image("images/Edrag.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)       

    def King():
        template, _, (_, max_val, _, max_loc) = match_image("images/Barbarian_king.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)

    def Queen():
        template, _, (_, max_val, _, max_loc) = match_image("images/Archer_queen.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)

    def Warden():
        template, _, (_, max_val, _, max_loc) = match_image("images/Grand_warden.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)

    def Prince():
        template, _, (_, max_val, _, max_loc) = match_image("images/Minion_prince.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)                        

    def RC():# complete 
        template, _, (_, max_val, _, max_loc) = match_image("images/Royal_champion.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)         

    def Bat_spell():
        template, _, (_, max_val, _, max_loc) = match_image("images/Bat_spell.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2) 

    def seige():
        template, _, (_, max_val, _, max_loc) = match_image("images/Siege_barracks.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2) 

    def seige_empty():
        template, _, (_, max_val, _, max_loc) = match_image("images/Siege_barracks_empty.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)         

    def Deploy(count):
        x1, y1 = 970, 45
        x2, y2 = 1720, 614
        for i in range(count + 1):
            t = i / count
            x = x1 + (x2 - x1) * t
            y = y1 + (y2 - y1) * t
            pyautogui.click(x, y)

    def End_battle():
        template, _, (_, max_val, _, max_loc) = match_image("images/End_battle.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)

    def Surrender():
        template, _, (_, max_val, _, max_loc) = match_image("images/Surrender.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)

    def Okay():
        template, _, (_, max_val, _, max_loc) = match_image("images/Okay.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)

    def Return_home():
        template, _, (_, max_val, _, max_loc) = match_image("images/Return_home.jpg")
        if max_val >= 0.8:
            h, w = template.shape
            pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2, duration=0.2)

    def set_field():
        screen_width, screen_height = pyautogui.size()
        pyautogui.click(screen_width//2, screen_height//2)
        time.sleep(0.5)
        pyautogui.keyDown("ctrl")
        pyautogui.scroll(-3000)
        pyautogui.keyUp("ctrl")
        time.sleep(0.5)
        pyautogui.mouseDown(button='left')
        pyautogui.moveRel(-300, 400, duration=1)
        pyautogui.mouseUp(button='left')
        time.sleep(0.5)


def main():
    bring_forward("LDPlayer")
    time.sleep(1)
    while not keyboard.is_pressed('q'):
        Error_Handling.Handle()
        Main_Base.set_field()
        Main_Base.Deploy(10)
main()