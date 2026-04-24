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










