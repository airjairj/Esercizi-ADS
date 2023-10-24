def cerca(sinistra, destra):
    """
    Date due stringhe le scorre per cercare una sottostringa, usando la più breve come riferimento.
    Ritorna un prefisso comune
    """

    # Cerco il più piccolo, cosi da fare meno cicli
    min_len = min(len(sinistra), len(destra))

    # Comparo le due stringhe lettera a lettera
    for i in range(min_len):
        if sinistra[i] != destra[i]:
            return sinistra[:i]
    return sinistra[:min_len]

def split(lista, sinistra, destra):
    """
    Data una lista, il suo valore più a "sinistra" (il primo) ed il suo valore più a "destra" (l'ultimo)
    la spezza a metà e ripete ricorsivamente la cosa finchà possibile
    """
        
    if sinistra == destra:
        return lista[sinistra]

    centro = (sinistra + destra) // 2

    prefisso_sin = split(lista, sinistra, centro)
    prefisso_des = split(lista, centro + 1, destra)

    return cerca(prefisso_sin, prefisso_des)


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

#------------------------------------------------------------------------------------------
# La complessità è : O(m*log(n)), 
# con n è il numero di stringhe ed m è la lunghezza massima di una singola stringa nell'input.