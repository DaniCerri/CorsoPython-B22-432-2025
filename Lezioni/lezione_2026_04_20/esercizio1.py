"""
l'obiettivo è in questo file fare una serie di funzioni di analisi del testo e
testarle brevemente nel blocco 'if __name__ == "__main__"':
Tutte le funzioni devono prendere una sola stringa, a meno che non sia
detto diversamente

1. Data una stringa conta il numero di parole totali, senza contare punteggiatura
e maiuscole/minuscole. es: Ciao == ciao == CIAO == CIAO!

2. Data una stringa conta il numero di volta in cui ogni parole compare
(senza punteggiatura e maiuscole/minuscole)
es: Ciao, ciao CIAO. CIAO! -> 4
Consiglio: prima togliere la punteggiatura

3. Data una stringa conta le frasi: una frase termina con un "." o "?" o "!"

4. Data una stringa conta i caratteri (non " ")

5. Data una stringa conta vocali e consonanti
"""
def pulisci_stringa(stringa: str, split: bool):
    # TODO: inserire la possibilità di eliminare gli accenti
    stringa_pulita = "".join(l for l in stringa.lower() if l.isalnum() or l == " ")
    if split:
        return stringa_pulita.split(" ")
    return stringa_pulita

def conta_parole(stringa: str):
    """
    Prende una stringa e conta da quante parole è composta
    :param stringa: Stringa generica
    :return: numero di parole
    """
    # soluzione 1, rischiosa, contiamo solo gli spazi
    # return stringa.count(" ")

    # soluzione 2, più robusta: rimuoviamo la punteggiatura, rendiamo tutto
    # lowercase, poi splittiamo e contiamo gli elementi della lista
    lista_parole = pulisci_stringa(stringa, True)
    return len(lista_parole)

def frequenza_parole(stringa: str):
    lista_pulita = pulisci_stringa(stringa, True)
    # Bisogna fare un dizionario in cui segnarsi come chiave le parole e come valori il conteggio
    # trovato
    # per ogni parola, controlliamo se c'è nel dizionario, se sì aumentiamo il contatore di 1,
    # altrimenti creiamo una nuova coppia "parola: 1"
    dizionario_freq = {}
    for parola in lista_pulita:
        if parola in dizionario_freq.keys():
            dizionario_freq[parola] += 1
        else:
            # Mettiamo il contatore a 1 perchè abbiamo trovato la parola per la prima volta (una volta)
            dizionario_freq[parola] = 1

        # dizionario_freq[parola] = dizionario_freq.get(parola, 0) + 1

    return dizionario_freq

def conta_frasi(stringa: str):
    stringa_pulita = stringa.replace("!", ".").replace("?", ".")
    frasi = stringa_pulita.split(".")

    frasi = [frase for frase in frasi if frase != ""]
    # Teniamo solo le frasi che hanno un contenuto, le altre
    # sono figlie di situazioni tipo "Ciao!!!", "Tutto bene?!" o "Vado a dormire.", etc
    return len(frasi)

def conta_caratteri(stringa: str, includi_spazi: bool):
    """
    Data una stringa conta i caratteri.
    :param includi_spazi: se vero conta anche gli spazi, altrimenti li ignora
    :param stringa: stringa di cui contare i caratteri
    :return: numero caratteri
    """
    if not includi_spazi:  # Se non dobbiamo includere gli spazi
        stringa.replace(" ", "")  # Li togliamo dalla stringa

    return len(stringa)

def conta_vocali_consonanti(stringa: str):
    stringa_pulita = pulisci_stringa(stringa, False)
    # TODO: si può rendere più efficente con i "set"
    vocali = "aeiou"
    consonanti = "bcdfghjklmnpqrstvwxyz"
    n_vocali = 0
    n_consonanti = 0
    for lettera in stringa_pulita:
        if lettera in vocali:
            n_vocali += 1
        if lettera in consonanti:
            n_consonanti += 1
    return n_vocali, n_consonanti









