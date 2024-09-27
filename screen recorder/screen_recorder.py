# Import benötigter Module
import pyautogui
import cv2
import numpy as np
 
# Festlegen der Auflösung
resolution = (1920, 1080)
 
# Festlegen des Codecs
codec = cv2.VideoWriter_fourcc(*"XVID")
 
# Festlegen des Dateinamens
filename = "Recording.avi"
 
# Festlegen der Framerate
fps = 60.0
 
# Anlegen eines VideoWriter Objekts
out = cv2.VideoWriter(filename, codec, fps, resolution)
 
# Anlegen eines leeren Fensters
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
 
# Skalierung des Fensters
cv2.resizeWindow("Live", 480, 270)
 
while True:
    # Screenshot erstellen mit PYautoGui
    img = pyautogui.screenshot()
 
    # Screenshot in ein Array umwandeln
    frame = np.array(img)
 
    # Umwandeln von BGR(Blue, Green, Red) zu RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
    # Ausgeben in die Output-Datei
    out.write(frame)
     
    # Optional: Anzeigen des Aufnahmebilds
    cv2.imshow('Live', frame)
     
    # Beenden der Aufnahme mit "q"-Taste
    if cv2.waitKey(1) == ord('q'):
        break
 
# Ausgabe des VideoWriters
out.release()
 
# Alle Fenster schliessen
cv2.destroyAllWindows()