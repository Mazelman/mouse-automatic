import ctypes
import time
import sys

# Windows-System-Flags definieren
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

print("System-Keep-Alive aktiv (Nativer Windows-Modus). Drücke STRG+C zum Beenden.")

try:
    # Teilt Windows direkt im Systemkern mit, dass der Bildschirm AN bleiben muss
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_DISPLAY_REQUIRED | ES_SYSTEM_REQUIRED)
    
    while True:
        time.sleep(60)  # Das Skript schläft, aber Windows blockiert den Standby-Modus aktiv

except KeyboardInterrupt:
    # Setzt die Energiespareinstellungen beim Schließen wieder zurück
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
    print("\nProgramm erfolgreich beendet.")
    sys.exit()
