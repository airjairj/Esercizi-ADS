#region INFO
#
# Insertion Sort è un algoritmo che considera un valore alla
# volta e lo inserisce nella corretta posizione tra i valori che lo
# precedono
#
# Complessità
# Caso peggiore: O(n^2)
# Caso migliore: O(n)
#
# Ordina sul posto
#
#endregion

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chiave = lista[i]  # Salvo l'elemento alla posizione i come chiave
        j = i - 1          # Imposto j come precedente ad i 

        # Controllo sottraendo a j che gli elementi prima della chiave
        # siano tutti minori della chiave, altrimenti scambio
        while j >= 0 and chiave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        # Dopo il ciclo rimetto la chiave alla sua posizione,
        # dato che tutti quelli prima sono ora ordinati
        lista[j + 1] = chiave

# Caso di test
nuova_lista = [12, 11, 13, 5, 6, 7]
insertion_sort(nuova_lista)
print("Lista ordinata:", nuova_lista)