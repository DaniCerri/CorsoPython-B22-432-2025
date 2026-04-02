### Esercizio 1: Blocco del traffico (Targhe alterne)

Oggi in città c'è il blocco del traffico e possono circolare solo le auto con la targa che termina con un numero pari. Chiedi all'utente di inserire l'ultima cifra della sua targa. Il programma deve stampare "Puoi circolare" se il numero è pari, altrimenti deve stampare "Oggi devi prendere i mezzi pubblici".

### Esercizio 2: Sconti in cassa al supermercato

Chiedi all'utente il totale in euro della sua spesa al supermercato.

* Se la spesa è maggiore o uguale a 100€, applica uno sconto fedeltà del 20%.

* Se la spesa è compresa tra 50€ e 99.99€, applica uno sconto del 10%.

* Altrimenti, non applicare nessuno sconto.

Il programma deve stampare in modo chiaro il prezzo finale da pagare in cassa.

### Esercizio 3: Il timer del microonde

Stai scaldando la cena. Scrivi un programma che simuli il display di un microonde. Fai partire un conto alla rovescia da 10 fino a 1, stampando un numero alla volta. Al termine, il programma deve stampare "Il cibo è pronto! DING!".

### Esercizio 4: Il salvadanaio per le vacanze

Vuoi mettere via dei soldi per un viaggio. Chiedi all'utente un numero che rappresenta quanti mesi mancano alla partenza. Usa un ciclo `while` per chiedere all'utente, mese per mese: "Quanto hai risparmiato questo mese?". Somma via via gli importi e alla fine stampa il totale del budget accumulato per la vacanza.

### Esercizio 5: Preventivo per la palestra

L'abbonamento mensile alla palestra costa 45€. Chiedi all'utente quanti mesi vorrebbe frequentare (es. da 1 a 12). Stampa un preventivo chiaro che mostri il costo per ogni mese cumulato, ad esempio: `1 mese: 45€`, `2 mesi: 90€`, `3 mesi: 135€`, fino al numero di mesi inserito.

### Esercizio 6: Sportello Bancomat bloccato

Imposta all'inizio del codice un PIN segreto della carta di credito (es. "1234"). L'utente ha a disposizione al massimo 3 tentativi allo sportello per inserirlo. Se sbaglia, mostra il messaggio "PIN errato, riprova". Se indovina, mostra "Accesso al conto consentito" e ferma il ciclo. Se finisce i 3 tentativi, mostra "Sicurezza: Carta trattenuta dallo sportello".

### Esercizio 7: Le faccende di casa

Scrivi un programma che pianifichi i primi 30 giorni del mese. Fai scorrere i giorni da 1 a 30.
Regole per le pulizie:

* Ogni 3 giorni bisogna annaffiare le piante (stampa "Giorno X: Annaffiare le piante").

* Ogni 5 giorni bisogna buttare il vetro (stampa "Giorno X: Buttare il vetro").

* Se i due compiti capitano nello stesso giorno, stampa "Giorno X: Giornata di pulizie generali!".

* Per gli altri giorni, stampa semplicemente "Giorno X: Relax".

### Esercizio 8: Il registro presenze del professore

Chiedi all'insegnante di inserire l'esito dell'appello in un'unica sequenza di lettere, dove 'P' sta per Presente e 'A' per Assente (es. "P P A P R P A"). Il programma deve analizzare la sequenza e stampare quanti alunni sono "Presenti" (contando solo le P, ignorando il resto e non facendo distinzione tra maiuscole o minuscole).

### Esercizio 9: Il recinto dell'orto

Vuoi recintare un orto quadrato per proteggerlo, mantenendo la terra all'interno libera per piantare. Chiedi i metri del lato (es. 5). Stampa una mappa dell'orto fatta di simboli `*` (che rappresentano lo steccato) di dimensione `Lato x Lato`, ma l'interno deve essere vuoto (fatto di spazi). I bordi esterni avranno gli asterischi, l'interno solo spazi.

### Esercizio 10: Suddivisione delle squadre al torneo

Sei l'organizzatore di un torneo amatoriale. Chiedi quanti giocatori si sono iscritti (un numero maggiore di 1). Vuoi sapere se i giocatori possono essere divisi in gironi o squadre eque di almeno 2 persone. Un numero di iscritti non può essere diviso equamente se è un "numero primo" (divisibile solo per 1 e per sé stesso). Verifica matematicamente il numero di iscritti: se non è divisibile per nulla, avvisa l'utente stampando "Dovremo fare squadre sbilanciate, il numero non è divisibile equamente!", altrimenti stampa "Ottimo, possiamo formare squadre equilibrate".