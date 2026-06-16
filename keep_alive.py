import ctypes
import threading
import time
import sys
import customtkinter as ctk

# Windows-System-Flags
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

class KeepAliveApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Fenster-Einstellungen
        self.title("Screen Keep-Alive")
        self.geometry("400x250")
        ctk.set_appearance_mode("System")  # Erkennt automatisch Dark/Light Mode
        ctk.set_default_color_theme("blue")

        self.is_running = False
        self.keep_alive_thread = None

        # --- UI ELEMENTE ---
        # Titel
        self.title_label = ctk.CTkLabel(self, text="Screen Keep-Alive Menü", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=20)

        # Status-Anzeige
        self.status_label = ctk.CTkLabel(self, text="Status: Gestoppt", text_color="red", font=ctk.CTkFont(size=14))
        self.status_label.pack(pady=10)

        # Start / Stopp Button
        self.btn_toggle = ctk.CTkButton(self, text="Programm Starten", command=self.toggle_keep_alive, fg_color="green", hover_color="darkgreen")
        self.btn_toggle.pack(pady=15)

        # Beenden Button (Schließt die ganze App sauber)
        self.btn_exit = ctk.CTkButton(self, text="App Schließen", command=self.quit_app, fg_color="#333333", hover_color="#555555")
        self.btn_exit.pack(pady=5)

    def toggle_keep_alive(self):
        if not self.is_running:
            # Starten
            self.is_running = True
            self.status_label.configure(text="Status: Aktiviert (Bildschirm bleibt an)", text_color="green")
            self.btn_toggle.configure(text="Programm Stoppen", fg_color="red", hover_color="darkred")
            
            # Hintergrund-Thread starten, damit das Fenster nicht einfriert
            self.keep_alive_thread = threading.Thread(target=self.run_keep_alive, daemon=True)
            self.keep_alive_thread.start()
        else:
            # Stoppen
            self.is_running = False
            self.status_label.configure(text="Status: Gestoppt", text_color="red")
            self.btn_toggle.configure(text="Programm Starten", fg_color="green", hover_color="darkgreen")
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

    def run_keep_alive(self):
        while self.is_running:
            # Sende das Signal an Windows
            ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_DISPLAY_REQUIRED | ES_SYSTEM_REQUIRED)
            time.sleep(1)

    def quit_app(self):
        self.is_running = False
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    app = KeepAliveApp()
    app.mainloop()
