class Output:
    def numeroSoluzioni(self, n):
        # Creo la scacchiera
        scacchiera = [['.' for i in range(n)] for j in range(n)]
        # Imposto il numero di regine da piazzare ad n
        self.regine = n
        # Inizializzo le combinazioni trovate a 0
        self.combinazioni = 0
        # Invoco la prova delle posizioni
        self.provaPosizione(0, scacchiera)
        # Ritorno le combinazioni trovate (modificate nella funzione "provaPosizione")
        return self.combinazioni
    
    def provaPosizione(self, i, scacchiera, regine=None, piazzate=0):
        """
        Dati in input:
        i (la riga corrente)
        scacchiera (la configurazione corrente della scacchiera)
        regine (una lista delle posizioni delle regine precedentemente piazzate, inizializzata a None)
        piazzate (il numero di regine già piazzate, inizializzato a 0)
        esegue un ciclo su tutte le colonne di una riga e cerca di piazzare una regina 
        """

        if piazzate == self.regine: # self.regine è n per intenderci
            self.combinazioni += 1  # Se quindi ho piazzato n regine ho una combinazione valida
            return
        
        if i>= self.regine:         # Se i >= self.regine (che è sempre n) significa che non ho piazzato nessuna regina sulla riga, quindi non cè soluzione
            return                  # o qualcosa è andato storto perchè è finita la scacchiera
        
        if not regine:              # Inizializzo le posizioni se non l'ho gia fatto
            regine = []

        for j in range(self.regine):                                                     # j scorre da 0 a self.regine (vale sempre n) quindi scorre le colonne in una riga
            if self.controlloPosizione(regine + [[i,j]], piazzate, scacchiera):          # Ora se il controllo posizione in [i][j] mi da true -> piazzo una regina in [i][j]
                scacchiera[i][j] = 'o'
                self.provaPosizione(i + 1, scacchiera, regine + [[i,j]], piazzate + 1)   # Continuo a posizionare quindi dalla riga successiva "(i+1)", sulla stessa scacchiera, ora con
                scacchiera[i][j] = '.'                                                   # ora con delle regine piazzate e le loro posizioni salvate in "regine"
    
    def controlloPosizione(self, regine, piazzate, scacchiera):
        """
        Dati in input:
        regine (una lista delle posizioni delle regine precedentemente piazzate)
        piazzate (il numero di regine già piazzate)
        scacchiera (la configurazione corrente della scacchiera)
        controlla se possono convivere le regine che vorrei piazzare
        """

        if piazzate < 1:            # Se non ho piazzato manco una regina, ovviamente ritorno true, non ho controlli da fare
            return True
        for regina in regine:                               # Se ho invece delle regine piazzate (le loro posizioni sono sempre in "regine")
            r_x = regina[0]
            r_y = regina[1]                                 # prendo le coordinate di ognuna nel ciclo e le salvo in "r_x" ed "r_y"
            
            for i in range(self.regine):                    # Ciclo da 0 a n
                if scacchiera[i][r_y] == 'o' and i!=r_x:    # Controllo la riga
                    return False                            # se trovo un "o", cè una regina, ritorno false
                if scacchiera[r_x][i] == 'o' and i!=r_y:    # Controllo la colonna
                    return False                            # se trovo un "o", cè una regina, ritorno false
                
            #region Diagonale destra bassa
            while r_x+1 < self.regine and r_y+1 < self.regine:     # Controllo la diagonale destra bassa
                r_x += 1                                           # Vado a destra
                r_y += 1                                           # Vado in basso
                if scacchiera[r_x][r_y] == 'o':                    # se trovo un "o", cè una regina, ritorno false
                    return False
            #endregion

            #region Diagonale sinistra bassa
            r_x = regina[0]                             # Reset, dato che l'ultimo controllo mi ha sfasato
            r_y = regina[1]
            while r_x-1 >= 0 and r_y+1 < self.regine:   # Controllo la diagonale sinistra bassa
                r_x -= 1                                # Vado a sinistra
                r_y += 1                                # Vado in basso
                if scacchiera[r_x][r_y] == 'o':         # se trovo un "o", cè una regina, ritorno false
                    return False
            #endregion

            #region Diagonale destra alta
            r_x = regina[0]                                 # Reset, dato che l'ultimo controllo mi ha sfasato
            r_y = regina[1]
            while r_x+1 < self.regine and r_y-1 >= 0:       # Controllo la diagonale destra alta
                r_x += 1                                    # Vado a destra
                r_y -= 1                                    # Vado in alto
                if scacchiera[r_x][r_y] == 'o':             # se trovo un "o", cè una regina, ritorno false
                    return False
            #endregion  

            #region Diagonale sinistra alta
            r_x = regina[0]                                 # Reset, dato che l'ultimo controllo mi ha sfasato
            r_y = regina[1]
            while r_x-1>=0 and r_y-1>=0:                    # Controllo la diagonale sinistra alta
                r_x -= 1                                    # Vado a sinistra
                r_y -= 1                                    # Vado in alto
                if scacchiera[r_x][r_y] == 'o':             # se trovo un "o", cè una regina, ritorno false
                    return False
            #endregion

        return True     # Se non ho trovato nulla, ovviamente ritorno true     
            
if __name__ == "__main__":
    numero = int(input())
    output = Output()
    print("SOLUZIONI TROVATE:", output.numeroSoluzioni(numero))


# La complessità è O(N!) dato che esploriamo tutte le possibili combinazioni, date dalle N righe, con N colonne.
# Dati N il numero di regine da piazzare ed n il numero di regine mancanti:

# La funzione La funzione "controllo posizione" controlla le regine già posizionate, ha un tempo di esecuzione nel caso peggiore di O(N-n).
# Poiché O(N-n)<O(N), possiamo scrivere O(N-n) = O(N). 
# Dato che la funzione "prova posizione" itera n volte e per ogni iterazione chiama la funzione "controllo posizione", la complessità temporale totale diverrebbe O(N^2).
# Però "prova poszione" è ricorsiva, quindi: 

# La chiamata ricorsiva di T(n-1) verrà eseguita n volte perché verrà eseguita solo per le celle sicure. 
# Dato che abbiamo iniziato riempiendo le righe, non ci saranno più di n (numero di regine rimaste) celle sicure nella riga in ogni caso. 
# Ciò si traduce in nT(n-1) volte. 
# 
# Sommando i risultati otteniamo T(n) = nT(n-1) + O(N^2) mediante l'albero di ricorsione. 

# Sostituisco T(n−1) with O(N^2)+(n−1)T(n−2):

# T(n) = O(N^2)+ n∗(O(N^2)+(n−1)T(n−2))
# T(n) = O(N^2)+ nO(N^2)+n(n−1)T(n−2)

# Sostituendo T(n−2) with O(N^2)+(n−2)T(n−3):

# T(n) = O(N^2)+ nO(N^2)+n(n−1)(O(N^2)+(n−2)T(n−3)) = O(N^2)+nO(N^2)+ n(n−1)O(N^2)+n(n−1)(n−2)T(n−3)

# Si vede quindi che proseguendo:

# T(n) = O(N^2)(1+n+n(n−1)+n(n−2)+...) + n∗(n−1)∗(n−2)∗(n−3)∗(n−4)∗....∗T(0)
# T(n) = O(N^2)(O((n−2)!)) + n∗(n−1)∗(n−2)∗(n−3)∗....∗T(0)T(n) = O(N^2)(O((n−2)!))+n∗(n−1)∗(n−2)∗(n−3)∗....∗T(0) = O(N^2)(O((n−2)!))+O(n!) = O(n!) dato che è di ordine superiore 
