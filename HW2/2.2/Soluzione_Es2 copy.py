def trovaPosizioni(n):
    scacchiera = [["." for _ in range(n)] for _ in range(n)]
    combinazioni = 0

    def provaCombinazione(comb,scacc):
        for colonna in range(n):
            colonna_iniziale = colonna
            riga = 0
            scacc = [["." for _ in range(n)] for _ in range(n)] # Reset
            comb += piazzaRegine(riga,colonna_iniziale,n,scacc)
        return comb
        
    def piazzaRegine(r,c,n,s):
        print("PROVO")
        piazzate = 0
        spazi_rimasti = n*n
        for r in range(r,n):
            for c in range(c,n):
                # Trovato spazio libero
                if s[r][c] == ".":
                    riga_t = r
                    colonna_t = c

                    #region segno spazi vietati
                    # Cambio riga a destra
                    while colonna_t < n:
                        if s[riga_t][colonna_t] != "x":
                            s[riga_t][colonna_t] = "x"
                            spazi_rimasti -= 1
                        colonna_t +=1
                            
                    colonna_t = c
                    # Cambio riga a sinistra
                    while colonna_t >= 0:
                        if s[riga_t][colonna_t] != "x":
                            s[riga_t][colonna_t] = "x"
                            spazi_rimasti -= 1
                        colonna_t -=1
                    colonna_t = c
                    # Cambio colonna sotto
                    while riga_t < n:
                        if s[riga_t][colonna_t] != "x":
                            s[riga_t][c] = "x"
                            spazi_rimasti -= 1
                        riga_t +=1
                    riga_t = r
                    # Cambio colonna sopra
                    while riga_t >= 0:
                        if s[riga_t][colonna_t] != "x":
                            s[riga_t][c] = "x"
                            spazi_rimasti -= 1
                        riga_t -=1
                    riga_t = r
                    colonna_t = c
                    # Cambio diagonali sotto
                    while riga_t < n and colonna_t < n:
                        if s[riga_t][colonna_t] != "x":
                            s[riga_t][colonna_t] = "x"
                            spazi_rimasti -= 1
                        riga_t +=1
                        colonna_t += 1
                    riga_t = r
                    colonna_t = c
                    while riga_t < n and colonna_t >= 0:
                        if s[riga_t][colonna_t] != "x":
                            s[riga_t][colonna_t] = "x"
                            spazi_rimasti -= 1
                        riga_t +=1
                        colonna_t -= 1
                    riga_t = r
                    colonna_t = c
                    # Cambio diagonali sopra
                    while riga_t >= 0 and colonna_t >= 0:
                        if s[riga_t][colonna_t] != "x":
                            s[riga_t][colonna_t] = "x"
                            spazi_rimasti -= 1
                        riga_t -=1
                        colonna_t -= 1
                    riga_t = r
                    colonna_t = c
                    while riga_t >= 0 and colonna_t < n:
                        if s[riga_t][colonna_t] != "x":
                            s[riga_t][colonna_t] = "x"
                            spazi_rimasti -= 1
                        riga_t -=1
                        colonna_t += 1
                    # Piazzo la regina
                    s[r][c] = "o"
                    piazzate += 1
                    #endregion
                    
                    # Stampo la scacchiera
                    for i in range(n):
                        print(s[i])
                        if i == n-1:
                            print("\n")

                    if piazzate == n:
                        return 1
                
                if spazi_rimasti < n-piazzate:
                    # Backtrack all'ultimo stato sicuro
                    return 0
                elif piazzate == n:
                    return 1
            c = 0
        if piazzate == n:
            return 1
        else:
            return 0

    combinazioni = provaCombinazione(combinazioni,scacchiera)

    return combinazioni

if __name__ == "__main__":
    numero = int(input())
    output = trovaPosizioni(numero)
    print("SOLUZIONI TROVATE:",output)
