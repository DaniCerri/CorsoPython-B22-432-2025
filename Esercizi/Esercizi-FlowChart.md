# Esercizi sui Diagrammi di Flusso

*Strutture condizionali annidate (If-Else a cascata)*

## 1. Fasce di Voto Universitario

Progettare un diagramma di flusso che, ricevuto in input l'esito numerico di un esame universitario, determini e stampi la relativa fascia di valutazione: "Non superato" se il voto è strettamente minore di 18, "Eccellente" se è esattamente pari a 30, e "Superato" in tutti gli altri casi.

## 2. Lo Sconto Progressivo

Disegnare un diagramma di flusso che calcoli il totale da pagare per una spesa, applicando degli sconti progressivi. Nello specifico, se il totale iniziale è minore di 50 euro, non viene applicato alcuno sconto. Se è inferiore a 100 euro (ma maggiore o uguale a 50), si applica uno sconto del 10%. Se è pari o superiore a 100 euro, lo sconto applicato è del 20%. Stampare infine il totale aggiornato.

## 3. Classificazione dell'Angolo Geometrico

Realizzare un diagramma di flusso che, data in input l'ampiezza in gradi di un angolo (un valore compreso tra 1 e 179), lo classifichi correttamente. L'algoritmo deve stampare "Angolo Acuto" se l'ampiezza è strettamente minore di 90 gradi, "Angolo Retto" se è esattamente 90 gradi, e "Angolo Ottuso" nei restanti casi.

---

# Suggerimenti per la Risoluzione

*Aiuti per l'impostazione logica dei blocchi decisionali*

### Suggerimento Esercizio 1: Fasce di Voto

- Il primo blocco di decisione (rombo) deve controllare semplicemente se il voto è < 18.
- Se la risposta è **Falso** (il che significa che il voto è già matematicamente ≥ 18), inserisci a cascata un secondo blocco di decisione in quel ramo per verificare se il voto è esattamente uguale a 30.

### Suggerimento Esercizio 2: Lo Sconto Progressivo

- Inizia verificando se il totale è < 50.
- Nel ramo **Falso** di questa prima domanda, posiziona un secondo rombo che verifichi se il totale è < 100.
- *Nota bene:* nel secondo controllo non c'è bisogno di verificare se il totale è anche ≥ 50 (ovvero non serve una condizione AND/doppia). Se l'algoritmo è arrivato a quel punto del diagramma, il primo rombo lo ha già accertato per esclusione!

### Suggerimento Esercizio 3: Classificazione dell'Angolo

- Usa il primo rombo per chiedere: l'angolo è < 90?
- Se è **Falso**, fai scendere il flusso in un secondo rombo che chiede se l'angolo è esattamente uguale a 90.
- Se anche quest'ultima condizione è **Falso**, rimane solo una possibilità (l'angolo è > 90). Non serve un terzo rombo: puoi far finire direttamente la freccia nel blocco di output "Angolo Ottuso".
