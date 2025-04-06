import os
import time

try:
    os.system("taskkill /f /im chrome.exe")
    time.sleep(1)
except:pass