def Soluzione(pista, dim_riga,dim_col, riga, col, percorso,migliore):

    if (col < dim_col-1 and col >= 0) and pista[riga][col + 1] < pista[riga][col]:                         # Vado a destra      
        percorso.append([riga,col])
        result = Soluzione(pista, dim_riga,dim_col,riga,col+1,percorso,migliore+1)
        if result > migliore:                                          
            return migliore                                              
        percorso.pop()   

    if (col < dim_col-1 and col >= 0) and pista[riga][col - 1] < pista[riga][col]:                         # Vado a sinistra      
        percorso.append([riga,col])
        result = Soluzione(pista, dim_riga,dim_col,riga,col-1,percorso,migliore+1)
        if result > migliore:                                          
            return migliore                                              
        percorso.pop()   

    if (riga < dim_riga-1 and riga >= 0) and pista[riga+1][col] < pista[riga][col]:                         # Vado a sotto      
        percorso.append([riga,col])
        result = Soluzione(pista, dim_riga,dim_col,riga+1,col,percorso,migliore+1)
        if result > migliore:                                          
            return migliore                                              
        percorso.pop()   

    if (riga < dim_riga-1 and riga >= 0) and pista[riga-1][col] < pista[riga][col]:                         # Vado a sopra      
        percorso.append([riga,col])
        result = Soluzione(pista, dim_riga,dim_col,riga-1,col,percorso,migliore+1)
        if result > migliore:                                          
            return migliore                                              
        percorso.pop()                
    return migliore

with open("C:\\Users\\GAMING EDGE\\Desktop\\UNI\\1o ANNO\\1o SEMESTRE\\Algoritmi e data structures\\ADS\\Esercitazioni\\Backtracking\\TestCase2.txt", "r") as file:
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

        migliore_output = []
        for i in range(righe):
            for j in range(col):
                path = []
                output = Soluzione(pista, dim_mat[0],dim_mat[1],i,j,path,0)


        print(output)

        num_test -= 1

