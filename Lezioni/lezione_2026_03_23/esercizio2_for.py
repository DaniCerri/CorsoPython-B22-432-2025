# Chiediamo all'utente 5 oggetti da comprare
N_OGGETTI = 5

# definiamo la lista
lista_oggetti = []

for i in range(N_OGGETTI):  # Per i che va da 0 a N_OGGETTI - 1 (N_OGGETTI volte)
    oggetto = input(f"Inserisci l'oggetto numero {i + 1} da comprare: ")  # Prendiamo in input il nome di un oggetto
    lista_oggetti.append(oggetto)  # Lo aggiungiamo alla lista

print(lista_oggetti)


