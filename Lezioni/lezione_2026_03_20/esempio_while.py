# Esempio con while "normale"
voto = 0  # Inizializziamo la variabile voto a 0

while not (18 <= voto <= 30):
    voto = int(input("Inserisci il tuo voto (tra 18 e 30 compresi): "))

    if not (18 <= voto <= 30):
        print("Il voto inserito non è valido perchè non è tra 18 e 30")

print(f"Voto accettato: {voto}")

# Stessa cosa ma con il while True:
while True:  # è vera sempre, se non facciamo interrompere "manualmente" il while gira per sempre
    voto2 = int(input("Inserisci il tuo secondo voto (18 <= voto2 <= 30): "))

    if 18 <= voto2 <= 30:
        # Usciamo dal while, se il voto va bene
        break

    # Se non siamo usciti finiamo qua
    print("Il voto inserito non è valido")

print(f"Voto2 accettato: {voto2}")
media = (voto + voto2) / 2
print(f"Media: {media}")

