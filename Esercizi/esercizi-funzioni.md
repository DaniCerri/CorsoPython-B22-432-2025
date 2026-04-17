# 10 Esercizi Python: Funzioni e Moduli

In questa raccolta faremo un passo avanti: il codice non sarà più un blocco unico. Impareremo a creare **funzioni** (usando la parola chiave `def`) per riutilizzare il codice e a separare il nostro lavoro in più file, importando le funzioni da un file all'altro con il comando `import`.

## Modulo 1: Il Registratore di Cassa (Esercizi 1-3)

### Esercizio 1: La libreria degli sconti

Crea un file chiamato `promozioni.py`. All'interno di questo file, non deve esserci nessun `input()` o `print()`. Devi solo definire una funzione chiamata `applica_sconto(prezzo, percentuale)`. La funzione deve calcolare lo sconto, sottrarlo al prezzo originale e **restituire** (`return`) il prezzo finale scontato.

### Esercizio 2: La libreria delle tasse

Crea un file chiamato `tasse.py`. Anche qui, niente input/output diretti. Definisci una funzione chiamata `aggiungi_iva(prezzo_netto, aliquota_iva)`. La funzione deve calcolare il valore dell'IVA, aggiungerlo al prezzo netto e **restituire** il prezzo lordo finale.

### Esercizio 3: Lo scontrino del negozio

Crea un nuovo file chiamato `registratore_cassa.py`. In questo file, scrivi un programma che chiede all'utente il prezzo di listino di un prodotto, lo sconto da applicare e l'IVA (es. 22%).
**Obbligo:** Devi importare le funzioni create nei file `promozioni.py` e `tasse.py`. Usa prima la funzione dello sconto per trovare il prezzo scontato, e poi passa questo risultato alla funzione dell'IVA per calcolare il totale da pagare in cassa. Stampa lo scontrino finale.

## Modulo 2: Viaggi Internazionali (Esercizi 4-5)

### Esercizio 4: Il convertitore universale

Crea un file chiamato `conversioni.py`. Definisci due funzioni:

1. `miglia_a_km(miglia)`: converte le miglia in chilometri (1 miglio = 1.609 km) e restituisce il valore.

2. `galloni_a_litri(galloni)`: converte i galloni in litri (1 gallone = 3.785 litri) e restituisce il valore.

### Esercizio 5: Il computer di bordo dell'auto americana

Hai noleggiato un'auto negli Stati Uniti, ma il cruscotto mostra la velocità in miglia orarie (mph) e il consumo in galloni. Crea un file `computer_bordo.py`. Chiedi all'utente quanti galloni di benzina ha messo nel serbatoio e a quante miglia orarie sta viaggiando.
**Obbligo:** Importa le funzioni da `conversioni.py` e usale per stampare all'utente messaggi comprensibili in Europa: "Hai fatto rifornimento di X litri" e "Stai viaggiando a Y km/h".

## Modulo 3: Sicurezza e Validazione (Esercizi 6-7)

### Esercizio 6: Il "Buttafuori" Digitale

Crea un file chiamato `validazione.py`. Scrivi due funzioni:

1. `is_maggiorenne(anno_nascita, anno_corrente)`: restituisce `True` se l'utente ha almeno 18 anni, altrimenti `False`.

2. `is_password_sicura(password)`: restituisce `True` se la password è lunga almeno 8 caratteri E contiene almeno un carattere "!", altrimenti `False`.

### Esercizio 7: Iscrizione alla piattaforma

Crea un file chiamato `registrazione.py`. Simula il modulo di iscrizione a un sito. Chiedi all'utente il suo anno di nascita e di inventare una password.
**Obbligo:** Importa il file `validazione.py`. Usa le funzioni importate per controllare i dati. Se l'utente è minorenne, ferma tutto stampando "Devi essere maggiorenne per iscriverti". Se la password non è sicura, stampa "La password non rispetta i requisiti". Se entrambi i controlli (fatti tramite le funzioni) danno `True`, stampa "Registrazione completata con successo!".

## Modulo 4: Geometria Urbana (Esercizi 8-9)

### Esercizio 8: La cassetta degli attrezzi geometrica

Crea un file chiamato `geometria.py`. Crea due funzioni:

1. `area_rettangolo(base, altezza)`: restituisce l'area di un rettangolo.

2. `area_cerchio(raggio)`: restituisce l'area di un cerchio (usa 3.14 come Pi greco).

### Esercizio 9: Il preventivo del giardiniere

Sei stato incaricato di seminare l'erba in una piazza cittadina. La piazza è rettangolare, ma al centro ha una grande fontana circolare (dove ovviamente non va seminata l'erba).
Crea un file `giardiniere.py`. Chiedi all'utente le dimensioni (base e altezza) della piazza e il raggio della fontana.
**Obbligo:** Importa `geometria.py`. Calcola l'area totale della piazza, calcola l'area della fontana, e fai la sottrazione per trovare i metri quadrati calpestabili da seminare. Moltiplica il risultato per 15€ al mq per fornire il preventivo finale.

## Modulo 5: La vita da Freelance (Esercizio 10)

### Esercizio 10: Il simulatore di Partita IVA (Regime Forfettario)

Mettiamo insieme tutto ciò che abbiamo imparato sulla modularità.
Crea un file `calcoli_fiscali.py` con due funzioni:

1. `calcola_imponibile(incasso_totale, coefficiente_redditivita)`: calcola e restituisce su quale cifra si pagheranno effettivamente le tasse (es. incasso 1000€, coefficiente 67% = imponibile 670€).

2. `calcola_imposte(imponibile, aliquota)`: calcola e restituisce le tasse da pagare sull'imponibile.

Ora crea un file `gestionale_freelance.py`. Chiedi all'utente il totale fatturato nell'anno, il suo coefficiente di redditività (es. 0.67 o 0.78 a seconda del codice ATECO) e la sua aliquota (es. 0.05 per i primi 5 anni, o 0.15).
**Obbligo:** Usando rigorosamente le funzioni importate da `calcoli_fiscali.py`, calcola quanto l'utente deve pagare di tasse allo Stato e stampagli in faccia la dura realtà: il suo guadagno netto finale tolte le imposte!