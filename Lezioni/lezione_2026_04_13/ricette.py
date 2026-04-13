"""
Vogliamo fare un programma che data una ricetta (una lista di ricette) e un riferimento di persone ne calcoli tutti
gli aggiustamenti per le varie proporzione

es:
ricetta pancake (4 persone):
 - farina: 200 g
 - uova: 2 pz
 - burro: 40 g
 - latte: 200 mL
 - lievito: 2 cucchiaini

La vogliamo adattare per 10 persone
farina: 200 -> 500 g

Bisogna:
 1. fare la funzione per risolvere una proporzione
 2. fare la funzione per formattare bene i numeri con la virgola : 3.0 -> 3, 2.5323 -> 2.5
        round(2.425634, 1) -> ...
 3. data una ricetta nel formato nel main -> calcolare e stampare la versione aggiustata per il nuovo numero di persone
"""
def calcola_proporzione():
    """
    Funzione che calcola una proporzione dati quantità iniziale, persone di riferimento e persone obiettivo
    :return: quantità adeguata alle persone obiettivo
    """
    ...

if __name__ == "__main__":
    ricetta = [
        "Ricetta pancake",  # Nome ricetta
        [
            ("farina", 200, "g"),  # Ingrediente, quantità, unità di misura
            ("uova", 3, "pz"),
            ("burro", 40, "g"),
            ("latte", 200, "mL"),
            ("lievito", 2, "cucchiaini")
        ],  # Elenco ingredienti
        4   # Numero di persone di riferimento
    ]