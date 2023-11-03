def calcola_posizione(profondita, num_palla):
    position = 1

    for i in range(profondita - 1, 0, -1):
        sinistra = num_palla % 2 == 1
        num_palla = (num_palla + 1) // 2

        if sinistra:
            position = 2 * position
        else:
            position = 2 * position + 1

    return position

if __name__ == "__main__":
    T = int(input("Inserisci il numero di casi di test: "))
    for k in range(T):
        profondita, num_palla = map(int, input().split())
        output = calcola_posizione(profondita, num_palla)
        print(output)