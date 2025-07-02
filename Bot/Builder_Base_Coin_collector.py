import pyautogui
import time
import random
time.sleep(2)


def random_point_in_triangle(p1, p2, p3):
    u = random.random()
    v = random.random()
    if u + v > 1:
        u = 1 - u
        v = 1 - v
    x = p1[0] + u * (p2[0] - p1[0]) + v * (p3[0] - p1[0])
    y = p1[1] + u * (p2[1] - p1[1]) + v * (p3[1] - p1[1])
    return (x, y)


t1 = [(314, 505), (400, 448), (443, 604)]
t2 = [(400, 448), (443, 604), (525, 560)]
pt1 = random_point_in_triangle(*t1)
pt2 = random_point_in_triangle(*t2)


def Spawn():
    p1 = (324, 215)
    p2 = (456, 125)
    p3 = (531, 182)
    p4 = (398, 284)

    def interpolate(a, b, t):
        return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    s = random.random()
    t = random.random()
    if s + t > 1:
        s = 1 - s
        t = 1 - t
    a = interpolate(p1, p2, s)
    b = interpolate(p1, p4, t)
    x, y = interpolate(a, b, random.random())
    return (int(x), int(y))


def main():
    while True:
        try:
            if pyautogui.locateOnScreen("Attack.png", confidence=0.8):
                pyautogui.click(pyautogui.locateOnScreen("Attack.png", confidence=0.8))
                time.sleep(0.5)
        except:  
            flag = True
        try:      
            if pyautogui.locateOnScreen("Find.png", confidence=0.8):
                pyautogui.click(pyautogui.locateOnScreen("Find.png", confidence=0.8))
        except:
                time.sleep(10)
                pyautogui.leftClick(190, 970)
                pyautogui.leftClick(Spawn())
                time.sleep(0.2)
                pyautogui.leftClick(358, 970)
                pyautogui.leftClick(Spawn())
                time.sleep(0.2)
                pyautogui.leftClick(514, 970)
                pyautogui.leftClick(Spawn())
                time.sleep(0.2)
                pyautogui.leftClick(671, 970)
                pyautogui.leftClick(Spawn())
                time.sleep(0.2)
                pyautogui.leftClick(817, 970)
                pyautogui.leftClick(Spawn())
                time.sleep(0.2)
                pyautogui.leftClick(969, 970)
                pyautogui.leftClick(Spawn())
                time.sleep(0.2)
                pyautogui.leftClick(1125, 970)
                pyautogui.leftClick(Spawn())
                while True:
                    try:
                        if pyautogui.locateOnScreen("Stage2.png", confidence=0.8):
                            break
                    except:
                        pass
                    try:
                        if pyautogui.locateOnScreen("return.png", confidence=0.8):
                            pyautogui.leftClick(pyautogui.locateOnScreen("return.png"))
                            time.sleep(5)
                            return main()
                    except:
                        pass

main()