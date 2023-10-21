#region INFO
#
# Basato sulla struttura dati heap, versione max-heap
#
# Complessità: 
# Caso peggiore: O(nlog(n))
#
# Ordina sul posto
#
#endregion

def heapify(lista, n, i): # Con heapify mantengo sempre l'elemento maggiore in testa, per poi rimuoverlo dopo
    maggiore = i                  # Inizialmente il maggiore è l'indice
    figlio_sinistro = 2 * i + 1   # Suo figlio sinistro
    figlio_destro = 2 * i + 2     # Suo figlio destro

    if figlio_sinistro < n and lista[figlio_sinistro] > lista[maggiore]: # Se il figlio sinistro è maggiore del padre lo nomino maggiore
        maggiore = figlio_sinistro

    if figlio_destro < n and lista[figlio_destro] > lista[maggiore]: # Se il figlio destro è maggiore del padre lo nomino maggiore
        maggiore = figlio_destro

    if maggiore != i: # Se il maggiore è cambiato, scambio l'indice (che è la radice) con il maggiore
        lista[i], lista[maggiore] = lista[maggiore], lista[i]
        heapify(lista, n, maggiore) # Richiamo heapify per ordinare

def heap_sort(lista):
    n = len(lista)

    # Costruisco un max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Estraggo un elemento alla volta
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # Scambio la radice con l'ultimo elemento
        heapify(lista, i, 0)  # Richiamo heapify per ordinare

# Caso di test
nuova_lista = [12, 11, 13, 5, 6, 7]
heap_sort(nuova_lista)
print("Lista ordinata:", nuova_lista)