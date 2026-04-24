"""
Scriviamo una funzione che prenda in input una lista di numeri float
e restituisca la somma dei loro quadrati
(eleva ogni numero al quadrato e POI somma tutto)
"""
def somma_quadrati(lista_num: list[float]):
    totale = 0
    for numero in lista_num:
        totale += numero ** 2

    return totale

def somma_quadrati_bella(lista_num: list[float]):
    lista_quadrati = [n ** 2 for n in lista_num]
    return sum(lista_quadrati)

def errore_indice(n: int):
    lista = ["a"] * n
    for i in range(len(lista)):
        print(lista[i + 1] != lista[i])

"""
La funzione sotto dovrebbe calcolare il massimo di una lista, bisogna correggerla
per farla funzionare (senza usare "max()")
"""
def calcola_max(lista_numeri: list[int]):  # Errore bonus: deve essere una lista di interi
    assert len(lista_numeri) != 0, "Non c'è massimo di una lista vuota"
    massimo = lista_numeri[0]  # Errore uno: Non si può sapere se 0 non sia maggiore del massimo
    for numero in lista_numeri:  # Errore due: mancavano i ":"
        if numero > massimo:  # Errore tre: Dobbiamo controllare che superiamo il massimo
            massimo = numero
    return massimo # Errore quattro: Dobbiamo mettere il return fuori dal for





if __name__ == "__main__":
    # errore_indice(10)
    # int("2.2")   # ValueError
    lista = [2.2, 3.4, 120, 12, 213, 23, 12]
    print(somma_quadrati(lista))
