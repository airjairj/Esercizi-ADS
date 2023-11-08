'''
SBAGLIATO, NON HO CORRETTO NIENTE PERCHé STAVO ARRABBIATO CHE ERA FACILE MA HO PERSO TEMPO PER LE PARENTESI IN RIGA 14
'''
def impera(vett,sin,des):
    if len(vett[sin:des]) == 1:
        return vett[0]
    else:
        return 0
    

def divide(vett,sin,des,output):

    if sin < des:
        centro = (sin+des) // 2

        output+=divide(vett,sin,centro,output)
        output+=divide(vett,centro+1,des,output)

        output+= impera(vett,sin,des)

    return output

#region input
num_test = 1 #int(input("Numero test: "))

while num_test > 0:
    lunghezza_vettore = 6 #int(input("Lunghezza vettore: "))
    vettore = [3,6,12,15,18,21]
    output = -1
    somma_presunta = (lunghezza_vettore+1)*(0.5)*(vettore[0]+vettore[len(vettore)-1])

    output = divide(vettore,0,len(vettore)-1, 0)
    finale = somma_presunta-output    
    
    print(finale)

    num_test -= 1
#endregion output