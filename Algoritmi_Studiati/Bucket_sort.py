#region INFO
#
# Assume che gli elementi da ordinare siano distribuiti uniformemente sull'intervallo [0,1)
# Dividere l'intervallo [0,1) in n sottointervalli uguali e distribuire gli n elementi in tali sottointervalli
#
# Complessità
# Caso peggiore: Θ(n)
#
# NON ordina sul posto
#
#endregion

def bucket_sort(lista):
    if len(lista) == 0:
        return lista

    # Trovo max e min
    valore_min, valore_max = min(lista), max(lista)
    
    # Creo buckets vuoti, in numero che dipende dal max e min
    num_buckets = int((valore_max - valore_min) // len(lista) + 1)
    buckets = [[] for _ in range(num_buckets)]

    # Distribuisco gli elementi nei buckets
    for num in lista:
        indice = int((num - valore_min) // len(lista))
        buckets[indice].append(num)

    # Sorto i buckets (uso sort tanto posso usare quello che mi pare)
    for i in range(num_buckets):
        buckets[i].sort()

    # Concateno i bucket in ordine per avere il risultato finale
    buckets_ordinati = []
    for i in range(num_buckets):
        buckets_ordinati.extend(buckets[i])

    return buckets_ordinati

# Example usage:
nuova_lista = [0.12, 0.31, 1.0, 0.65, 0.90, 0.27, 0.54, 0.48, 0.88, 0.33, 0.62, 0.93, 0.22, 0.57, 0.43, 0.86]
nuova_lista = bucket_sort(nuova_lista)
print("Lista ordinata:", nuova_lista)
