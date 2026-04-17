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
def calcola_proporzione(quantita, riferimento, obiettivo):
    """
    Funzione che calcola una proporzione dati quantità iniziale, persone di riferimento e persone obiettivo
    :param quantita: Quantità di ingrediente nella ricetta originale
    :param riferimento: Persone di riferimento nella ricetta originale
    :param obiettivo: Persone a cui adattare la ricetta
    :return: quantità adeguata alle persone obiettivo
    """
    # Dobbiamo risolvere la proporzione q : pi = x : po
    # x -> po * q / pi -> q * (po / pi)
    return round(quantita * obiettivo / riferimento, 1)  # Arrotondiamo giù il risultato a una sola cifra decimale

def formatta_numero(numero):
    """
    Prende un numero, se "intero" lo restituisce convertito a int, altrimenti a float (con un solo decimale)
    :param numero: numero da formattare
    :return: numero formattato
    """
    # 0.3 -> 3 è la parte decimale
    # 1.0 -> 0 è la parte decimale
    # 1. Controllare che la parte decimale sia 0
    # controlliamo che il risultato della divisione intera per 1 e il numero originale siano uguali
    # 1.2 -> 1.2 // 1 = 1.0 != 1.2
    # 4.0 -> 4.0 // 1 = 4.0 == 4.0
    if numero // 1 == numero:
        # 2. Se vero -> restituire il numero convertito a int
        return int(numero)
    # 3. "Altrimenti" -> restituire il numero arrotondato a 1 cifra decimale
    return round(numero, 1)

def adatta_ingrediente(nome: str, quantita: float, unita: str, riferimento: int, obiettivo: int):
    """
    Restituisce una riga completa dell'ingrediente aggiustato
    :param nome: Nome dell'ingrediente
    :param quantita: Quantità di ingrediente
    :param unita: Unità di misura dell'ingrediente
    :param riferimento: Persone di riferimento originali della ricetta
    :param obiettivo: Persone da soddisfare con l'adattamento della ricetta
    :return: (nome, quantita_calcolata, unita)
    """
    ...
    # 1. Calcolare quantita_calcolata con la funzione adatta
    quantita_calcolata = calcola_proporzione(quantita, riferimento, obiettivo)

    # 2. Comporre la riga
    riga = (nome, formatta_numero(quantita_calcolata), unita)

    # 3. Restituire la riga
    return riga

def adatta_ricetta(ricetta_completa: list, obiettivo: int):
    """
    Prende la ricetta completa e il numeoro di persone a cui adattarla e la restituisce aggiustata
    :param ricetta_completa: Lista opportunamente organizzata
    :param obiettivo: numero di persone a cui arrivare
    :return: ricetta adattata
    """
    nome_ricetta = ricetta_completa[0]  # Otteniamo il nome della ricetta
    persone_riferimento = ricetta_completa[-1]  # Sappiamo che il numero di persone è l'ultimo elemento
    lista_ingredienti = ricetta_completa[1]  # Prendiamo anche gli ingredienti

    # Aggiustiamo gli ingredienti per il nuovo numero di persone
    for i in range(len(lista_ingredienti)):
        ingrediente = lista_ingredienti[i]
        lista_ingredienti[i] = adatta_ingrediente(ingrediente[0], ingrediente[1], ingrediente[2],
                                                  persone_riferimento, obiettivo)

    # Ricomponiamo la ricetta adattata
    ricetta_adattata = [
        nome_ricetta,
        lista_ingredienti,
        obiettivo  # Salviamo nella ricetta adattata il nuovo numero di persone
    ]

    return ricetta_adattata

def stampa_linea(linea_ingrediente: tuple):
    linea = f"  * {linea_ingrediente[0].capitalize()}: {linea_ingrediente[1]} {linea_ingrediente[2]}"
    return linea

def stampa_ricetta(ricetta: list):
    output = "=" * 10 + f" {ricetta[0].upper()} " + "=" * 10 + "\n"  # Intestazione ricetta
    output += f"Per {ricetta[2]} persone\n"
    for linea in ricetta[1]:  # Per ogni linea ingrediente nella nostra ricetta
        # usiamo la funzione di prima e la aggiungiamo all'output
        output += f"{stampa_linea(linea)}\n"
    print(output)

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

    # usiamo le funzioni
    stampa_ricetta(ricetta)  # Stampiamo la ricetta originale
    print()
    ricetta_adattata = adatta_ricetta(ricetta, 10) # Adattiamo la ricetta per 10 persone
    stampa_ricetta(ricetta_adattata)  # Stampiamo la ricetta modificata

