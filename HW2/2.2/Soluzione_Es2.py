def trovaPosizioni(n):
    def cercaSicuro(riga, colonna):
        # Check the column
        for i in range(riga):
            if scacchiera[i][colonna] == "Q":
                return False

        # Check the upper-left diagonal
        i, j = riga, colonna
        while i >= 0 and j >= 0:
            if scacchiera[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check the upper-right diagonal
        i, j = riga, colonna
        while i >= 0 and j < n:
            if scacchiera[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    scacchiera = [["." for _ in range(n)] for _ in range(n)]
    q_piazzate = 0
    colonna = 0

    while q_piazzate != n:
        for i in range(n):
            if cercaSicuro(i, colonna):
                scacchiera[i][colonna] = "Q"
                q_piazzate += 1
                colonna += 1
                break
        else:
            # If no safe position was found, backtrack
            if colonna == 0:
                return None  # No solution found
            colonna -= 1
            for i in range(n):
                if scacchiera[i][colonna] == "Q":
                    scacchiera[i][colonna] = "."
                    q_piazzate -= 1

    return scacchiera

if __name__ == "__main__":
    numero = int(input("n = : "))
    output = trovaPosizioni(numero)
    if output is not None:
        for riga in output:
            print(" ".join(riga))
    else:
        print("Nessuna soluzione trovata")
