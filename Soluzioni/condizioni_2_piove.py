piove = True
ritardo = False

if piove and ritardo:
    print("Piove e sono in ritardo: uso la macchina")

if piove or not ritardo:
    print("Piove o non sono in ritardo: uso la macchina")

if not piove and not ritardo:
    print("Non piove e non sono in ritardo: vado a piedi")
