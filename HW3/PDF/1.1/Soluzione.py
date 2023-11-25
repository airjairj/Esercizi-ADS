def calcolo_differenze(valori):
    bottino_totale = sum(valori)
    temp = {}

    for val in valori:
        if val not in temp:
            temp[val] = val


    '''val_tot = sum(valori)
    print("Valore totale: ",val_tot)

    # Creazione dell'array
    array = [0] * (val_tot // 2 + 1)

    print("array inizializzato:\n",array)

    # Riempimento dell'array
    for valore in valori:
        for j in range(val_tot // 2, valore - 1, -1):
            array[j] = max(array[j], array[j - valore] + valore)

    # Trova la differenza minima tra i ladri
    min_diff = val_tot - 2 * array[val_tot // 2]
    print("array post calcoli:\n",array)

    return min_diff'''

num_test = int(input("NUMERO DI CASI DI TEST: "))

while num_test > 0:

    val_monete = []
    num_monete = int(input("NUMERO DI MONETE: "))  # 1 / 50

    for _ in range(num_monete):
        val_monete.append(int(input("VALORE: ")))  # 1 / 1000

    ris = calcolo_differenze(val_monete)
    print("OUTPUT:", ris)

    num_test -= 1
