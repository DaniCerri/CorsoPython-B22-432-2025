# definizione delle costanti per il programma
PESO_MAX = 300  # peso massimo supportato dall'ascensore

# inizializzazione delle variabili
n_persone = 0  # definiamo una variabile che conterà il numero di persone (inizialmente 0)
peso_tot = 0  # definiamo una variabile che conterrà il peso totale man mano che si aggiungono persone

print(f"Portata massima: {PESO_MAX} kg")
while True:  # finché rimaniamo con un peso inferiore alla portata massima
    peso_attuale = int(input(f"Inserisci il peso della persona n° {n_persone + 1}: "))

    # controlliamo che la persona possa salire
    # ci chiediamo se il peso accumulato finora sommato a quello di chi deve salire rispetta la capacità massima
    # if peso_tot + peso_attuale <= PESO_MAX:
    #     n_persone += 1  # n_persone = n_persone + 1 -> aggiungiamo una persona al contatore
    #     peso_tot += peso_attuale  # peso_tot = peso_tot + peso_attuale -> aggiungiamo il peso al peso totale
    # else:
    #     print("Allarme: peso eccessivo, l'ultima persona deve scendere!")
    #     break
    if PESO_MAX < peso_tot + peso_attuale:
        print(f"Allarme: peso eccessivo ({peso_tot + peso_attuale}), l'ultima persona deve scendere!")
        break

    n_persone += 1  # n_persone = n_persone + 1 -> aggiungiamo una persona al contatore
    peso_tot += peso_attuale  # peso_tot = peso_tot + peso_attuale -> aggiungiamo il peso al peso totale

print(f"Numero persone: {n_persone}")
print(f"Peso raggiunto: {peso_tot}")



