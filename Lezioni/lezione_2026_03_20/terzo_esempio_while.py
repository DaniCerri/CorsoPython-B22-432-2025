# Abbiamo due numeri interi che si chiama base ed esponente
# calcoliamo con un while il risultato che dovrebbe dare
# l'espressione base ** esponente

base = 2
esponente = 8
risultato = 1
print(f"Risultato atteso: {base ** esponente}")

while esponente > 0:
    risultato *= base
    esponente -= 1

print(f"Risultato ottenuto: {risultato}")
