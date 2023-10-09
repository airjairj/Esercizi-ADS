import random

class Nodo:
    def __init__(self, c_val, p_val, genitore):
        self.priorita = p_val
        self.chiave = c_val
        self.sin = None
        self.des = None
        self.padre = genitore

class AlberoBinario:
    def __init__(self):
        self.radice = None

    #region Parte albero binario
    def primo_inserimento(self, c_val, p_val):
        if self.radice is None:
            self.radice = Nodo(c_val,p_val, None)
        else:
            self.inserimento(c_val, self.radice, p_val)

    def inserimento(self, c_val, rad, p_val):
        if c_val < rad.chiave:
            if rad.sin is None:
                rad.sin = Nodo(c_val,p_val, rad)
            else:
                self.inserimento(c_val, rad.sin, p_val)
        else:
            if rad.des is None:
                rad.des = Nodo(c_val,p_val, rad)
            else:
                self.inserimento(c_val, rad.des, p_val)

        # Dopo l'inserimento, controlla ed esegue scambi se serve
        rad = self.scambi(rad)
    #endregion

    #region Parte heap
    def scambi(self, nodo):
        if nodo.sin and nodo.sin.priorita < nodo.priorita:
            # Rotazione a destra
            self.scambio_sinistra(nodo) #SINISTRA

        if nodo.des and nodo.des.priorita < nodo.priorita:
            # Rotazione a sinistra
            self.scambio_destra(nodo) #DESTRA

    def scambio_sinistra(self, nodo):
        # Salvo i cretini da scambiare
        figlio_da_ruotare = nodo.sin
        figlio_altro = nodo.des
        nodo_originale = nodo
        # Pulisco le var
        nodo.des = None
        nodo.sin = None
        # Riassegno
        figlio_da_ruotare.des = nodo_originale
        figlio_da_ruotare.des.des = figlio_altro
        nodo.padre.sin = figlio_da_ruotare
        
        return nodo

    def scambio_destra(self, nodo):
        # Salvo i cretini da scambiare
        figlio_da_ruotare = nodo.des
        figlio_altro = nodo.sin
        nodo_originale = nodo
        # Pulisco le var
        nodo.des = None
        nodo.sin = None
        # Riassegno
        figlio_da_ruotare.sin = nodo_originale
        figlio_da_ruotare.sin.sin = figlio_altro
        nodo.padre.des = figlio_da_ruotare
        #nodo = figlio_da_ruotare

        return nodo
    #endregion

    #region Parte stampa
    def stampa_albero(self, radice=None, livello=0, prefisso="Radice: "):
        if radice is None:
            radice = self.radice

        if radice is not None:
            print(" " * (livello * 4) + prefisso + str(radice.chiave) + f" (Pri: {radice.priorita})")
            if radice.sin is not None or radice.des is not None:
                if radice.sin is not None:
                    self.stampa_albero(radice.sin, livello + 1, "Sin: ")
                if radice.des is not None:
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