# Esercizio 1: fare una funzione che prende una lista di stringhe e la restituisce tutta maiuscola
def lista_maiuscola(lista_str: list[str]):
    for i in range(len(lista_str)):
        lista_str[i] = lista_str[i].upper()

    return lista_str

# Esercizio 2: fare una funzione che dato un numero intero calcoli il suo quadrato, cubo, radice quadrata e
# li restituisca in ordine in una lista
def calcoli(numero: int):
    lista = [numero ** 2, numero ** 3, numero ** 0.5]
    return lista

if __name__ == "__main__":
    # lista_di_stringhe = ["ciao", "come", "va"]
    # print(lista_di_stringhe)
    # lista_maiusc = lista_maiuscola(lista_di_stringhe)
    # print(lista_maiusc)
    numero_int = 10
    result = calcoli(numero_int)
    print(result)




