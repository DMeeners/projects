# Import benötigter Module
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

#Funktion zum Aufruf der Widgets
def Widgets():
 
    head_label = Label(root, text="YouTube Downloader by dmeeners",
                       padx=15,
                       pady=15,
                       font="SegoeUI 14",
                       bg="darkblue",
                       fg="white")
    head_label.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=3)
 
    link_label = Label(root,
                       text="YouTube link :",
                       bg="red",
                       pady=5,
                       padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)
 
    root.linkText = Entry(root,
                          width=35,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)
 
 
    destination_label = Label(root,
                              text="Destination :",
                              bg="red",
                              pady=5,
                              padx=9)
    destination_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)
 
 
    root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=download_Path,
                                 font="Arial 14")
    root.destinationText.grid(row=3,
                              column=1,
                              pady=5,
                              padx=5)
 
 
    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="bisque",
                      relief=GROOVE)
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)
 
    Download_B = Button(root,
                        text="Download",
                        command=Download,
                        width=20,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)
    

# Funktion zur Auswahl des Speicherverzeichnisses

def Browse():
    # Pop-Up-Fenster
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")
 
    # Anzeige des Dateipfads
    download_Path.set(download_Directory)

# Funktion zum Starten des Downloads
def Download():
 
    # getter für Link
    Youtube_link = video_Link.get()
 
    # Aufruf zur Auswahl des Speicherverzeichnisses
    download_Folder = download_Path.get()
 
    # Objektaufruf mittels YouTube()
    getVideo = YouTube(Youtube_link)
 
    #getter für den ersten Stream des Videos
    videoStream = getVideo.streams.first()
 
    # Download-Aufruf in das gewählte Verzeichnis
    videoStream.download(download_Folder)
 
    # Ereignisanzeige
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)
 
# Tkinter Objektaufruf
root = tk.Tk()
 
# Festlegen der Fenstereigenschaften
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Downloader by dmeeners")
root.config(background="deepskyblue")
 
# Stringvariablen anlegen
video_Link = StringVar()
download_Path = StringVar()
 
# Auf der Widgets Funktion
Widgets()
 
# Programmaufruf
root.mainloop()
