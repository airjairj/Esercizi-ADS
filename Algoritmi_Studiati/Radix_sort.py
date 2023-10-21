#region INFO
#
# Ordina i valori a partire dalla cifra meno significativa
#
# Complessità
# Caso peggiore: Θ(d(n+k))
#
# NON ordina sul posto
#
#endregion

def radix_sort(lista):
    # Trovo il valore max per sapere il numero di cifre
    valore_max = max(lista)
    num_cifre = len(str(valore_max))

    for cifra in range(num_cifre):
        # Creo 10 gruppi (0-9)
        gruppi = [[] for _ in range(10)]

        # Distribuisco gli elementi nei gruppi in base alle cifre
        for num in lista:
            digit_value = (num // 10**cifra) % 10
            gruppi[digit_value].append(num)

        # Rimetto insieme ed in ordine
        lista = []
        for bucket in gruppi:
            lista.extend(bucket)

    return lista

# Example usage
nuova_lista = [170, 45, 75, 90, 802, 24, 2, 66]
nuova_lista = radix_sort(nuova_lista)
print("Lista ordinata:", nuova_lista)