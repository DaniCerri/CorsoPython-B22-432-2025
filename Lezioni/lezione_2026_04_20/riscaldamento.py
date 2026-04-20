def fibo(n: int):
    """
    calcola (partendo con n che parte da 1) l'enne-simo numero di fibonacci
    :param n: enne-simo da calcolare
    :return: valore di fibonacci numero n
    """
    # controlliamo che n > 0, altrimenti diamo errore
    assert n > 0, "n deve essere > 0"
    if n == 1:
        return 0  # Sappiamo che il primo numero della serie è 1
    if n == 2:
        return 1  # Sappiamo che il secondo numero della serie è 2

    # Calcoliamo gli altri in maniera ricorsiva sommando i due precedenti
    return fibo(n-1) + fibo(n-2)

if __name__ == "__main__":
    for i in range(3, 30):
        a = fibo(i)
        b = fibo(i - 1)
        print(f"Approssimazione rapporto aureo ({i} / {i-1}): {a / b}")
        # rapporto aureo: 1.6180339887
    # print(f"Numero di fibonacci n° {5}: {fibo(5)}")
    # print(f"Numero di fibonacci n° {10}: {fibo(10)}")
    # print(f"Numero di fibonacci n° {12}: {fibo(12)}")
    # print(f"Numero di fibonacci n° {-1}: {fibo(-1)}")
