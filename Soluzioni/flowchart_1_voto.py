voto = int(input("Inserisci il voto dell'esame: "))

if voto < 18:
    print("Non superato")
elif voto == 30:
    print("Eccellente")
else:
    print("Superato")
