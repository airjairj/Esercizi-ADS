'''
Complessità: O(num_righe * num_colonne * lunghezza_parola)
'''

def backtrack(matrice,parola,riga,colonna,ris_attuale,n_righe,n_colonne,lettera):
    
    if len(ris_attuale) == len(parola):
        print(ris_attuale)
        return ris_attuale
    
    if(matrice[riga][colonna] == parola[lettera]):
        ris_attuale.append([riga,colonna])
        if len(ris_attuale) == len(parola):
            print(ris_attuale)
            return ris_attuale
    #region controllo il posto di dopo    
        if colonna+1 < n_colonne and lettera+1<len(parola) and matrice[riga][colonna+1] == parola[lettera+1]: # Vado a destra
            backtrack(matrice,parola,riga,colonna+1,ris_attuale,n_righe,lettera+1)

        if colonna-1 >= 0 and lettera+1<len(parola) and matrice[riga][colonna-1] == parola[lettera+1]:        # Vado a sinistra
            backtrack(matrice,parola,riga,colonna-1,ris_attuale,n_righe,n_colonne,lettera+1)

        if riga-1 >= 0 and lettera+1<len(parola) and matrice[riga-1][colonna] == parola[lettera+1]:           # Vado sopra
            backtrack(matrice,parola,riga-1,colonna,ris_attuale,n_righe,n_colonne,lettera+1)

        if riga+1 < n_righe and lettera+1<len(parola) and matrice[riga+1][colonna] == parola[lettera+1]:      # Vado sotto
            backtrack(matrice,parola,riga+1,colonna,ris_attuale,n_righe,n_colonne,lettera+1)

        if riga-1 >= 0 and colonna-1 >= 0 and lettera+1<len(parola) and matrice[riga-1][colonna-1] == parola[lettera+1]:        # Vado a sinistra sopra
            backtrack(matrice,parola,riga-1,colonna-1,ris_attuale,n_righe,n_colonne,lettera+1)

        if riga+1 < n_righe and colonna-1 >= 0 and lettera+1<len(parola) and matrice[riga+1][colonna-1] == parola[lettera+1]:        # Vado a sinistra sotto
            backtrack(matrice,parola,riga+1,colonna-1,ris_attuale,n_righe,n_colonne,lettera+1)

        if riga-1 >= 0 and colonna+1 < n_colonne and lettera+1<len(parola) and matrice[riga-1][colonna+1] == parola[lettera+1]:        # Vado a destra sopra
            backtrack(matrice,parola,riga-1,colonna+1,ris_attuale,n_righe,n_colonne,lettera+1)

        if riga+1 < n_righe and colonna+1 < n_colonne and lettera+1<len(parola) and matrice[riga+1][colonna+1] == parola[lettera+1]:        # Vado a destra sotto
            backtrack(matrice,parola,riga+1,colonna+1,ris_attuale,n_righe,n_colonne,lettera+1)
    #endregion
        ris_attuale.pop()

    return

num_test =  int(input("Numero"))

while num_test > 0:
    parola_da_cercare = input("Parola")
    righe = 5
    colonne = 5

    matrice = [["s","r","z","h","d"],["f","o","a","g","e"],["x","d","n","l","o"],["o","r","a","t","n"],["z","p","o","i","n"]]
    for i in range(righe):
        print(matrice[i])
    output = []
    for i in range(righe):
        for j in range(colonne):
            backtrack(matrice,parola_da_cercare,i,j,output,righe,colonne,0)
            if len(output) == len(parola_da_cercare):
                print(output) 
                break
    print("END")
    num_test -= 1

#