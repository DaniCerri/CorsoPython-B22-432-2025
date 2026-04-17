# Per gestire al meglio l'apertura e la chiusura dello stream per l'utilizzo di un file
# si usa il blocco "with"
from sys import flags
import esercizio1  # Importiamo il codice scritto in esercizio1.py per usarlo qua

def row_parse(riga: str):
    """
    Eseguiamo il parsing di una riga in formato stringa per renderla una tupla
    con (data: str, ora: str, temp: float, umidita: float)
    :param riga: riga letta dal file
    :return: (data: str, ora: str, temp: float, umidita: float)
    """
    riga = riga.strip()  # Togliamo il "\n"
    parti = riga.split(",")  # Separiamo i valori con le virgole
    parti[2] = float(parti[2])  # Convertiamo a float la temperatura
    parti[3] = float(parti[3])  # Convertiamo a float l'umidità
    return tuple(parti)

if __name__ == "__main__":
    # Con il comando open, creiamo uno stream per il file "dati.txt" in lettura e lo chiamiamo
    # "file_in"
    with open("dati.txt") as file_in:
        # per leggere una riga alla volta dalla memoria
        # for riga in file_in:
            # riga = riga.strip()  # Togliamo il \n
            # poi si fa ciò che serve con la riga

        righe_file = file_in.readlines()  # Leggiamo tutte le righe e le mettiamo in una lista

    # Uscendo dal blocco "with" si chiude lo stream
    # Facciamo una lista di righe processate chiamando la funzione "row_parse" su ogni riga
    # della nostra lista "righe_file"
    righe_processate = [row_parse(riga) for riga in righe_file[1:]]
    # Non prendiamo la riga 0 del file perchè è quella con i nomi dei valori

    # Usiamo la funzione del file esercizio.py per convertire le tuple a dizionari
    diz_righe = [esercizio1.registrazione_to_dict(*riga) for riga in righe_processate]

    # Usiamo la funzione del file esercizio.py per ottenere le medie
    temperatura_media, umidita_media = esercizio1.medie(diz_righe)

    # Stampiamo le righe
    print(esercizio1.stampa_elenco_misurazioni(diz_righe))

    print("-" * 50)
    print(f" * Temperatura media: {temperatura_media:.2f} °C")
    print(f" * Umidità media: {umidita_media:.2%}")
