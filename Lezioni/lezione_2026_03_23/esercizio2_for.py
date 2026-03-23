# Chiediamo all'utente 5 oggetti da comprare
N_OGGETTI = 5

# definiamo la lista
lista_oggetti = []

for i in range(N_OGGETTI):  # Per i che va da 0 a N_OGGETTI - 1 (N_OGGETTI volte)
    oggetto = input(f"Inserisci l'oggetto numero {i + 1} da comprare: ")  # Prendiamo in input il nome di un oggetto
    lista_oggetti.append(oggetto)  # Lo aggiungiamo alla lista

print(lista_oggetti)

# Adesso per ogni oggetto chiediamo all'utente (in maniera chiara) quanto costa l'oggetto
# Salviamo tutti i prezzi in una lista di prezzi (i prezzi in questa lista devono lo stesso indice dell'oggetto a cui fanno
# riferimento)
# Controllare con un while che il prezzo sia > 0
lista_prezzi = []
for oggetto in lista_oggetti:
    while True:
        prezzo_oggetto = float(input(f"Inserisci il prezzo dell'oggeto '{oggetto}': "))
        if prezzo_oggetto > 0:
            break

        print("Il prezzo deve essere maggiore di zero")

    lista_prezzi.append(prezzo_oggetto)

print(lista_prezzi)

# Stampare il totale della spesa comprando tutti gli oggetti (somma di lista_prezzi)
totale = 0
for prezzo in lista_prezzi:
    totale += prezzo

print(f"La spesa totale è {totale:.2f} €")




