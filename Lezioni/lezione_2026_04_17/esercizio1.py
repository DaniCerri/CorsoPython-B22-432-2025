# facciamo una funzione che prenda i dati e li inserisca dentro un dizionario che poi
# verrà restituito.
# Dati: data (13/12/2012), ora (12:00), temperatura (°C), umidità (%)
def registrazione_to_dict(data: str, ora: str, temperatura: float, umidita: float):
    """
    Prende i dati singoli e li aggrega in un dizionario
    :param data: stringa formattata come "dd/MM/YYYY"
    :param ora: stringa formattata come "hh:mm"
    :param temperatura: temperatura in °C
    :param umidita: % di umidità espressa come coefficiente es: 50% -> 0.5
    :return: dizionario con i dati, chiavi: data, ora, temp, umidita
    """
    # formattazione: come viene presentata la stringa
    # TODO: fare controlli per la corretta formattazione di data e ora
    # TODO: controllare che la temperatura sia >= -273.15
    # TODO: controllare che l'umidita sia tra 0 e 1 compresi

    dizionario = {
        "data": data,
        "ora": ora,
        "temp": round(temperatura, 2),
        "umidita": round(umidita, 4)  # Per avere due cifre decimali della percentuale
    }
    return dizionario

# TODO: fare anche una funzione per processare con registrazione_to_dict una lista di misurazioni
#  e ottenere una lista di dizionari [OPZIONALE]

# facciamo poi una funzione che data una lista di registrazioni nel calcoli temperatura e
# umidità medie e le restituisca
def medie(lista_registrazioni: list[dict]):
    # TODO: fare funzione per fare la media di una chiave di una lista di dizionari
    #  prenderà la lista di dizionari e la chiave di cui fare la media
    tot_temp, tot_um = 0, 0
    for diz_registrazione in lista_registrazioni:
        tot_temp += diz_registrazione['temp']
        tot_um += diz_registrazione['umidita']
    media_temp = tot_temp / len(lista_registrazioni)
    media_um = tot_um / len(lista_registrazioni)
    return media_temp, media_um

# TODO: fare funzione conversione in Farenheit

def stampa_misurazione(misurazione: dict):
    return (f"  * {misurazione['data']} {misurazione['ora']} : "
            f"{misurazione['temp']:.2f} °C | {misurazione['umidita']:.2%}")

def stampa_elenco_misurazioni(lista_misurazioni: list[dict]):
    output = ""
    for misurazione in lista_misurazioni:
        output += f"{stampa_misurazione(misurazione)}\n"

    # output = "\n".join(mis for mis in lista_misurazioni)
    return output

# Per i test
if __name__ == "__main__":
    # Possiamo passare una tupla a una funzione
    # usando un "*" davanti al nome della tupla
    # Questo la scompone nei suoi componenti e li passa alla funzione nell'ordine
    # in cui appaiono nella tupla
    lista_misurazioni = [
        ("17/04/2026", "17:48", 24, 0.45),
        ("18/04/2026", "16:48", 12, 0.55),
        ("19/04/2026", "17:38", 43.2, 0.24),
        ("20/04/2026", "18:48", 12.2, 0.96),
        ("21/04/2026", "16:28", 10.12, 0.12),
        ("22/04/2026", "14:18", 10.2, 0.18),
    ]
    lista_dizionari = []
    for misurazione in lista_misurazioni:
        # diz2 = registrazione_to_dict(misurazione[0], ..., misurazione[-1])
        diz2 = registrazione_to_dict(*misurazione)
        lista_dizionari.append(diz2)

    m_temp, m_um = medie(lista_dizionari)
    print(f"Temp media: {m_temp}")
    print(f"Umidità media: {m_um:.2%}")
