# Capita, e ci è già capitato, di dover salvare in memoria (dentro una variabile) delle informazioni su più
# "entità" della stessa categoria
# es: avremmo usato per segnare 3 temperature le variabili temp1, temp2 e temp3
# es: abbiamo usato per salvare 2 voti universitari le variabili voto1, voto2
# Questo approccio è molto scomodo per due motivi:
#   1. Se le temperature o i voti raddoppiano, dobbiamo usare e dichiarare il doppio delle variabili
#   2. Al variare del numero di variabili bisogna anche duplicare il codice per gestirle / elaborarle etc

# Per risolvere questi problemi utilizziamo una nuova struttura -> LISTA / TUPLA
# Cos'hanno in comune lista e tupla:
# * Servono per memorizzare un elenco di oggetti che appartengono alla stessa categoria e sono ordinati
#   es: un elenco di temperature, un elenco di voti, un elenco di nomi, un elenco di numeri
#   -> cosa vuol dire "ordinati": esiste un primo elemento, un secondo elemento etc fino all'ultimo elemento
#   gli elementi si dice che sono indicizzati dalla posizione
# Cosa c'è di diverso tra liste e tuple:
# * Le liste si possono modificare e le tuple NO: posso aggiungere/togliere/modificare un elemento della lista, tuple no
# * Le tuple in Python, siccome non sono modificabili, sono molto più veloci ed efficienti

# Da ora in poi i nostri voti li otterremo come
# 1. Dichiarazione della lista vuota
lista_voti = []  # Notiamo che le liste utilizzano le parentesi quadre
# Se volessimo metterci già dentro dei valori useremmo lista_voti = [20, 21, 30]

# 2. Per aggiungere un voto alla volta usiamo il metodo append() che python ci mette a disposizione
lista_voti.append(30)
lista_voti.append(24)
lista_voti.append(26)
lista_voti.append(21)  # Quarto voto che verrà eliminato
lista_voti.append(23)

# 3. Per eliminare un elemento possiamo fare diverse cose ma la più importante è rimuovere da indice
lista_voti.pop(3)  # Togliamo il quarto elemento -> in python si conta da 0 -> il primo elemento ha indice 0

# 4. Proviamo a stampare la lista
print(f"Lista: {lista_voti}")

# Se volessimo fare una tupla di voti, dovremmo già dichiarare finita
tupla_voti = (30, 24, 26, 23)  # Per le tuple si usano le parentesi tonde
print(f"Tupla voti: {tupla_voti}")

# 5. Accediamo e modifichiamo un elemento di una lista con la seguente sintassi
indice = 2  # Dichiariamo una variabile intera che conterrà l'indice -> posizione indice + 1
print(f"L'elemento ad indice {indice} è {lista_voti[indice]}")  # Andiamo dentro la lista al nostro indice

# per la modifica trattiamo lista[indice] come se fosse una variabile
lista_voti[indice] = 29  # Da ora nella posizione dell'indice ci sarà 29
print(f"L'elemento ad indice {indice} è {lista_voti[indice]}")  # Andiamo dentro la lista al nostro indice

# Per accedere agli elementi delle tuple si usa la stessa sintassi, ovviamente questi elementi non possono essere modificati
print(f"L'elemento ad indice {indice} è {tupla_voti[indice]}")  # Andiamo dentro la lista al nostro indice

# Approfondimento: accesso a più elementi -> VALIDO SIA PER LISTE CHE PER TUPLE
# 1. Accesso all'ultimo elemento
# In python per ottenere l'ultimo elemento di una lista, senza saperne la lunghezza -> usiamo l'indice -1
print(f"L'ultimo elemento è {lista_voti[-1]}")  # NB: Questa sintassi vale solo in Python (e forse in Julia)

# 2. Accesso a una sottolista
indice_partenza = 1  # Indice di partenza della sottolista -> verrà compreso nella sottolista
indice_fine = 3  # Indice di fine della sottolista -> NON verrà compreso nella sottolista
# -> la sottolista si fermerà all'indice subito prima
print(f"La sottolista di indici [{indice_partenza}, {indice_fine}) è {lista_voti[indice_partenza:indice_fine]}")
# Altri esempi -> lista[1:4], lista[0:-1], lista[4:9]


