import pywhatkit
import pyautogui
import time 

# Replace with the full number including country code (e.g., +91XXXXXXXXXX)
p = "+91XXXXXXXXXX"
m = "This is an automated message"
h = 20  # Hour (24h format)
min = 9  # Minute

pywhatkit.sendwhatmsg(p, m, h, min)
time.sleep(20)
pyautogui.press('enter')
