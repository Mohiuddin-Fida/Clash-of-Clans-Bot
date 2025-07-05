import pytesseract as pyt
import pyautogui
import time
pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(3)

pyautogui.leftClick(1794, 949)
pyautogui.leftClick(1201, 106)

coin_region = (540, 1005, 183, 34)
img = pyautogui.screenshot(region=coin_region)

elixir_region = (855, 1005, 181, 34)
img2 = pyautogui.screenshot(region=elixir_region)


Builder_Base_Coins = pyt.image_to_string(img)


Builder_Base_Elixir = pyt.image_to_string(img2)

Builder_Base_Coins = Builder_Base_Coins.replace(' ', '')
Builder_Base_Elixir = Builder_Base_Elixir.replace(' ', '')

print("Builder Base Coins:", Builder_Base_Coins)
print("Builder Base Elixir:", Builder_Base_Elixir)
