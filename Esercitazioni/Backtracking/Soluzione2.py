def Soluzione(pista, dim_riga, dim_col, riga, col, attuale):
    
    if not (0 <= riga < dim_riga) or not (0 <= col < dim_col):
        return attuale

    max_attuale = attuale  # Keep track of the current path length

    if col < dim_col - 1 and pista[riga][col + 1] < pista[riga][col]:
        result = Soluzione(pista, dim_riga, dim_col, riga, col + 1, attuale + 1)
        max_attuale = max(max_attuale, result)

    if col >= 0 and pista[riga][col - 1] < pista[riga][col]:
        result = Soluzione(pista, dim_riga, dim_col, riga, col - 1, attuale + 1)
        max_attuale = max(max_attuale, result)

    if riga < dim_riga - 1 and pista[riga + 1][col] < pista[riga][col]:
        result = Soluzione(pista, dim_riga, dim_col, riga + 1, col, attuale + 1)
        max_attuale = max(max_attuale, result)

    if riga >= 0 and pista[riga - 1][col] < pista[riga][col]:
        result = Soluzione(pista, dim_riga, dim_col, riga - 1, col, attuale + 1)
        max_attuale = max(max_attuale, result)

    return max_attuale

with open("Esercitazioni/Backtracking/TestCase2.txt", "r") as file:
    num_test = int(file.readline())

    while num_test > 0:
        nome = file.readline().strip()
        dim_mat = list(map(int, file.readline().split()))
        righe, col = dim_mat[0], dim_mat[1]

        pista = []
        for _ in range(righe):
            pista.append(list(map(int, file.readline().split())))

        print("Pista:")
        for riga in pista:
            print(riga)

        attuale_output = 0
        for i in range(righe):
            for j in range(col):
                output = Soluzione(pista, righe, col, i, j, 1)
                attuale_output = max(attuale_output, output)

        print(attuale_output)

        num_test -= 1
