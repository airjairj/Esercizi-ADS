#region INFO
#
# Suddivide una sequenza di n elementi in due sottosequenze di n/2 elementi
# Ordina le sottosequenze ricorsivamente
#
# Complessità
# Caso peggiore: O(nlog(n))
#
# NON ordina sul posto
#
#endregion

def merge_sort(lista):
    # Questo if in testa mi arricura che quando arrivo al caso di 1 elemento non fa calcoli
    if len(lista) > 1:
        centro = len(lista) // 2  # Trovo il centro della lista
        lista_sinistra = lista[:centro]  # Divido la lista in due metà
        lista_destra = lista[centro:]

        merge_sort(lista_sinistra)  # Richiamo merge_sort sulle due metà
        merge_sort(lista_destra)

        i = j = k = 0

        # Confronto gli elementi di sinistra e di destra, ed ordino nella lista
        while i < len(lista_sinistra) and j < len(lista_destra):
            if lista_sinistra[i] < lista_destra[j]:
                lista[k] = lista_sinistra[i]
                i += 1
            else:
                lista[k] = lista_destra[j]
                j += 1
            k += 1

        # Se una delle due metà termina prima, inserisco i restanti elementi
        while i < len(lista_sinistra):
            lista[k] = lista_sinistra[i]
            i += 1
            k += 1

        while j < len(lista_destra):
            lista[k] = lista_destra[j]
            j += 1
            k += 1

# Caso di test
nuova_lista = [12, 11, 13, 5, 6, 7]
merge_sort(nuova_lista)
print("Lista ordinata:", nuova_lista)