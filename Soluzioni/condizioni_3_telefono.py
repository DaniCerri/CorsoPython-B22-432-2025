tel1 = input("Primo numero di telefono: ")
tel2 = input("Secondo numero di telefono: ")

if not (tel1.startswith("3") and len(tel1) == 10 and tel1.isdigit()):
    print("Primo numero non valido")
elif not (tel2.startswith("3") and len(tel2) == 10 and tel2.isdigit()):
    print("Secondo numero non valido")
else:
    nome = input("Nome: ")
    eta = int(input("Eta: "))
    if eta >= 18:
        print("Ciao", nome + "! Iscrizione al programma confermata.")
    else:
        print("Ciao", nome + "! Devi essere maggiorenne per iscriverti.")
