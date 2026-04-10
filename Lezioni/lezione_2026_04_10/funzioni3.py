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

# Esercizio 3: fare una funzione che prenda due numeri interi e dica True se esiste un numero che li
# divida entrambi, False altrimenti
# a è divisibile per b se a % b == 0
def not_coprimi(numero1: int, numero2: int):
    riferimento = min(numero1, numero2)  # Prendiamo il minore come riferimento
    if numero1 % 2 == 0 and numero2 % 2 == 0:  # Controlliamo subito se sono entrambi pari
        return True

    print(int(riferimento ** 0.5) + 1)
    # Per ogni numero i da 3 alla radice del riferimento + 1, a salti di due -> [3, 5, 7, ...]

    # TODO: trovare il miglior numero centrale per fare meno controlli possibile
    for i in range(3, int(riferimento // 2) + 1, 2):
    # for i in range(int(riferimento // 2) + 1, 3, -2):  # [..., 7, 5, 3] Per fare questo dovremmo sapere se si parte da un numero pari o dispari
        print(i)
        if numero1 % i == 0 and numero2 % i == 0:
            return True

    return False




if __name__ == "__main__":
    # lista_di_stringhe = ["ciao", "come", "va"]
    # print(lista_di_stringhe)
    # lista_maiusc = lista_maiuscola(lista_di_stringhe)
    # print(lista_maiusc)
    # numero_int = 10
    # result = calcoli(numero_int)
    # print(result)
    num1, num2 = 10, 15
    print(not_coprimi(num1, num2))



