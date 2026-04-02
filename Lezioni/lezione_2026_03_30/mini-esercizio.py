"""
Presa una lista di numeri, dire per ogni numero se è pari o dispari

I numeri dispari hanno resto 1 della divisione per 2
"""
lista_numeri = [1, 2, 3.4, 3.5, 10, 20, 30]
for numero in lista_numeri:
    tipologia = "pari"  # Diamo questa tipologia di default
    # Vediamo se dobbiamo smentire la tipologia di default
    if numero % 2 != 0:  # Se il resto della divisione per 2 non è 0
        tipologia = "dispari"  # Allora il numero è dispari

    print(f"Il numero {numero} è {tipologia}")



