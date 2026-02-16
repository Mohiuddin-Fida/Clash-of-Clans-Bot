import os, cv2, numpy as np, pyautogui, math, time

def Image_path(name):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Images")
    full_path = os.path.join(path, f"{name}.png")
    return full_path if os.path.exists(full_path) else None

def Verify(path, threshold=0.8):
    if not path: return None
    temp = cv2.imread(path, 0)
    if temp is None: return None
    scr = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2GRAY)
    h, w = temp.shape[:2]
    for s in np.linspace(0.5, 1.5, 20):
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
    print("Attempting deployment...")
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
        while Status(E_drag):
            deploy_grid()
            if Verify(End_battle): break
    Hero_list = [King, Queen, Rc, Warden, Seige]
    for hero in Hero_list:
        if Click(hero):
            time.sleep(0.3)
            deploy_grid()
            time.sleep(0.1)
    if Click(Bat_spell):
        time.sleep(0.5)
        while Status(Bat_spell):
            deploy_grid()
            if Verify(End_battle): break
    time.sleep(45)
    print("Deployment finished.")
    

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

time.sleep(3)

while True:
    Error()
    if Click(Attack_main):
        time.sleep(1)
        if Click(Find_match):
            time.sleep(1)
            if Click(Attack_troops):
                while not Verify(Next):
                    time.sleep(0.5)
                print("Match found!")
                Deploy()
                Error()
                Click(Surrender)
                Click(End_battle)
                time.sleep(0.5)
                Click(Okay)
                time.sleep(0.5)
                Click(Return_home)
                time.sleep(0.5)