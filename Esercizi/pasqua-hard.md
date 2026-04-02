### Esercizio 1: Il distributore automatico (Il resto esatto)

Stai comprando una merendina alle macchinette. Il programma deve chiedere il costo del prodotto e l'importo inserito (in Euro, ad esempio `1.50` o `2.00`). Se l'importo inserito è maggiore del costo, la macchinetta deve erogare il resto utilizzando il **minor numero possibile di monete**.
Sapendo che la macchinetta dispone solo di monete da 2€, 1€, 0.50€, 0.20€, 0.10€ e 0.05€, calcola e stampa esattamente quante monete di ciascun taglio devono essere restituite per dare il resto esatto all'utente. *(Attenzione: in programmazione i numeri decimali possono fare brutti scherzi con le approssimazioni, assicuratevi che il resto sia calcolato in modo preciso!)*

### Esercizio 2: La promozione "Prendi 3, Paghi 2" al supermercato

Sei in cassa e stai passando i prodotti sul nastro. Il programma deve continuare a chiedere all'utente il prezzo di ogni articolo finché non viene digitato "0" (che chiude lo scontrino).
Il supermercato ha una promozione su tutta la spesa: ogni 3 articoli acquistati, **quello che costa meno è in omaggio**. Attenzione: se compro 6 articoli, i 2 articoli meno costosi di tutto lo scontrino saranno gratuiti, e così via.
Il programma deve calcolare il totale senza sconto, l'importo risparmiato grazie ai prodotti in omaggio, e il totale finale da pagare.

### Esercizio 3: Prenotazione dei posti al cinema

Un gruppo di amici vuole andare al cinema, ma pretendono assolutamente di sedersi tutti vicini.
Immagina una fila del cinema rappresentata da una lista di 0 (posto libero) e 1 (posto occupato), ad esempio: `[0, 1, 1, 0, 0, 0, 1, 0, 0]`.
Chiedi all'utente quanti biglietti vuole acquistare. Il programma deve analizzare la fila e verificare se esiste una sequenza ininterrotta di posti liberi sufficiente per l'intero gruppo. Se la trova, deve "prenotare" i posti trasformando i relativi `0` in `1` e stampare la nuova fila. Altrimenti, deve stampare: "Ci dispiace, non ci sono abbastanza posti vicini per voi".

### Esercizio 4: L'algoritmo della password bancaria

Stai creando le credenziali per il tuo nuovo home banking. La banca è paranoica sulla sicurezza.
Chiedi all'utente di inserire una password. Il programma deve analizzarla e accettarla solo se rispetta **tutte e quattro** le seguenti regole simultaneamente:

1. Deve essere lunga almeno 8 caratteri.

2. Deve contenere almeno una lettera maiuscola e almeno un numero.

3. Deve contenere almeno un carattere speciale (scegli tra `!`, `@`, `#`, `?`).

4. **Regola avanzata:** Non deve mai contenere due caratteri identici consecutivi (es. la parola "Pa**ss**word!" viene rifiutata per la doppia s).

Se la password non è valida, il programma deve continuare a richiederla spiegando all'utente esattamente **quale o quali** regole sono state violate.

### Esercizio 5: L'ascensore intelligente

Sei l'amministratore di un condominio di 15 piani. Per risparmiare corrente e tempo, l'ascensore non deve fare su e giù seguendo l'ordine cronologico in cui i condomini premono i bottoni, ma deve **ottimizzare il percorso**. Viaggerà in una direzione servendo le chiamate, per poi invertire la marcia. Ma qual è la direzione iniziale migliore?

Chiedi all'utente due informazioni:

1. **A quale piano si trova attualmente l'ascensore** (es. piano 6).

2. **Quali piani sono stati prenotati**, inseriti tutti insieme e separati da uno spazio (es. `8 2 12 5`).

**Regole di movimento:**
Il programma deve calcolare i "piani di distanza" totali percorsi dall'ascensore in due scenari differenti e scegliere quello più breve:

* **Scenario A (Prima SU, poi GIÙ):** Sale fino al piano richiesto più alto, poi inverte la marcia e scende fino al piano richiesto più basso.

* **Scenario B (Prima GIÙ, poi SU):** Scende fino al piano richiesto più basso, poi inverte la marcia e sale fino al piano richiesto più alto.

Il programma deve stampare quale scenario fa risparmiare più strada (indicando i piani totali percorsi) e poi stampare il "diario di bordo" con l'ordine esatto delle fermate.

**Esempio pratico:**

* **Piano di partenza:** `6`

* **Piani prenotati:** `8 2 12 5`

* **Calcolo dello Scenario A (SU -> GIÙ):** * Da 6 sale a 12 (percorre 6 piani).
  * Da 12 scende a 2 (percorre 10 piani).
  * Totale: 16 piani percorsi. L'ordine fermate sarebbe: `8 -> 12 -> 5 -> 2`.

* **Calcolo dello Scenario B (GIÙ -> SU):**
  * Da 6 scende a 2 (percorre 4 piani).
  * Da 2 sale a 12 (percorre 10 piani).
  * Totale: 14 piani percorsi. L'ordine fermate sarebbe: `5 -> 2 -> 8 -> 12`.

* **Output del programma:** Il programma deve accorgersi che lo Scenario B è più efficiente (14 < 16) e stampare: "Meglio scendere prima! Piani totali percorsi: 14. Fermate: 5 -> 2 -> 8 -> 12".