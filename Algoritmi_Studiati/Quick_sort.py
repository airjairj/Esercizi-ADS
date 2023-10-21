#region INFO
#
# Scelto un elemento x, detto pivot, partiziona l'array A[p..r] in due
# sottoarray tali che A[p..q-1] contiene gli elementi <= di x e A[q+1..r]
# contiene gli elementi >x 
# Il pivot va in A[q]
#
# Complessità
# Caso peggiore: O(n^2)
# Caso medio: O(nlog(n))
#
# Ordina sul posto
#
#endregion

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2]  # Scelgo un pivot
    sinistra = [x for x in lista if x < pivot]  # A sinistra vanno tutti quelli minori del pivot
    centro = [x for x in lista if x == pivot]  # Al centro tutti quelli uguali al pivot
    destra = [x for x in lista if x > pivot]  # A destra vanno tutti quelli magiori del pivot

    # Richiamo quicksort a sinistra ed a destra per ordinare
    return quick_sort(sinistra) + centro + quick_sort(destra)

# Caso di test
nuova_lista = [12, 11, 13, 5, 6, 7]
nuova_lista = quick_sort(nuova_lista)
print("Lista ordinata:", nuova_lista)