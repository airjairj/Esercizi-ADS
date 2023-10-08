import random

class Nodo:
    def __init__(self, c_val):
        self.prio = random.randint(1, 1000)
        self.chiave = c_val
        self.sin = None
        self.des = None

class AlberoBinario:
    def __init__(self):
        self.radice = None

    # Parte albero binario
    def primo_inserimento(self, c_val):
        if self.radice is None:
            self.radice = Nodo(c_val)
        else:
            self.inserimento(c_val, self.radice)

    def inserimento(self, c_val, rad):
        if c_val < rad.chiave:
            if rad.sin is None:
                rad.sin = Nodo(c_val)
            else:
                self.inserimento(c_val, rad.sin)
        else:
            if rad.des is None:
                rad.des = Nodo(c_val)
            else:
                self.inserimento(c_val, rad.des)

        # Dopo l'inserimento, controlla ed esegue rotazioni se serve
        rad = self.rotazioni(rad)

    # Parte heap
    def rotazioni(self, nodo):
        if nodo.sin and nodo.sin.prio < nodo.prio:
            # Rotazione a destra
            self.rotazione_destra(nodo)

        if nodo.des and nodo.des.prio < nodo.prio:
            # Rotazione a sinistra
            self.rotazione_sinistra(nodo)

    def rotazione_destra(self, nodo):
        figlio_sin = nodo.sin
        nodo.sin = figlio_sin.des
        figlio_sin.des = nodo
        return figlio_sin

    def rotazione_sinistra(self, nodo):
        figlio_des = nodo.des
        nodo.des = figlio_des.sin
        figlio_des.sin = nodo
        return figlio_des

    # Parte stampa
    def stampa_albero(self, radice=None, livello=0, prefisso="Radice: "):
        if radice is not None:
            print(" " * (livello * 4) + prefisso + str(radice.chiave) + f" (Prio: {radice.prio})")
            if radice.sin is not None or radice.des is not None:
                self.stampa_albero(radice.sin, livello + 1, "Sin: ")
                self.stampa_albero(radice.des, livello + 1, "Des: ")

if __name__ == "__main__":
    albero = AlberoBinario()
    num_nodi = int(input("Inserisci il numero di nodi dell'albero:"))

    for i in range(num_nodi):
        nodo = int(input(f"Inserisci il nodo ({i+1}/{num_nodi}):"))
        albero.primo_inserimento(nodo)

    print("\nAlbero:")
    albero.stampa_albero(radice=albero.radice)