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
    # Se sono alla fine dell'albero ritorno l'elemento  
    if sinistra == destra:
        return lista[sinistra]

    # Calcolo il centro con la divisione intera
    centro = (sinistra + destra) // 2

    # Richiamo la funzione a sinistra e a destra
    prefisso_sin = split(lista, sinistra, centro)
    prefisso_des = split(lista, centro + 1, destra)

    # Ritorno il valore ottenuto con la funzione di ricerca del prefisso
    return cerca(prefisso_sin, prefisso_des)

if __name__ == "__main__":
    # Inserimento numero di esecuzioni
    num_esecuzioni = int(input())
    
    while num_esecuzioni > 0:
        
        stringhe = []
        
        prefisso = ""

        # Se è 0 termina
        if num_esecuzioni <= 0:
            break

        # La sequenza è una serie di input di numero pari a num_esecuzioni
        tastiera = input()
        while tastiera != "":
            stringhe.append(tastiera)
            tastiera = input()
            

        prefisso = split(stringhe, 0, len(stringhe)-1)

        # Stampo a video
        print(prefisso)
        num_esecuzioni -= 1

#------------------------------------------------------------------------------------------
# La complessità è : O(m*log(n)), 
# con n è il numero di stringhe ed m è la lunghezza massima di una singola stringa nell'input.
# Lo split avviene ricorsivamente ed ha quindi complessità O(log(n)).
# La ricerca del prefisso avviene invece con un ciclo che "gira" per k volte, dove k è la stringa minore
# tra le 2 stringhe confrontate, chiamo m la lunghezza massima di una singola stringha, e quindi la
# complessità per la ricerca è O(m)
# La complessità totale è quindi O(m*log(n))

# CASI DI TEST:
# Sample Input (N.B. per terminare il caso di test premere solo invio, senza scrivere nulla)
# 1
# apple
# ape
# april
# applied
# 
# Sample Output
# ap

# Sample Input 
# 2
# fiore
# albero
# casa
# fiorire
# alberto
#
# Sample Output
#
# pesca
# partita
# partire
# peso
#
# Sample Output
# p

# Sample Input
# 1
# fiore
# fiorellino
# fioraio
# fiorista
# fiori
#
# Sample Output
# fior
