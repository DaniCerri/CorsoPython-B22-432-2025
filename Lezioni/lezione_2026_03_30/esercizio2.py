"""
Prendiamo in input una serie di numeri interi separati da spazi
es: "2 34 27 28 20 102 1892" -> Media: 300.7142857142857

Poi dopo averli separati con split e successivamente convertiti in interi (uno alla volta)
Ne calcoliamo la media

* La somma di una lista di interi si trova con sum(lista_interi)
* La lunghezza di una lista è len(lista)
"""

while True:
    numeri = input("Inserisci i tuoi numeri interi separati da spazi: ")
    if not numeri: # Se numeri è una stringa vuota
        print("Inserisci almeno un numero")
        continue

    # Controlliamo che siano tutti numeri convertibili a interi
    valido = True
    for pezzo in numeri.split(" "):
        if not pezzo.lstrip("-").isdigit():
            print(f"'{pezzo}' non è un numero intero valido")
            valido = False
            break

    if valido:
        break

# 1. Splittiamo la stringa in base agli spazi
lista_numeri_str = numeri.split(" ")

# 2. Per ogni elemento della lista di numeri in formato stringa, lo convertiamo a intero
lista_numeri_int = []
for numero_str in lista_numeri_str:
    numero_int = int(numero_str)  # Convertiamo la stringa a intero
    lista_numeri_int.append(numero_int)  # Aggiungiamo il numero convertito alla lista

# lista_numeri_int = [int(num) for num in numeri.split(" ")]  # Per approfondimento -> list comprehension
# il codice sopra fa esattamente i punti 1 e 2

# 3. Calcoliamo la media
media = sum(lista_numeri_int) / len(lista_numeri_int)

# 4. Stampiamo la media
print(f"La media della lista {lista_numeri_int} è {media}")

