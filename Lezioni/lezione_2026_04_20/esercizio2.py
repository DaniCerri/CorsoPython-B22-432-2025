import esercizio1 as es1  # Importiamo il file esercizio1 e gli diamo un
# alias chiamandolo es1
# ALTRI ESEMPI "FAMOSI"
#  * import numpy as np
#  * import pandas as pd
#  * import matplotlib.pytplot as plt

# 1. Leggere il file lorem.txt una riga alla volta e per ogni riga contare caratteri (con spazi)
# e vocali/consonanti e stampate
# esempio print: Riga 1: Caratteri: 102, Consonanti: 67, Vocali: 12
with open("lorem.txt") as file_in:
    n_riga = 0
    for riga in file_in:
        riga = riga.strip()
        if not riga:  # Se la riga è vuota
            continue  # Passiamo al prossimo giro del ciclo
        caratteri = es1.conta_caratteri(riga, True)
        vocali, consonanti = es1.conta_vocali_consonanti(riga)
        print(f"Riga {n_riga} | Caratteri: {caratteri}, Consonanti: {consonanti}, Vocali: {vocali}")
        n_riga += 1

# 2. Leggere tutto il file e poi dire: numero parole, numero frasi e dizionario di frequenza parole
with open("lorem.txt") as file_in:
    righe = file_in.readlines()

# TODO: questo codice calcola le cose per ogni riga, noi invece vogliamo per tutto il testo
#  Si può unire le righe o leggerle diversamente
for riga in righe:
    parole = es1.conta_parole(riga)  # TODO: eliminare anche da qui le parole vuote -> ""
    frasi = es1.conta_frasi(riga)
    diz_freq = es1.frequenza_parole(riga)


