# facciamo una funzione per prendere un input numerico in un range
def input_range(messaggio_input: str, valore_min, valore_max, to_int: bool):
    """
    Funzione che usiamo per prendere un input con un while in modo che rispetti il range
    :param to_int: variabile per dire se il numero vada convertito a intero o lasciato float
    :param messaggio_input: Messaggio da dare per chiedere il numero
    :param valore_min: minimo del range (escluso)
    :param valore_max: massimo del range (escluso)
    :return: il valore richiesto
    """
    # Facciamo il solito while true da interrompere una volta che abbiamo ottenuto ciò che ci serviva
    while True:
        numero_inserito = float(input(messaggio_input))  # Prendiamo in input il numero

        if to_int:
            # convertiamo il numero da float ad intero
            numero_inserito = int(numero_inserito)

        if valore_min < numero_inserito < valore_max:  # Se il numero rispetta il range
            # interrompiamo il while e la funzione per restituire il numero inserito in input
            return numero_inserito  # NB: il return interrompe SEMPRE TUTTA la funzione

        # Se non abbiamo interrotto già la funzione, ci troviamo qua
        print(f"Il numero inserito non rispetta il range ({valore_min}, {valore_max})")

giorno = input_range("Inserisci il giorno: ", 0, 32, True)
mese = input_range("Inserisci il mese: ", 0, 13, True)
anno = input_range("Inserisci l'anno: ", 2000, 2026, True)

print(f"giorno: {giorno}")
print(f"mese: {mese}")
print(f"anno: {anno}")
