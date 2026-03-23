# C'è un altro modo di usare i for ed è per svolgere qualcosa un numero esatto di volte (3 volte, 10 volte, etc)
# Chiameremo questo modo di fare cicli for "for numerato" e quello precedente "for classico [di python]"
# NB: Di solito negli altri linguaggi (C, C++, Java, etc) il for detto "classico" è quello numerato e poi si ottiene
# usando bene gli indici quello classico per python.
# In python il for di base è quello classico e con uno stratagemma del linguaggio lo si fa diventare numerato

# Vogliamo stampare un saluto alla stessa persona 6 volte
nome = "Daniele"
for i in range(6):  # -> per ogni i che va da 0 a 5 compresi -> per ogni i nella lista [0, 1, 2, 3, 4, 5]
    print(f"Saluto {i}: Ciao Daniele")

# in C++ questo for si scriverebbe for (int i=0; i < 6; i++) {codice da ripetere}
print("=" * 70)
lista = ["rosso", "verde", "giallo", "blu"]

for i in range(len(lista)): # per ogni i in [0, 1, 2, ..., len(lista) - 1]
    print(f"L'elemento in posizione {i} è {lista[i]}")

print("==" * 70)

# Esempio: vogliamo chiedere all'utente 3 numeri e metterli in una lista
lista_input = []  # Creiamo una lista vuota dove metteremo gli input dell'utente

N_VOTI = 3
for i in range(N_VOTI):

    while True:
        # 1. Prendiamo il voto in input -> dentro al while così che venga ripetuto
        voto = int(input(f"Inserisci il tuo voto numero {i + 1}: "))

        if 18 <= voto <= 30:  # Controlliamo se va bene
            break   # Se va bene interrompiamo il while

        # Se non abbiamo interrotto il while, spieghiamo all'utente perchè non va bene il voto inserito
        print("Il voto inserito non è valido (deve essere tra 18 e 30 compresi")

    # 2. Appendiamo (aggiungiamo) il voto alla lista -> fuori dal while così che venga fatto solo una volta PER OGNI VOTO
    lista_input.append(voto)

print(f"Voti inseriti: {lista_input}")



