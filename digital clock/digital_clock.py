# Import benötigter Module
from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import date
import locale
locale.setlocale(locale.LC_TIME,"de_DE")

# Fenster erstellen
root = Tk()
root.title("Digitale Uhr")

# Funktion zum Abrufen der Zeit und des Datums
def time():
    datum = date.today()
    uhrzeit = strftime('%H:%M:%S')
    datum = strftime('%A, %d.%m.%Y')
    lbl_uhrzeit.config(text=uhrzeit)
    lbl_datum.config(text=datum)
    root.after(1000, time)

# Funktion zum Skalieren des Labels anhand der Fenstergröße
def skal():
        new_size_uhr = min(event.width // 10, event.height // 4)
        new_size_datum = min(event.width // 20, event.height // 8)
        lbl_uhrzeit.config(font=('calibri', new_size_uhr, 'bold'))
        lbl_datum.config(font=('calibri', new_size_datum))

# Design der Uhr
lbl_uhrzeit = Label(root, font=('calibri', 40, 'bold'),
                    background='DarkBlue', foreground='white')
lbl_datum = Label(root, font=('calibri', 20),
                  background='DarkBlue', foreground='white')

# Positionierung im Fenster
lbl_uhrzeit.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
lbl_datum.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

# Spalten und Zeilen des Gitters expandierbar machen
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Binde das Fenster-Resize-Ereignis an die resize_font-Funktion
root.bind('<Configure>', skal)

# Funktionsaufruf und main
time()
mainloop()