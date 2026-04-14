def applica_sconto_benvenuto(prezzo_iniziale):
    return prezzo_iniziale - 5

prezzo = float(input("Inserisci il prezzo: "))
prezzo_scontato = applica_sconto_benvenuto(prezzo)
print(prezzo_scontato)