# Negli esempi precedenti abbiamo utilizzato gli indici per accedere ai valori salvati nelle liste
# Se la lista è lunga (o anche no) dover accedere ad ogni elementi separatamente per "elaborarlo" è
# ancora scomodo come prima e non può essere facilmente adattato alla crescita della lista.

# Per ovviare a questo problema utilizziamo il ciclo for
lista = ["Daniele", "Ilaria", "Luca", "Giulia", "Marco"]  # Creaiamo una lista di nomi
# Vogliamo stampare un saluto del tipo "Ciao <nome>, come stai?" per ogni elemento della lista
for nome in lista:  # si legge -> per ogni nome nella lista
    print(f"Ciao {nome}, come stai?")
print("SIAMO FUORI DAL FOR")
# -> Questo for prende, uno alla volta, gli elementi della lista ed esegue per ognuno il blocco di codice dentro il for
# -> Giro 1: nome <- "Daniele" | print("Ciao Daniele, come stai?")
# -> Giro 2: nome <- "Ilaria"  | print("Ciao Ilaria, come stai?")
# -> ...
# -> Giro 5: nome <- "Marco"   | print("Ciao Marco, come stai?")

# Una volta finiti gli elementi della lista la variabile utilizzata per iterare (nell'esempio la variabile "nome") non viene
# eliminata ma mantiene l'ultimo valore che ha assunto
print(f"Ultimo elemento: {nome}")

print("=" * 70)
# Otteniamo la somma di una lista
lista_numeri = [3, 4.5, 9, 2.2, 10.2, 19]

# Per prima cosa definiamo una variabile in cui mettiamo il totale
totale = 0

# Per ogni numero della lista, aggiungiamo il suo valore al totale
for numero in lista_numeri:
    totale += numero  # ----> totale <- totale + numero


# La funzione round(numero, n) arrotonda numero a n cifre decimali
# totale = round(totale, 2) -> se facessimo questo, staremmo proprio cambiando il valore PERMANENTEMENTE dentro la variabile
# Ovviamente non esiste un corrispondente che somigli a :.2f
print(f"Somma degli elementi nella lista: {round(totale, 2)}")
print(f"Somma degli elementi nella lista: {totale:.2f}") # -> otteniamo lo stesso risultato di prima




