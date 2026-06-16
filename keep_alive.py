import time
import sys
import pyautogui

# Sicherheitsfeature: Maus in eine Ecke ziehen stoppt das Skript
pyautogui.FAILSAFE = True

print("Maus-Skript aktiv. Drücke STRG+C zum Beenden.")

try:
    while True:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 1, y, duration=0.1)
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(60)
except KeyboardInterrupt:
    print("\nProgramm beendet.")
    sys.exit()
