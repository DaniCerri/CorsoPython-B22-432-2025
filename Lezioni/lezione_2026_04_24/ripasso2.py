"""
Facciamo una funzione che presa una lista di stringhe, dica qual è la più
lunga e la restituisca anche tutta maiuscola
"""
def funzione_stringa(lista_str: list[str]):
    assert len(lista_str) > 0, "Non si può fare con una lista vuota"

    max_length = len(lista_str[0])  # Definiamo come lunghezza massima la lunghezza 0
    max_string = 0  # Definiamo come indice della più lunga quello della prima
    for i in range(len(lista_str)):
        stringa = lista_str[i]
        if len(stringa) > max_length:
            max_length = len(stringa)
            max_string = i

    return max_string, lista_str[max_string].upper()


"""
Facciamo una funzione che aiuti a scrivere in CamelCase e kebab-case
* UnEsempioDiStringaCamelCase
* un-esempio-di-stringa-kebab-case
La funzione prende una stringa e la restituisce nei due formati
"""
def codifica(stringa: str):
    stringa_kebab = ""
    stringa_camel = ""
    for parola in stringa.split(" "):
        stringa_kebab += parola + "-"
        stringa_camel += parola.capitalize()
    # Togliamo l'ultimo trattino e rendiamo minuscola la stringa
    stringa_kebab = stringa_kebab[:-1].lower()

    # stringa_kebab = "-".join(parola for parola in stringa.split(" "))
    # stringa_camel = "".join(parola.capitalize() for parola in stringa.split(" "))

    return stringa_kebab, stringa_camel

"""
Vogliamo fare una funzione che calcoli quanti numeri sono sopra e sotto una soglia data
all'interno di una lista
Soglia -> Threshold
Es: lista = [1, 2, 3, 4, 5, 6, 7], soglia = 3.4  ----> Minori: 3, Maggiori: 4
"""
def conta_soglia(lista: list[float | int], soglia: float):  # Errore bonus: va bene sia float che int
    minori = 0  # Errore 1.1: inizializziamo i contatori a 0
    maggiori = 0  # Errore 1.2: inizializziamo i contatori a 0
    for n in lista:  # Errore 2: dobbiamo prendere proprio gli elementi, non indici
        if n < soglia:
            minori += 1  # Errore 3: Dobbiamo aumentare i contatori e non resettarli
        elif n > soglia:  # Errore 4: dobbiamo gestire il caso in cui si è uguali alla soglia
            maggiori += 1

    return minori, maggiori  # Errore 5: Il return era fuori dalla funzione

"""
Facciamo una funzione che date due liste restituisca una matrice (lista di liste)
con tutte le possibili coppie (prodotto cartesiano)

[1, 2, 3] x [4, 5, 6] -> 
[
    (1, 4), (1, 5), (1, 6),
    (2, 4), (2, 5), (2, 6),
    (3, 4), (3, 5), (3, 6)
]
"""
def prodotto_cartesiano(lista1: list, lista2: list):
    prodotto = ()
    for elem1 in lista1:
        for elem2 in lista2:
            prodotto += (elem1, elem2)

    for elem2 in lista2:
        for elem1 in lista1:
            prodotto += (elem2, elem1)

    return lista1, lista2










