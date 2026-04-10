# Dobbiamo calcolare la media di tre liste e stamparla per ognuna

# le funzioni si dichiarano con la parola "def"
# subito dopo si trova il nome della funzione (ciò con cui viene chiamata)
# dentro le parentesi inseriamo i dati (i parametri) con cui la funzione lavora
def calcola_media(lista: list):
    media = sum(lista) / len(lista)  # Calcoliamo la media della lista passata alla funzione
    return media  # Restituiamo il valore calcolato

def stampa(lista_stampa: list):
    media_stampa = calcola_media(lista_stampa)  # Usiamo la funzione appena creata per calcolare la media
    print(f"Media per la lista {lista_stampa}: {media_stampa:.2f}")

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [2, 2, 4, 4, 6, 6]
lista3 = [9, 2, 8, 4, 7, 6]

stampa(lista1)
stampa(lista2)
stampa(lista3)
stampa([2, 23, 1, 12, 23, 3])





