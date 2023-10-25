def mergeSort(seq, sinistra, centro, destra):
    """
    Data una lista, e rispettivamente gli elementi in testa, al centro ed alla coda della lista,
    si calcolano il numero di elementi per lato e si ordinano con confronto tra sin e des
    """

    # Reset conteggio
    conteggio_scambi = 0
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
        
        # Se l'elemento a destra è <= di quello a sinistra lo ordino prima, ed aumento SOLO L'INDICE DI DESTRA
        else:
            seq[k] = lista_destra[j]
            j += 1
            # Aggiungo al conteggio il numero di tutti gli elementi della lista di sinistra che stiamo saltando
            conteggio_scambi += (lunghezza_sinistra - i)
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

    return conteggio_scambi

def mergeSplit(seq, sinistra, destra):
    """
    Data una lista, il suo valore più a "sinistra" (il primo) ed il suo valore più a "destra" (l'ultimo)
    la spezza a metà e ripete ricorsivamente la cosa finchà possibile, infine conta gli scambi avvenuti
    """

    # Inizializzo il conteggio a 0
    conteggio_scambi = 0

    # Se posso dividere, divido (se l'elemento a sinistra è >= di quello a destra non ha senso dividere)
    if sinistra < destra:
        # Trovo il centro con la divisione intera ( // ) 
        centro = (sinistra + destra) // 2

        # Ricorsione da sinistra al centro e da centro+1 a destra
        conteggio_scambi += mergeSplit(seq, sinistra, centro)
        conteggio_scambi += mergeSplit(seq, centro + 1, destra)

        # Avvio il sort
        conteggio_scambi +=  mergeSort(seq, sinistra, centro, destra)

    return conteggio_scambi

if __name__ == "__main__":
    while True:
        # Inserimento lunghezza sequenza
        lunghezza_sequenza = int(input())

        # Se lunghezza è 0 ferma il programma
        if lunghezza_sequenza == 0:
            break

        # La sequenza è una serie di input di numero pari a lunghezza_sequenza
        sequenza = [int(input()) for k in range(lunghezza_sequenza)]
        
        # Conto il numero di scambi della sequenza
        inversioni_totali = mergeSplit(sequenza, 0, len(sequenza) - 1)
        
        # Stampo a video
        print(inversioni_totali,"\n")

#------------------------------------------------------------------------------------------
# La complessità è quella di un merge-sort: O(n*log(n))

# CASI DI TEST:
# Sample Input 
# 10
# 9
# 8
# 6
# 3
# 2
# 0
# 1
# 5
# 4
# 7
# Sample Output
# 29

# Sample Input 
# 6
# 9
# 1
# 0
# 5
# 4
# 71
# Sample Output
# 6

# Sample Input 
# 3
# 1
# 2
# 3
# Sample Output
# 0
