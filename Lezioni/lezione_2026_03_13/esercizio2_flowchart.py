# 1. Otteniamo i dati necessari in input
distanza = float(input("Inserisci la distanza (km): "))
durata_viaggio = float(input("Inserisci la durata del viaggio (h): "))
litri_consumati = float(input("Inserisci i litri consumati (L): "))
prezzo_litro = float(input("Inserisci costo al litro della benzina (€/L): "))

# 2. Calcoliamo il necessario
velocita_media = distanza / durata_viaggio
consumo_medio = distanza / litri_consumati
spesa_totale = litri_consumati * prezzo_litro

# 3. Stampiamo cosa abbiamo ottenuto
print(f"{'=' * 20} Dati iniziali {'=' * 20}")
print(f" * Distanza: {distanza} km")
print(f" * Durata del viaggio: {durata_viaggio} h")
print(f" * Litri di benzina usati: {litri_consumati} L")
print(f" * Prezzo della benzina: {prezzo_litro} €/L")

print(f"{'=' * 20} Risultati {'=' * 20}")
print(f"Velocità media: {velocita_media} km/h")
print(f"Consumo medio: {consumo_medio} km/L")
print(f"Costo totale benzina: {spesa_totale} €")
