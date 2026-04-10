# facciamo una funzione per prendere un input numerico in un range
def input_range(messaggio_input: str, valore_min, valore_max,
                to_int: bool, includi_min=True, includi_max=True):  # Settiamo di default le inclusioni a True
    """
    Funzione che usiamo per prendere un input con un while in modo che rispetti il range
    :param includi_max: impostare a True per includere il massimo nei valori possibili
    :param includi_min: impostare a True per includere il minimo nei valori possibili
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

        rispetta_range = True  # Inizializziamo una variabile per tenere traccia di eventuali incompatibilità

        # Ora ci chiediamo quand'è che il range non viene rispettato
        if (numero_inserito <= valore_min and not includi_min) or (numero_inserito < valore_min and includi_min):
            rispetta_range = False

        if (numero_inserito >= valore_max and not includi_max) or (numero_inserito > valore_max and includi_max):
            rispetta_range = False

        if rispetta_range:  # Se il numero rispetta il range
            # interrompiamo il while e la funzione per restituire il numero inserito in input
            return numero_inserito  # NB: il return interrompe SEMPRE TUTTA la funzione

        # Se non abbiamo interrotto già la funzione, ci troviamo qua
        print(f"Il numero inserito non rispetta il range ({valore_min}, {valore_max})")


if __name__ == "__main__":
    giorno = input_range("Inserisci il giorno: ", 0, 32,
                         True, False, False)  # qua minimo e massimo non saranno inclusi
    mese = input_range("Inserisci il mese: ", 1, 12,
                       True)  # Siccome non abbiamo detto niente, di default minimo e massimo saranno inclusi
    anno = input_range("Inserisci l'anno: ", 2000, 2026, True)

    print(f"giorno: {giorno}")
    print(f"mese: {mese}")
    print(f"anno: {anno}")
