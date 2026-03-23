"""
Fare una lista inizializzata con 7 numeri float e poi fare le seguenti cose:
1. Stampare la sottolista che va da elemento 2 a 5 escluso
2. Stampare la sottolista che va da elemento 2 a 5 incluso
3. Stampare quanto vale il secondo elemento elevato (**) al terzo elemento
4. Stampare quanto vale la somma tra primo ed ultimo elemento
5. Dire se il terzo elemento è maggiore di 10 (usando l'if -> se terzo elemento > 10: print("è maggiore di 10")
"""

# 0.
lista = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8]  # Creiamo la lista con 7 numeri float

# 1.
print(f"Lista con indici [2, 5): {lista[2:5]}")

# 2.
print(f"Lista con indici [2, 5] = [2, 6): {lista[2:6]}")

# 2. bis -> cosa facciamo se vogliamo stampare l'ultimo elemento della lista nella nostra sottolista?
# lista[2:7] non si puà fare, darebbe errore -> tutti gli indici devono essere tra 0 e len(lista) - 1 o tra -1 e -len(lista)
# per includere l'ultimo elemento della lista si omette l'indice di fine
print(f"Sottoista con range [2, ultimo-elemento]: {lista[2:]}")

# 2. tris -> stampare la sottolista con range (2, 5]
print(f"Lista con indici (2, 5] -> [3, 6): {lista[3:6]}")

# 3.
risultato_3 = lista[1] ** lista[2]
print(f"Risultato punto 3: {risultato_3}")

# 4.
risultato_4 = lista[0] + lista[-1]
print(f"Risultato punto 4: {risultato_4}")

# 5.
i = 4
if lista[i] > 10:
    print(f"{lista[i]} è maggiore di 10")
else:
    print(f"{lista[i]} NON è maggiore di 10")





