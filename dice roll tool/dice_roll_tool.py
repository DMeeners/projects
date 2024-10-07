# Import benötigter Module
import tkinter as tk
import random

# Funktion zum Hinzufügen von Würfeln
def add_dice(dice_type, entry):
    global list_d6, list_d20, list_d10, list_dx, list_sides
    # Abfrage der Würfelmenge per Getter-Methode
    amount = int(entry.get())
    # Würfelabfrage und anschliessende Listenerweiterung
    if dice_type == "D6":
        for _ in range(amount):
            list_d6.append(random.randint(1, 6))
        result_text.insert(tk.END, f"{amount} D6-Würfel wurden erfolgreich hinzugefügt!\n")

    elif dice_type == "D10":
        for _ in range(amount):
            list_d10.append(random.randint(1, 10))
        result_text.insert(tk.END, f"{amount} D10-Würfel wurden erfolgreich hinzugefügt!\n")

    elif dice_type == "D20":
        for _ in range(amount):
            list_d20.append(random.randint(1, 20))
        result_text.insert(tk.END, f"{amount} D20-Würfel wurden erfolgreich hinzugefügt!\n")

    elif dice_type == "DX":
        for _ in range(amount):
            sides = int(dx_sideentry.get())
            list_sides.append(sides)
            result = random.randint(1, sides)
            list_dx.append(result)
        result_text.insert(tk.END, f"{amount} D{sides}-Würfel wurde erfolgreich hinzugefügt!\n")

# Funktion zum Würfelwurf
def roll_all():
    result_text.insert(tk.END, f"Würfelergebnisse (D6): {list_d6}\n")
    result_text.insert(tk.END, f"Gesamtsumme der D6-Würfel: {sum(list_d6)}\n")
    result_text.insert(tk.END, f"Würfelergebnisse (D10): {list_d10}\n")
    result_text.insert(tk.END, f"Gesamtsumme der D10-Würfel: {sum(list_d10)}\n")
    result_text.insert(tk.END, f"Würfelergebnisse (D20): {list_d20}\n")
    result_text.insert(tk.END, f"Gesamtsumme der D20-Würfel: {sum(list_d20)}\n")
    result_text.insert(tk.END, f"Würfelauswahl Custom dice: {list_sides}\n")
    result_text.insert(tk.END, f"Würfelergebnisse (custom): {list_dx}\n")
    result_text.insert(tk.END, f"Gesamtsumme der D20-Würfel: {sum(list_dx)}\n")
    result_text.insert(tk.END, f"Gesamtergebnis: {sum(list_d6 + list_d20 + list_d10 + list_dx)}\n")

# Funktion zum resetten
def clear_all():
    global list_d6, list_d20, list_d10, list_dx, list_sides
    list_d6 = []
    list_d20 = []
    list_d10 = []
    list_dx = []
    list_sides = []
    result_text.delete(1.0, tk.END)

# Funktion zum Akualisieren der Ergebnisse (redundant)
def update_results():
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Würfelergebnisse (D6): {list_d6}\n")
    result_text.insert(tk.END, f"Gesamtsumme der D6-Würfel: {sum(list_d6)}\n")
    result_text.insert(tk.END, f"Würfelergebnisse (D10): {list_d10}\n")
    result_text.insert(tk.END, f"Gesamtsumme der D10-Würfel: {sum(list_d10)}\n")
    result_text.insert(tk.END, f"Würfelergebnisse (D20): {list_d20}\n")
    result_text.insert(tk.END, f"Gesamtsumme der D20-Würfel: {sum(list_d20)}\n")
    result_text.insert(tk.END, f"Würfelauswahl Custom dice: {list_sides}\n")
    result_text.insert(tk.END, f"Würfelergebnisse (custom): {list_dx}\n")
    result_text.insert(tk.END, f"Gesamtsumme der D20-Würfel: {sum(list_dx)}\n")
    result_text.insert(tk.END, f"Gesamtergebnis: {sum(list_d6 + list_d20 + list_d10 + list_dx)}\n")

# Listen initialisieren
list_d6 = []
list_d20 = []
list_d10 = []
list_dx = []
list_sides = []

# Hauptfenster mit Titel festlegen
root = tk.Tk()
root.title("Dice Roller")

# Entry-Fields für alle Würfelarten
d6_label = tk.Label(root, text="D6 Anzahl:")
d6_label.grid(row=0, column=0)
d6_entry = tk.Entry(root)
d6_entry.grid(row=0, column=1)

d10_label = tk.Label(root, text="D10 Anzahl:")
d10_label.grid(row=1, column=0)
d10_entry = tk.Entry(root)
d10_entry.grid(row=1, column=1)

d20_label = tk.Label(root, text="D20 Anzahl:")
d20_label.grid(row=2, column=0)
d20_entry = tk.Entry(root)
d20_entry.grid(row=2, column=1)

dx_label = tk.Label(root, text="DX Anzahl / Seiten")
dx_label.grid(row=3, column=0)
dx_entry = tk.Entry(root)
dx_entry.grid(row=3, column=1)
dx_sideentry = tk.Entry(root)
dx_sideentry.grid(row=3, column=2)

# Buttons zum Hinzufügen der Würfel
add_d6_button = tk.Button(root, text="D6 hinzufügen", command=lambda: add_dice("D6", d6_entry))
add_d6_button.grid(row=0, column=3)

add_d10_button = tk.Button(root, text="D10 hinzufügen", command=lambda: add_dice("D10", d10_entry))
add_d10_button.grid(row=1, column=3)

add_d20_button = tk.Button(root, text="D20 hinzufügen", command=lambda: add_dice("D20", d20_entry))
add_d20_button.grid(row=2, column=3)

add_dx_button = tk.Button(root, text="DX hinzufügen", command=lambda: add_dice("DX", dx_entry))
add_dx_button.grid(row=3, column=3)

# Button zum Würfeln
roll_button = tk.Button(root, text="Würfeln", command=roll_all)
roll_button.grid(row=4, column=0)

# Button zum resetten
clear_button = tk.Button(root, text="Alle löschen", command=clear_all)
clear_button.grid(row=4, column=1)

# Button zum Aktualisieren
update_button = tk.Button(root, text="Ergebnisse aktualisieren", command=update_results)
update_button.grid(row=4, column=2)

# Textfeld zur Ausgabe der Würfelergebnisse
result_text = tk.Text(root, height=20, width=50)
result_text.grid(row=5, columnspan=3)

# mainloop
root.mainloop()
