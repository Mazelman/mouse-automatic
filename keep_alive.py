import time
import sys
import pyautogui

# Sicherheitsfeature: Maus in eine Ecke ziehen stoppt das Skript
pyautogui.FAILSAFE = True

print("Verbessertes Skript aktiv (Nutzt Shift-Taste). Drücke STRG+C zum Beenden.")

try:
    while True:
        # Drückt die Umschalt-Taste (Shift), was Windows garantiert wach hält
        pyautogui.press('shift')
        
        # Wartet 60 Sekunden bis zum nächsten Drücken
        time.sleep(60)
except KeyboardInterrupt:
    print("\nProgramm beendet.")
    sys.exit()
