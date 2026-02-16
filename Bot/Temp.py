import os
import cv2
import numpy as np
import pyautogui
import math
import time
import threading
import tkinter as tk
from tkinter import scrolledtext
from queue import Queue
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class BotConfig:
    def __init__(self):
        self.stop_event = threading.Event()
        self.log_queue = Queue()

    def log(self, message):
        self.log_queue.put(f"{time.strftime('%H:%M:%S')} | {message}\n")

    def is_running(self):
        return not self.stop_event.is_set()

    def stop(self):
        self.stop_event.set()

config = BotConfig()

# --- Original Logic (Adapted) ---
def Image_path(name):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Images")
    full_path = os.path.join(path, f"{name}.png")
    return full_path if os.path.exists(full_path) else None

def Verify(path, threshold=0.8):
    if not path or not config.is_running(): return None
    temp = cv2.imread(path, 0)
    if temp is None: return None
    scr = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2GRAY)
    h, w = temp.shape[:2]
    for s in np.linspace(0.5, 1.5, 20):
        if not config.is_running(): return None
        rw, rh = int(w * s), int(h * s)
        if rw > scr.shape[1] or rh > scr.shape[0]: continue
        res = cv2.matchTemplate(scr, cv2.resize(temp, (rw, rh)), cv2.TM_CCOEFF_NORMED)
        _, val, _, loc = cv2.minMaxLoc(res)
        if val >= threshold:
            return (loc[0] + rw//2, loc[1] + rh//2)
    return None

def Click(name_path):
    pos = Verify(name_path)
    if pos:
        pyautogui.click(pos)
        return True
    return False

def deploy_grid(x1=880, y1=120, x2=1575, y2=667):
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy, ox, oy = (x2-x1)/d, (y2-y1)/d, (y1-y2)/d*40, (x2-x1)/d*40
    for j in range(-2, 1):
        if not config.is_running(): return
        n = 8 if j == 0 else 5
        for i in range(n + 1):
            t, s = i/n, 50
            px = x1 + ux*s + ox*j + t*(x2 - x1 - 2*ux*s)
            py = y1 + uy*s + oy*j + t*(y2 - y1 - 2*uy*s)
            pyautogui.click(px, py)
            time.sleep(0.01)

def Status(path, threshold=0.85):
    pos = Verify(path, threshold)
    if not pos: return False
    x, y = pos
    img = pyautogui.screenshot(region=(x-15, y-15, 30, 30))
    img_np = np.array(img)
    r, g, b = img_np[:,:,0], img_np[:,:,1], img_np[:,:,2]
    saturation = np.mean(np.abs(r.astype(int) - g.astype(int)) + np.abs(g.astype(int) - b.astype(int)))
    return saturation > 15

def Error():
    if Click(Try_again): time.sleep(1)
    if Click(Cross): time.sleep(1)
    if Click(Okay): time.sleep(1)

def Deploy():
    config.log("Attempting deployment...")
    w, h = pyautogui.size()
    cx, cy = w//2, h//2
    pyautogui.click(cx, cy)
    time.sleep(0.25)
    pyautogui.keyDown('ctrl')
    pyautogui.scroll(-1000)
    pyautogui.keyUp('ctrl')
    time.sleep(0.25)
    pyautogui.click(cx, cy)
    pyautogui.dragTo(w*0.1, h*0.9, duration=1, button='left')
    time.sleep(0.2)
    if Click(E_drag):
        time.sleep(0.5)
        while Status(E_drag) and config.is_running():
            deploy_grid()
            if Verify(End_battle): break
    Hero_list = [King, Queen, Rc, Warden, Seige]
    for hero in Hero_list:
        if not config.is_running(): break
        if Click(hero):
            time.sleep(0.3)
            deploy_grid()
            time.sleep(0.1)
    if Click(Bat_spell):
        time.sleep(0.5)
        while Status(Bat_spell) and config.is_running():
            deploy_grid()
            if Verify(End_battle): break
    time.sleep(45)
    config.log("Deployment finished.")

def bot_loop():
    while config.is_running():
        Error()
        if Click(Attack_main):
            time.sleep(1)
            if Click(Find_match):
                time.sleep(1)
                if Click(Attack_troops):
                    while not Verify(Next) and config.is_running():
                        time.sleep(0.5)
                    if config.is_running():
                        config.log("Match found!")
                        Deploy()
                        Error()
                        Click(Surrender)
                        Click(End_battle)
                        time.sleep(0.5)
                        Click(Okay)
                        time.sleep(0.5)
                        Click(Return_home)
                        time.sleep(0.5)
        time.sleep(1)

# --- Image Globals ---
Attack_main   = Image_path("Attack_main")
Attack_troops = Image_path("Attack_Troops")
Bat_spell     = Image_path("Bat_Spell")
Cross         = Image_path("Cross")
E_drag        = Image_path("E-Drag")
End_battle    = Image_path("End_Battle")
Find_match    = Image_path("Find")
King          = Image_path("King")
Next          = Image_path("Next_In_Battle")
Queen         = Image_path("Queen")
Rc            = Image_path("RC")
Return_home   = Image_path("Return_Home")
Seige         = Image_path("Seige")
Try_again     = Image_path("Try_Again")
Warden        = Image_path("Warden")
Surrender     = Image_path("Surrender")
Okay          = Image_path("Okay")

# --- UI Implementation ---
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Control Panel")
        self.root.geometry("500x600")
        self.root.configure(bg="#1a1a1a")
        
        # Style
        self.btn_fg = "#ffffff"
        self.btn_bg = "#333333"
        self.log_bg = "#0d0d0d"
        self.log_fg = "#00ff41"
        
        # Header
        lbl = tk.Label(root, text="System Status: Online", bg="#1a1a1a", fg="#ffffff", font=("Consolas", 12))
        lbl.pack(pady=10)
        
        # Log Window
        self.log_box = scrolledtext.ScrolledText(root, bg=self.log_bg, fg=self.log_fg, font=("Consolas", 9))
        self.log_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Controls
        btn_frame = tk.Frame(root, bg="#1a1a1a")
        btn_frame.pack(pady=10)
        
        self.start_btn = tk.Button(btn_frame, text="Start", command=self.start_bot, bg="#2b5c2b", fg="#ffffff", width=10)
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_btn = tk.Button(btn_frame, text="Stop", command=self.stop_bot, bg="#5c2b2b", fg="#ffffff", width=10)
        self.stop_btn.pack(side=tk.LEFT, padx=10)
        
        self.thread = None
        self.update_log()
        
    def update_log(self):
        while not config.log_queue.empty():
            msg = config.log_queue.get()
            self.log_box.insert(tk.END, msg)
            self.log_box.see(tk.END)
        self.root.after(100, self.update_log)
        
    def start_bot(self):
        if self.thread and self.thread.is_alive():
            return
        config.stop_event.clear()
        self.thread = threading.Thread(target=bot_loop, daemon=True)
        self.thread.start()
        config.log("System initiated. I'm watching.")
        
    def stop_bot(self):
        config.stop()
        config.log("System halted. Rest now.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()