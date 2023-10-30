def trovaSottoArray(lista):
        """
        Data una lista in ingresso, ritorna la sottolista con la somma maggiore
        """

        temp = 0                        # Inizializzo il valore temporaneo che uso come buffer a 0
        tot = float('-inf')             # Inizializzo il valore che uso come totale a -infinito (0 non andrebbe bene per liste negative)
 
        for val in lista:               # Scorro i valori
            temp += val                 # Sommo il valore al temp
            
            if temp > tot:              # Se il temp è maggiore del totale, ho un nuovo totale
                tot = temp
            
            if temp < 0:                # Se il temp è diventato < 0 dopo l'ultima somma, resetto temp
                temp = 0                # dato che il maggiore è stato gia salvato, e se è diventato negativo non ci guadagno
                                        # a continuare questa sottolista, conviene ricominciare
        return tot


if __name__ == "__main__":
    
    lista = [-1,-3,4,6,-8,8,6,7,-100,5]
    output = trovaSottoArray(lista)
    print(output)
