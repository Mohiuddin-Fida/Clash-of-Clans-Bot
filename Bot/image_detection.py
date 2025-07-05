import pytesseract as pyt
import numpy as np
import cv2
import pyautogui
import time
import os
pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(3)

pyautogui.leftClick(1794, 949)
pyautogui.leftClick(1201, 106)

time.sleep(0.5)
coin_region = (540, 1005, 183, 34)
img = pyautogui.screenshot(region=coin_region)
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
cv2.imwrite(r'C:\Users\Cacada 3301\Documents\Python\Coin.png', img)

time.sleep(0.5)
elixir_region = (855, 1005, 183, 34)
img2 = pyautogui.screenshot(region=elixir_region)
img2 = cv2.cvtColor(np.array(img2), cv2.COLOR_RGB2BGR)
cv2.imwrite(r'C:\Users\Cacada 3301\Documents\Python\Elixir.png', img2)


img = cv2.imread("Coin.png")
Builder_Base_Coins = pyt.image_to_string(img)
print("Builder Base Coins:", Builder_Base_Coins)


img2 = cv2.imread("Elixir.png")
Builder_Base_Elixier = pyt.image_to_string(img2)
print("Builder Base Elixir:", Builder_Base_Elixier)


# os.remove(r"C:\Users\Cacada 3301\Documents\Python\Coin.png")

# os.remove(r"C:\Users\Cacada 3301\Documents\Python\Elixir.png")
