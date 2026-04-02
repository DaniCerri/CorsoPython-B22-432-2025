angolo = int(input("Inserisci l'ampiezza dell'angolo in gradi: "))

if angolo < 90:
    print("Angolo Acuto")
elif angolo == 90:
    print("Angolo Retto")
else:
    print("Angolo Ottuso")
