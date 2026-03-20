# Chiaramente il while non si utilizza solamente per richiedere un input
# Esempio1 - Calcoliamo il fattoriale di un numero
# regole: 0! ----> 1

num = 1024
risultato = 1

while num > 1:
    print(f"Giro: {8 - num}: ")
    print(f" * risultato <- {risultato} * {num} = {risultato * num} ")
    print(f" * num <- {num} - 1 = {num - 1}")
    risultato *= num  # -> risultato = risultato * num
    num -= 1  # num = num - 1

troppo_lungo = len(str(risultato)) >= len(str(2 ** 64))
print(risultato)

