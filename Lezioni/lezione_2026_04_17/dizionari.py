# Dizionario: Una sequenza *non ordinata* di coppie "chiave-valore"
# - Non ordinata: gli elementi salvati in un dizionario non hanno un ordine -> NON ESISTE
#   il concetto di "primo elemento" o "ultimo elemento"
# -> Ogni valore quindi non è identificato dalla sua posizione come in liste e tuple ma dalla sua
#    chiave

# Rappresentiamo la ricetta dell'ultimo esercizio
ricetta = {
    "nome": "Ricetta Pancake",
    "persone": 4,
    "ingredienti": (
        {"ingrediente": "farina",  "quantita": 200, "unita": "g"},
        {"ingrediente": "uova",    "quantita": 3,   "unita": "pz"},
        {"ingrediente": "burro",   "quantita": 40,  "unita": "g"},
        {"ingrediente": "latte",   "quantita": 200, "unita": "mL"},
        {"ingrediente": "lievito", "quantita": 2,   "unita": "cucchiaini"},
    ),
    "allergeni": ("glutine", "latte")  # è facile aggiungere dati, come gli allergeni
}

# Per ottenere tutte le chiavi (di primo livello) di un dizionario si usa
print(list(ricetta.keys()))  # dizionario.keys() non restituisce una lista vera e propria

# Per ottenere tutti i valori (di primo livello) di un dizionario si usa
print(list(ricetta.values()))  # dizionario.values() non restituisce una lista vera e propria

# Per ottenere tutte le coppie chiave-valore (di primo livello) di un dizionario si usa
print(list(ricetta.items()))  # dizionario.items() non restituisce una lista vera e propria

for chiave, valore in ricetta.items():
    print(f" * {chiave}: {valore}")

# Fare il dizionario di questo corso:
# Il corso ha codice B22-432-2025, ha come materie python e javascript.
# La prima la insegna Daniele Cerrina, la seconda Dario Mennillo. Il corso è iniziato il
# 06/03/2026 e finirà il 01/05/2026 e ci sono 10 iscritti.
corso = {
    "codice": "B22-432-2025",
    "materie": (
        {"nome": "python", "insegnante": "Daniele Cerrina"},
        {"nome": "javascript", "insegnante": "Dario Mennillo"},
    ),
    "data_inizio": "06/03/2026",
    "data_fine": "01/05/2026",
    "n_iscritti": 10
}

print(corso['codice'])