"""
Gestiamo un sistema di micro-anagrafe:
 - Passo 1: Chiediamo all'utente un elenco di nomi (e cognomi)
 - Passo 2: Per ogni nome chiediamo la data di nascita

 Salviamo tutto in due liste, una con i nomi e una con le date di nascita
"""

lista_persone = []  # Creiamo una lista vuota in cui metteremo i nomi delle persone

# Se abbiamo un numero_fisso di persone, usiamo un for i in range(numero_fisso)
# Altrimenti usiamo un while True che esce se l'utente sceglie di fermarsi

while True:
    # Prendiamo in input o il nome e cognome di una persona, oppure 0 per uscire dal while
    persona = input("Inserire nome e cognome della persona oppure 0 per terminare: ")

    # Controlliamo se l'utente ha inserito "0" per uscire
    if persona == "0":
        break  # Se l'utente ha inserito "0", usciamo dal while

    # Arriviamo qui solamente se l'utente non ha inserito "0"

    # Facciamo un controllo preliminare, verificando che ci sia ALMENO uno spazio nella stringa
    # Daniele Cerrina -> 1 -> va bene, niente errore
    # Daniele Luca Cerrina -> 2 -> va bene, niente errore
    # DanieleCerrina -> 0 -> non va bene, errore
    if persona.count(" ") < 1:  # Se il conteggio della stringa " " all'interno della persona è < 1
        print("Bisogna inserire 'nome cognome'")
        continue  # Passiamo al prossimo ciclo del while

    # Se non siamo usciti con il break e non è stato fatto il continue arriviamo qui
    # Salviamo la persona nella lista
    lista_persone.append(persona)
    print(f"Lista nel while: {lista_persone}")

print(f"Lista fuori dal while: {lista_persone}")

lista_date = []  # Creiamo una lista vuota in cui metteremo le date
# PER OGNI persona NELLA lista_persone, prendiamo la data di nascita
for persona in lista_persone:
    while True:
        data_nascita = input(f"Inserisci la data di nascita (dd/mm/YYYY) di {persona}: ")

        # Controlliamo che la data inserita abbia un formato corretto
        data_lista = data_nascita.split("/")  # Dividiamo la stringa con "/"

        if len(data_lista) != 3:  # Se non abbiamo esattamente 3 elementi, la data sicuramente non va bene
            print("La data non è nel formato corretto")
            continue  # Terminiamo questo ciclo e andiamo al prossimo

        is_sbagliato = False  # Creiamo questa variabile per tenere traccia di eventuali problemi
        # 1. Controlliamo se il giorno non va bene
        if not (1 <= int(data_lista[0]) <= 31): # Se la conversione del primo elemento della lista non è tra 1 e 31
            print("Il giorno inserito non va bene")
            is_sbagliato = True  # Settiamo a True perchè c'è stato un problema

        # 2. Controlliamo se il mese non va bene
        if not (1 <= int(data_lista[1]) <= 12):  # Se la conversione del secondo elemento della lista non è tra 1 e 12
            print("Il mese inserito non va bene")
            is_sbagliato = True  # Settiamo a True perchè c'è stato un problema

        # 3. Controlliamo se l'anno non va bene -> siamo nel caso di gente a partire dal 1900
        if not (1900 <= int(data_lista[2]) <= 2026):
            print("L'anno inserito non è valido")
            is_sbagliato = True  # Settiamo a True perchè c'è stato un problema

        if is_sbagliato:  # Se c'è stato almeno un problema
            continue  # Passiamo al prossimo giro

        # Se non c'è stato nessun problema arriviamo qua
        lista_date.append(data_nascita)  # Aggiungiamo la data nella lista
        break  # Usciamo dal while

print(lista_persone)
print(lista_date)

































