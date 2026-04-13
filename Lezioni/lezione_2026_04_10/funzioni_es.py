"""
Facciamo una funzione per calcolare la media di una lista NON ORDINATA
Usiamo la stessa funzione per calcolare la deviazione standard:
    1. Calcolo della media
    2. Si fa una lista con le differenze tra gli elementi della lista originale e la media
    3. Ogni elemento di questa lista si eleva al quadrato
    4. Si fa la media (sempre con la funzione di prima) di questa nuova lista
    5. Si fa la radice quadrata di questa media
Facciamo una funzione che data una lista ne calcoli media e deviazione standard e le stampi in questo modo:
Lista: [...], Media: media:.2f, Std: std:.2f

# --------------------- BONUS ---------------------
Calcoliamo anche la massima differenza tra i membri della lista e la mettiamo nella stampa di sopra
"""
# Definiamo una funzione chiamata "calcola_media" che prende come parametro una lista di numeri float e la chiama
# "lista"
def calcola_media(lista: list[float]):
    media = sum(lista) / len(lista)  # Calcoliamo la media
    return media  # Facciamo uscire in output il valore della media dalla funzione

# TODO: Fare una funzione per il AMSE -> Absolute Mean Squared Error
def calcola_deviazione_standard(lista: list[float]):  # Spesso si chiama anche RMSE -> Root Mean Squared Error
    # 1. Calcolo della media
    media = calcola_media(lista)  # Calcoliamo la media della lista dentro la funzione usando la funzione di prima

    # 2-3. Calcolo delle differenze al quadrato
    # Facciamo la lista in cui metteremo le differenze con la media. Per evitare di dover allungare la lista man mano,
    # la creiamo già della lunghezza finale <len(lista)> e come valori ci mettiamo già dentro quelli della media
    lista_differenze = [media] * len(lista)  # stiamo facendo una lista [media, media, media, ... , media] lunga len(lista)
    for i in range(len(lista)):  # Per ogni numero della lista
        # differenza = numero - media  # Calcoliamo la differenza
        # differenza_quadrata = differenza ** 2  # Eleviamo la differenza al quadrato
        # lista_differenze.append(differenza_quadrata)  # Aggiungiamo la differenza alla lista differenze

        # per ogni i prendiamo la media salvata in quella posizione e ci togliamo il valore della lista a quella stessa
        # posizione
        lista_differenze[i] -= lista[i]
        lista_differenze[i] **= 2  # successivamente lo eleviamo al quadrato

    # lista_differenze = [(numero - media) ** 2 for numero in lista]  # Questo fa esattamente i punti 2-3

    # 4. Media della nuova lista
    varianza = calcola_media(lista_differenze)  # Usiamo di nuovo la funzione di prima su questa nuova lista

    # 5. Calcoliamo la radice quadrata della varianza
    deviazione_std = varianza ** 0.5

    return deviazione_std  # Diamo il risultato del nostro calcolo in output a chi ha chiamato la funzione

def stampa(lista: list[float]):
    media = calcola_media(lista)
    dev_std = calcola_deviazione_standard(lista)

    print(f"Lista: {lista}, Media: {media:.2f}, Std: {dev_std:.2f}")


if __name__ == "__main__":
    lista_prova = [1, 2, 4, 6]
    # Chiamiamo la funzione calcola_media passandole lista_prova. Il risultato verrà messo dentro media_prova
    media_prova = calcola_media(lista_prova)
    print(f"Media calcolata: {media_prova:.2f}")  # ":.2f" stampa la media_prova arrotondata a 2 cifre dopo la virgola

    dev_std_prova = calcola_deviazione_standard(lista_prova)
    print(f"Deviazione standard calcolata: {dev_std_prova:.2f}")
