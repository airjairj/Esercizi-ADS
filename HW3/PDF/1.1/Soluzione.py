def soluzione(numero,valori):
    return 0

num_test = int(input("NUMERO DI CASI DI TEST: "))

while num_test > 0:
    
    num_monete = int(input("NUMERO DI MONETE: ")) # 1 / 50
    val_monete = int(input("VALORE DI MONETE: ")) # 1 / 1000
    
    ris = soluzione(num_monete,val_monete)
    print("OUTPUT:", ris)

    num_test -= 1