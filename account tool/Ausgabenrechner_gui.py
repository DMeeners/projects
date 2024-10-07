from tkinter import *
from Ausgabenrechner_Klassen import Account

# globale Variable
current_account = None

# Funktion zum Hinzufügen eines Accounts
def add_account():
    global current_account
    try:
        # Kontoinformationen per Getter-Methode aus den Entry-Fields beziehen
        account_nr = int(ent_account_nr.get())
        holder = str(ent_holder.get())
        balance = float(ent_balance.get())

        # Neue Account-Instanz anlegen
        current_account = Account(account_nr, holder, balance)

        # Labels mit Kontoinformationen aktualisieren
        lbl_account_nr.config(text=f"Kontonummer: {current_account.account_nr}")
        lbl_account_holder.config(text=f"Kontoinhaber: {current_account.holder}")
        lbl_account_balance.config(text=f"Kontostand(Start): {current_account.balance}€")

        # Entry-Fields leeren
        ent_account_nr.delete(0, END)
        ent_holder.delete(0, END)
        ent_balance.delete(0, END)

        # Freigabe der Einkommen-/Ausgabebuttons
        btn_income.config(state=NORMAL)
        btn_expense.config(state=NORMAL)

        # Textbox leeren
        result_txt.delete(1.0, END)
    # Error abfangen    
    except ValueError:
        result_txt.insert(END, "Ungültige Eingabewerte für den Account\n")

# Funktion zum Hinzufügen von Einkommen
def add_income():
    if current_account:
        try:
            value = float(ent_income.get())  
            current_account.income(value)
            result_txt.insert(END, f"Buchung: {ent_incomekind.get()}, Betrag: {ent_income.get()}\n", "income")
            update_labels()
        # Error abfangen     
        except ValueError:
            result_txt.insert(END, "Ungültiger Wert für Einnahmen\n")
        
        # Entry-Fields leeren nach Buttonclick
        ent_income.delete(0, END)
        ent_incomekind.delete(0, END)

# Funktion zum Abziehen von Ausgaben
def add_expense():
    if current_account:
        try:
            value = float(ent_income.get())
            current_account.expense(value)
            result_txt.insert(END, f"Buchung: {ent_incomekind.get()}, Betrag: {ent_income.get()}\n", "expense")
            update_labels()
        except ValueError:
            result_txt.insert(END, "Ungültiger Wert für Ausgaben\n")
        
        # Entry-Fields leeren nach Buttonclick
        ent_income.delete(0, END)
        ent_incomekind.delete(0, END)

# Funktion zum Aktualisieren der Labels für Einkommen, Ausgaben und aktualisiertem Kontostand
def update_labels():
    lbl_total_income.config(text=f"Gesamteinnahmen: {current_account.sum_income}€")
    lbl_total_expense.config(text=f"Gesamtausgaben: {current_account.sum_expense}€")
    lbl_updated_balance.config(text=f"Neuer Kontostand: {current_account.total_balance()}€")

# Festlegen des Hauptfensters
gui = Tk()
gui.title("Kontoführungs-Tool")
gui.geometry("700x700")

# Entry-Fields for Account Creation
lbl_create_account = Label(master=gui, text="Kontoführungs-Tool", font=("Arial", 12, "bold"))
lbl_create_account.grid(row=0, columnspan=4, pady=10)

lbl_account_nr = Label(master=gui, text="Kontonummer:")
lbl_account_nr.grid(row=1, column=0, sticky="W", padx=5, pady=1)
ent_account_nr = Entry(master=gui)
ent_account_nr.grid(row=1, column=1, padx=5)

lbl_holder = Label(master=gui, text="Kontoinhaber:")
lbl_holder.grid(row=2, column=0, sticky="W", padx=5, pady=1)
ent_holder = Entry(master=gui)
ent_holder.grid(row=2, column=1, padx=5)

lbl_balance = Label(master=gui, text="Kontostand(Start):")
lbl_balance.grid(row=3, column=0, sticky="W", padx=5, pady=1)
ent_balance = Entry(master=gui)
ent_balance.grid(row=3, column=1, padx=5)

# Button um Konto hinzuzufügen
btn_add_account = Button(master=gui, text="Konto hinzufügen", command=add_account)
btn_add_account.grid(row=3, column=2, padx=10)

# Labels mit Account Informationen
lbl_account_nr = Label(master=gui, text="Kontonummer: ")
lbl_account_nr.grid(row=4, columnspan=4, sticky="W", padx=5, pady=1)
lbl_account_holder = Label(master=gui, text="Kontoinhaber: ")
lbl_account_holder.grid(row=5, columnspan=4, sticky="W", padx=5, pady=1)
lbl_account_balance = Label(master=gui, text="Kontostand(Start): ")
lbl_account_balance.grid(row=6, columnspan=4, sticky="W", padx=5, pady=1)

# Label für das Entry-Field der Einkommens- bzw. Ausgabenart
lbl_ent_incomekind = Label(master=gui, text="Buchungstext: ")
lbl_ent_incomekind.grid(row=7, column=0, sticky="W", padx=5, pady=1)
# Entry_Field für die Eingabe der Einkommens- bzw. Ausgabenart
ent_incomekind = Entry(master=gui, width=8)
ent_incomekind.grid(row=7, column=1, padx=5)
# Label für das Entry-Field der Summen
lbl_ent_income = Label(master=gui, text="Summe: ")
lbl_ent_income.grid(row=8, column=0, sticky="W", padx=5, pady=1)
# Entry-Field für die Summen
ent_income = Entry(master=gui, width=8)
ent_income.grid(row=8, column=1, padx=5)
# Button zum Ausführen der Einkommensfunktion
btn_income = Button(master=gui, text="Einnahme", bg="green", command=add_income, state=DISABLED)
btn_income.grid(row=8, column=2)
# Button zum Ausführen der Ausgabenfunktion
btn_expense = Button(master=gui, text="Ausgabe", bg="red", command=add_expense, state=DISABLED)
btn_expense.grid(row=8, column=3)

# Textfeld zur Ausgabe
result_txt = Text(master=gui, height=20, width=50)
result_txt.grid(row=9, columnspan=4, padx=5, pady=2)

# Farbe des Text in Abhängigkeit der Buchung
result_txt.tag_configure("income", foreground="green")
result_txt.tag_configure("expense", foreground="red")

# Labels für Gesamteinnahmen, Gesamtausgaben und aktualisierter Kontostand
lbl_total_income = Label(master=gui, text="Gesamteinnahmen: 0€")
lbl_total_income.grid(row=10, columnspan=4, sticky="W", padx=5, pady=1)
lbl_total_expense = Label(master=gui, text="Gesamtausgaben: 0€")
lbl_total_expense.grid(row=11, columnspan=4, sticky="W", padx=5, pady=1)
lbl_updated_balance = Label(master=gui, text="Neuer Kontostand: 0€", font=("bold"))
lbl_updated_balance.grid(row=12, columnspan=4, sticky="W", padx=5, pady=1)

# mainloop
gui.mainloop()