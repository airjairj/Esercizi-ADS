def Soluzione(labirinto, target, riga, col, percorso):
    if riga == target and col == target:                                # Controllo se sono al target
        percorso.append((col, riga))                                    # Appendo l'ultimo passo
        return percorso                                                 # Ritorno

    if col < target and labirinto[riga][col + 1] == 1:                  # Vado a destra
        percorso.append((col, riga))                                    # Appendo l'ultimo passo
        result = Soluzione(labirinto, target, riga, col + 1, percorso)  # Ricorsivamente continuo il percorso
        if result is not None:                                          # Se il risultato ricorsivo NON è nullo
            return result                                               # Lo ritorno
        percorso.pop()                                                  # Altrimenti faccio pop perchè devo tornare indietro

    if riga < target and labirinto[riga + 1][col] == 1:                 # Vado in basso
        percorso.append((col, riga))                                    # Appendo l'ultimo passo
        result = Soluzione(labirinto, target, riga + 1, col, percorso)  # Ricorsivamente continuo il percorso
        if result is not None:                                          # Se il risultato ricorsivo NON è nullo
            return result                                               # Lo ritorno
        percorso.pop()                                                  # Altrimenti faccio pop perchè devo tornare indietro

    return None

with open("C:\\Users\\GAMING EDGE\\Desktop\\UNI\\MAGISTRALE\\1o ANNO\\1o SEMESTRE\\Algoritmi e data structures\\ADS\\Esercitazioni\\Backtracking\\TestCase.txt", "r") as file:
    num_test = int(file.readline())

    while num_test > 0:
        grandezza_lab = int(file.readline())
        lab = [[0 for _ in range(grandezza_lab)] for _ in range(grandezza_lab)]

        for i in range(grandezza_lab):
            lab[i] = list(map(int, file.readline().split()))

        for riga in lab:
            print(riga)

        path = []
        output = Soluzione(lab, grandezza_lab - 1, 0, 0, path)

        if output is not None:
            print("Percorso trovato:")
            print(output)
        else:
            print("Nessun percorso trovato.")

        num_test -= 1
