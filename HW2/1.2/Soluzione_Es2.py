def trovaSottoArray(lista):
        temp = 0
        tot = float('-inf')
 
        for val in lista:
            temp += val
            
            if temp > tot:
                tot = temp
            
            if temp < 0:
                temp = 0

        return tot


if __name__ == "__main__":
    
    lista = [-1,-3,4,6,-8,8,6,7,-100,5]
    output = trovaSottoArray(lista)
    print(output)
