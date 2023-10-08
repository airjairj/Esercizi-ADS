import random

class Nodo:
    def __init__(self, c_val, p_val):
        self.priorita = p_val
        self.chiave = c_val
        self.sin = None
        self.des = None

class AlberoBinario:
    def __init__(self):
        self.radice = None

    #region Parte albero binario
    def primo_inserimento(self, c_val, p_val):
        if self.radice is None:
            self.radice = Nodo(c_val,p_val)
        else:
            self.inserimento(c_val, self.radice, p_val)

    def inserimento(self, c_val, rad, p_val):
        if c_val < rad.chiave:
            if rad.sin is None:
                rad.sin = Nodo(c_val,p_val)
            else:
                self.inserimento(c_val, rad.sin, p_val)
        else:
            if rad.des is None:
                rad.des = Nodo(c_val,p_val)
            else:
                self.inserimento(c_val, rad.des, p_val)

        # Dopo l'inserimento, controlla ed esegue rotazioni se serve
        rad = self.rotazioni(rad)
    #endregion

    #region Parte heap
    def rotazioni(self, nodo):
        if nodo.sin and nodo.sin.priorita < nodo.priorita:
            # Rotazione a destra
            self.rotazione_destra(nodo)

        if nodo.des and nodo.des.priorita < nodo.priorita:
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
    #endregion

    #region Parte stampa
    def stampa_albero(self, radice=None, livello=0, prefisso="Radice: "):
        if radice is not None:
            print(" " * (livello * 4) + prefisso + str(radice.chiave) + f" (Prio: {radice.priorita})")
            if radice.sin is not None or radice.des is not None:
                self.stampa_albero(radice.sin, livello + 1, "Sin: ")
                self.stampa_albero(radice.des, livello + 1, "Des: ")
    #endregion

if __name__ == "__main__":
    albero = AlberoBinario()
    num_nodi = int(input("Inserisci il numero di nodi dell'albero:"))

    for i in range(num_nodi):
        valore = int(input(f"Inserisci il nodo ({i+1}/{num_nodi}):"))
        prio = int(input(f"Inserisci la priorita del nodo ({i+1}/{num_nodi}):"))
        albero.primo_inserimento(valore,prio)

    print("\nAlbero:")
    albero.stampa_albero(radice=albero.radice)