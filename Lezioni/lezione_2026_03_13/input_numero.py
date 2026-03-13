numero = input("Inserisci un numero: ")  # Proviamo a prendere un numero in input
numero = int(numero)  # Convertiamo la stringa ricevuta in input in un numero intero
print(numero * 10)  # Stampiamo il numero * 10

# la conversione inversa si fa con str()
numero_stringa = str(numero)

# Se non siamo sicuri di che tipologia sia una variabile, usiamo type()
print(f"Tipo numero: {type(numero)}, tipo numero_stringa: {type(numero_stringa)}")



