"""
Abbiamo una p.IVA e facciamo i consulenti, vogliamo fare un calcolatore di tasse
e netto che ci rimane dal fatturato.

Siamo in regime forfettario quindi le tasse si pagano come segue:
1. Si calcola la base imponibile con il coefficiente di redditività
   es: ho guadagnato 100€ le tasse le pago solo sul 67% di questo importo -> base imponibile: 67€
   es: ho guadagnato 130€ le tasse le pago solo sul 73% di questo importo -> base imponibile: 94.9€

2. Su questo nuovo importo si calcolano le tasse:
    a. INPS: 26.27% della base imponibile
    b. IRPEF: 5% della base imponibile

Abbiamo una lista di importi che abbiamo fatturato -> [100, 500, 1023, 17, 20]
per ognuno dobbiamo calcore tutti i dettagli

Poi, sappiamo che per ogni fattura bisogna pagare 2€ di bollo

L'obiettivo finale è produrre un elenco dettagliato dei costi per ogni fattura e in totale, bolli compresi
"""

def calcola_percentuale(numero: float, percentuale: float):
    """
    Dato un numero e la percentuale la calcola. Es: 10, 4% -> 0.4
    :param numero: Numero base
    :param percentuale: percentuale espressa senza "%"
    :return: il valore calcolato
    """
    # per risolvere una percentuale dobbiamo risolvere una semplice proporzione
    # per ottenere il p% di n -> x : n = p : 100
    # x = n * (p / 100)

    coeff = percentuale / 100  # Calcoliamo il coeff percentuale
    # il risultato sarà dato da numero * coeff
    return numero * coeff

def calcola_dettaglio_fattura(importo: float, perc_redditivita=67):
    """
    Funzione che calcola e restituisce tutti i dettagli che compongono un prezzo fatturato (senza bollo)
    :param importo: Importo fatturato in €
    :param perc_redditivita: Percentuale di importo da considerare per le tasse (es: 67%)
    :return: netto, da_pagare_irpef, da_pagare_inps
    """
    inps = 26.27 # % inps
    irpef = 5  # % irpef

    # Calcoliamo l'imponibile con la percentuale di redditivitù
    imponibile = calcola_percentuale(importo, perc_redditivita)

    da_pagare_inps = calcola_percentuale(imponibile, inps)  # Sull'imponibile calcoliamo quanto va pagato di inps
    da_pagare_irpef = calcola_percentuale(imponibile, irpef)  # Sull'imponibile calcoliamo quanto va pagato di irpef

    netto = importo - (da_pagare_inps + da_pagare_irpef)

    return netto, da_pagare_irpef, da_pagare_inps  # li restituiamo dalla funzione

if __name__ == "__main__":
    # mai scrivere "nome_variabile: " dentro la chiamata ad una funzione, lo scrive da solo Pycharm
    # print(f"Il 10% di 49 è {calcola_percentuale(49, 10)}")
    # print(f"Il 12.4% di 26 è {calcola_percentuale(26, 12.4)}")
    # print(f"Il 83.2% di 452 è {calcola_percentuale(452, 83.2)}")
    #
    # # Calcoliamo il 10% del 50% di 27
    # primo = calcola_percentuale(27, 50)
    # ris = calcola_percentuale(primo, 10)
    #
    # ris2 = calcola_percentuale(calcola_percentuale(27, 50), 10)
    #
    # perc_nuova = calcola_percentuale(50, 10)
    # ris3 = calcola_percentuale(27, perc_nuova)
    #
    # ris4 = calcola_percentuale(27, calcola_percentuale(50, 10))
    #
    # print(ris, ris2, ris3, ris4)
    fattura = 1035.23 # € di fattura

    # Per salvare i valori multipli restituiti da una funzione, possiamo fare in due modi
    risultato = calcola_dettaglio_fattura(fattura)  # Mettiamo tutto dentro UNA SOLA variabile -> tupla
    # Usiamo ESATTAMENTE lo stesso numero di variabili che escono dalla funzione per "spacchettare" il risultato
    netto_f, irpef_f, inps_f = calcola_dettaglio_fattura(fattura)

    print(f"Netto: {risultato[0]}, IRPEF: {risultato[1]}, INPS: {risultato[2]}")
    print(f"Netto: {netto_f}, IRPEF: {irpef_f}, INPS: {inps_f}")
