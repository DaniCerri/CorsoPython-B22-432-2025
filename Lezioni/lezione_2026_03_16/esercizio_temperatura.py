temperatura = float(input("Inserisci la temperatura (°C): "))  # Prendiamo in input la temperatura

print("VERSIONE BASE COME DA FLOWCHART")
# Ci chiediamo se la temperatura è minore o uguale di zero -> blocco rosso
if temperatura <= 0:  # Eseguiamo questo blocco se la condizione è VERA
    print(f"L'acqua alla temperatura di {temperatura} °C congela")
else:  # ALTRIMENTI (se la condizione è FALSA)
    # Ci chiediamo se la temperatura è tra 0 e 100 esclusi -> blocco verde
    if 0 < temperatura < 100:  # Eseguiamo questo blocco se la condizione è VERA
        print(f"L'acqua alla temperatura di {temperatura} °C rimane liquida")
    else:  # ALTRIMENTI
        # blocco viola
        print(f"L'acqua alla temperatura di {temperatura} °C evapora")

print("=" * 70)
print("VERSIONE COMPATTA DI PYTHON")
# nel caso in cui servisse mettere insieme molte condizioni, sarebbe molto scomodo e (aumenterebbe la possibilità di
# sbagliare) mettere gli if nei annidati dentro i blocchi else precedenti per molte volte.
# Per questo in Python si utilizza il costrutto elif (else if) che permette di unire il blocco else con il blocco if
# if subito dopo

# Quindi la nostra struttura di prima diventa così
if temperatura <= 0:  # Controllo rosso
    print(f"L'acqua alla temperatura di {temperatura} °C congela") # Output rosso
elif 0 < temperatura < 100:  # Controllo verde
    print(f"L'acqua alla temperatura di {temperatura} °C rimane liquida")  # Output verde
else: # Ramo del falso del controllo verde
    print(f"L'acqua alla temperatura di {temperatura} °C evapora")  # Output viola








