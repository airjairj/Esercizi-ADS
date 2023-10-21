#region INFO
#
# Per ciascun intero i compreso tra 0 e k, si contano quanti elementi pari ad i ci sono nel vettore da ordinare
# Per ciascun intero i compreso tra 0 e k, si determinano quanti elementi minori o uguali ad i ci sono nel vettore da ordinare
# Ciò ci indica in che posizione deve stare ciascun elemento
#
# Complessità
# Caso peggiore: Θ(n)
#
# NON ordina sul posto
#
#endregion

def counting_sort(lista):
    # Trovo il massimo valore nell'array di input
    valore_max = max(lista)
    
    # Creo una lista di conteggio per conservare il numero dei vari elementi
    conteggio = [0] * (valore_max + 1)
    
    # Conto le occorrenze dei vari elementi
    for num in lista:
        conteggio[num] += 1

    # Ricostruisco la lista a conti fatti
    output = []
    for i in range(len(conteggio)):
        output.extend([i] * conteggio[i])

    return output

# Example usage:
nuova_lista = [4, 2, 2, 8, 3, 3, 1]
nuova_lista = counting_sort(nuova_lista)
print("Lista ordinata:", nuova_lista)