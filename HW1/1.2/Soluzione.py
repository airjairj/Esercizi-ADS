def cerca(str_sinistra, str_destra):
    """
    Date due stringhe le scorre per cercare una sottostringa, usando la più breve come riferimento.
    Ritorna un prefisso comune
    """

    # Inizializzo il prefisso a 0
    prefisso = ""

    # Cerco il più piccolo, cosi da fare meno cicli
    lun_min = min(len(str_sinistra), len(str_destra))

    # Comparo le due stringhe lettera a lettera
    for i in range(lun_min):
        if str_sinistra[i] == str_destra[i]:
            prefisso += str_sinistra[i]
        else:
            break

    return prefisso


def split(lista, sinistra, destra):
    """
    Data una lista, il suo valore più a "sinistra" (il primo) ed il suo valore più a "destra" (l'ultimo)
    la spezza a metà e ripete ricorsivamente la cosa finchà possibile
    """

    # Se posso dividere, divido (se l'elemento a sinistra è >= di quello a destra non ha senso dividere)
    if sinistra == destra:
        return sinistra
    
    # Trovo il centro con la divisione intera ( // ) 
    centro = (sinistra + destra) // 2

    # Ricorsione da sinistra al centro e da centro+1 a destra
    split(lista, sinistra, centro)
    split(lista, centro + 1, destra)

    return cerca(lista[sinistra], lista[destra])

if __name__ == "__main__":
    # Inserimento numero di esecuzioni
    num_esecuzioni = int(input("Inserisci il numero di esecuzioni: "))
    
    while num_esecuzioni > 0:
        
        stringhe = []
        
        prefisso = ""

        # Se è 0 termina
        if num_esecuzioni <= 0:
            break

        # La sequenza è una serie di input di numero pari a num_esecuzioni
        tastiera = input("Inserisci una stringa o lascia vuoto per elaborare quelle inserite: ")
        while tastiera != "":
            stringhe.append(tastiera)
            tastiera = input("Inserisci una stringa o lascia vuoto per elaborare quelle inserite: ")
            

        prefisso = split(stringhe, 0, len(stringhe)-1)

        # Stampo a video
        print("Prefisso comune più lungo: ", prefisso,"\n")
        num_esecuzioni -= 1