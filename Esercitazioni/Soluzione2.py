def mergeSort(seq, sinistra, centro, destra):
    # Reset conteggio
    distanza = []
    # Calcolo del numero di elementi a sinistra e a destra
    lunghezza_sinistra = centro - sinistra + 1
    lunghezza_destra = destra - centro

    # Faccio slicing della sequenza in 2 liste, una che va da sinistra al centro, e l'altra che va dal centro+1 a destra
    lista_sinistra = seq[sinistra:centro + 1]
    lista_destra = seq[centro + 1:destra + 1]

    # Contatori
    i, j, k = 0, 0, sinistra

    # Faccio il merge confrontando ogni elemento a sinistra e destra, quindi fino a che ho da confrontare:
    while i < lunghezza_sinistra and j < lunghezza_destra:
        # Se l'elemento a sinistra è <= di quello a destra lo ordino prima, ed aumento SOLO L'INDICE DI SINISTRA
        if lista_sinistra[i] <= lista_destra[j]:
            seq[k] = lista_sinistra[i]
            i += 1
            distanza[k] += abs(lista_sinistra[i] - lista_destra[j])
        
        # Se l'elemento a destra è <= di quello a sinistra lo ordino prima, ed aumento SOLO L'INDICE DI DESTRA
        else:
            seq[k] = lista_destra[j]
            j += 1
            distanza[k] += abs(lista_sinistra[i] - lista_destra[j])

        k += 1

    # Quando una delle due lista termina prima dell'altra aggiungo gli elementi di quella che è rimastra alla sequenza
    while i < lunghezza_sinistra:
        seq[k] = lista_sinistra[i]
        i += 1
        k += 1

    while j < lunghezza_destra:
        seq[k] = lista_destra[j]
        j += 1
        k += 1

    d_min= 0

    for kk in distanza:
        
        if d_min > distanza[kk]:
            d_min = distanza[kk]

    return d_min

def mergeSplit(seq, sinistra, destra):
    # Inizializzo il conteggio a 0
    distanza = 0

    # Se posso dividere, divido (se l'elemento a sinistra è >= di quello a destra non ha senso dividere)
    if sinistra < destra:
        # Trovo il centro con la divisione intera ( // ) 
        centro = (sinistra + destra) // 2

        # Ricorsione da sinistra al centro e da centro+1 a destra
        distanza = mergeSplit(seq, sinistra, centro)
        distanza = mergeSplit(seq, centro + 1, destra)

        # Avvio il sort
        distanza =  mergeSort(seq, sinistra, centro, destra)

    return distanza

if __name__ == "__main__":
    num_test = int(input("Inserisci il numero di test case:"))

    while num_test > 0:
        num_depth = int(input("Inserisci il numero di profondità:"))
        
        num_palla = int(input("Inserisci il numero di palla:"))
        
        mergeSplit(num_depth, 0, len(num_civici)-1)

        num_test -= 1