# 1. Prendiamo in input i dati necessari
lunghezza = input("Inserisci la lunghezza della stanza: ")
lunghezza = float(lunghezza)

profondita = input("Inserisci la profondità della stanza: ")
profondita = float(profondita)

costo_mq = input("Inserisci il costo per mq: ")
costo_mq = float(costo_mq)

# 2. Calcoliamo ciò che ci serve
area_stanza = lunghezza * profondita  # Calcoliamo l'area della stanza
costo_stanza = area_stanza * costo_mq  # Calcoliamo il costo totale

# 3. Stampiamo il risultato
print(f"La stanza con lunghezza {lunghezza} m e profondità {profondita} m")
print(f"Ad un costo al mq di {costo_mq} €/mq")
print(f"Costerà: {costo_stanza} €")





