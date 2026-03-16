# Prendiamo in input il primo voto
# (non stiamo controllando che si possa convertire a numero intero, lo diamo per scontato)
voto1 = int(input("Inserisci il tuo primo voto (deve essere tra 18 e 30 compresi): "))

if 18 <= voto1 <= 30:  # Entriamo in questo blocco SOLAMENTE se la condizione inserita è vera
    # codice se la condizione è vera
    voto2 = int(input("Inserisci il tuo secondo voto (deve essere tra 18 e 30 compresi): "))

    if 18 <= voto2 <= 30:
        media = (voto1 + voto2) / 2  # Se entrambi i voti vanno bene, calcoliamo la media
        print(f"la tua media è: {media}")  # Stampiamo la media

    else: # Gestiamo il caso in cui la condizione 18 <= voto2 <= 30 sia FALSA
        print("Il voto deve essere tra 18 e 30 compresi")

else: # Gestiamo il caso in cui la condizione 18 <= voto1 <= 30 sia FALSA
    print("Il voto deve essere tra 18 e 30 compresi")

# per definire un blocco di codice:
#   in C -> {} parentesi graffe
#   in Python -> : definiamo l'inizio del blocco di codice, ogni riga dentro al nostro blocco sarà
#                indentata a destra di più di quelle fuori dal blocco
# è fondamentale (sennò il codice non funziona) che le indentazioni siano tutte uguali (es: 2 spazi, 4 spazi, 6 spazi)
# se ho due blocchi uno dentro l'altro, il può interno dovrà avere DUE indentazioni dal bordo sinistro (2 * 2 spazi,
# 4 * 2 spazi, 6 * 2 spazi, ...)