totale = float(input("Inserisci il totale della spesa: "))

if totale < 50:
    pass
elif totale < 100:
    totale = totale * 0.9
else:
    totale = totale * 0.8

print("Totale da pagare:", totale)
