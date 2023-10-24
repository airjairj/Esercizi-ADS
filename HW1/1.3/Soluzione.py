import random

class Nodo:
    """
    La classe dei nodi dell'albero
    """
    # Costruttore
    def __init__(self, c_val, p_val, genitore):
        self.priorita = p_val
        self.chiave = c_val
        self.sin = None
        self.des = None
        self.padre = genitore

class AlberoBinario:
    """
    La classe dell'albero
    """

    #region Costruttore
    def __init__(self):
        self.radice = None
    #endregion

    #region Albero binario
    def primo_inserimento(self, c_val, p_val):
        """
        Data una chiave ed una priorità inserisce il nodo nell'albero, se è il primo sarà la radice
        """

        # Se la radice non esiste, il nodo diventa radice, altrimenti il nodo viene inserito normalmente
        if self.radice is None:
            self.radice = Nodo(c_val, p_val, None)
        else:
            self.inserimento(c_val, self.radice, p_val)

    def inserimento(self, c_val, rad, p_val):
        """
        Data una chiave, una priorità ed un genitore, inserisce il nodo nell'albero
        """

        # Se la chiave è minore di quella del padre, va a sinistra, se è maggiore a destra, 
        # se un nodo figlio è gia presente nella direzione presa, si fa inserimento sul figlio
        if c_val < rad.chiave:
            if rad.sin is None:
                rad.sin = Nodo(c_val, p_val, rad)
            else:
                self.inserimento(c_val, rad.sin, p_val)
        else:
            if rad.des is None:
                rad.des = Nodo(c_val, p_val, rad)
            else:
                self.inserimento(c_val, rad.des, p_val)

        # Infine controllo per eventuali scambi
        return self.scambi(rad)
    #endregion

    #region Heap
    def scambi(self, nodo):
        """
        Dato un nodo controlla se è necessario scambiarlo con i figli in base alla priorità (più alta = figlio)
        """
        # While perchè uno scambio potrebbe portare ad altri
        while nodo.sin and nodo.sin.priorita < nodo.priorita:
            nodo = self.scambio_sinistra(nodo)

        while nodo.des and nodo.des.priorita < nodo.priorita:
            nodo = self.scambio_destra(nodo)

        # Ritorna il nodo aggiornato dopo l'eventuale scambio
        return nodo

    def scambio_sinistra(self, nodo):
        """
        Dato un nodo, si scambiano il nodo ed il suo figlio sinistro, il nodo diventa figlio destro
        """
        
        # Salvo i nodi importanti in variabili
        figlio_da_ruotare = nodo.sin
        nodo_originale = nodo
        padre_originale = nodo.padre

        # Comincio gli scambi, facendo attenzione a padri e figli
        nodo.sin = figlio_da_ruotare.des
        if nodo.sin:
            nodo.sin.padre = nodo

        # Scambi
        figlio_da_ruotare.des = nodo_originale
        figlio_da_ruotare.des.padre = figlio_da_ruotare
        figlio_da_ruotare.padre = padre_originale

        # Controllo tramite i padri, anche in caso non ci sia (radice)
        if padre_originale:
            if padre_originale.sin == nodo_originale:
                padre_originale.sin = figlio_da_ruotare
            else:
                padre_originale.des = figlio_da_ruotare
        else:
            self.radice = figlio_da_ruotare

        # Ritorno il figlio prescelto
        return figlio_da_ruotare

    def scambio_destra(self, nodo):
        """
        Dato un nodo, si scambiano il nodo ed il suo figlio destro, il nodo diventa figlio sinistro
        """
    
        # Salvo i nodi importanti in variabili
        figlio_da_ruotare = nodo.des
        nodo_originale = nodo
        padre_originale = nodo.padre
        
        # Comincio gli scambi, facendo attenzione a padri e figli
        nodo.des = figlio_da_ruotare.sin
        if nodo.des:
            nodo.des.padre = nodo

        # Scambi
        figlio_da_ruotare.sin = nodo_originale
        figlio_da_ruotare.sin.padre = figlio_da_ruotare
        figlio_da_ruotare.padre = padre_originale

        # Controllo tramite i padri, anche in caso non ci sia (radice)
        if padre_originale:
            if padre_originale.sin == nodo_originale:
                padre_originale.sin = figlio_da_ruotare
            else:
                padre_originale.des = figlio_da_ruotare
        else:
            self.radice = figlio_da_ruotare

        # Ritorno il figlio prescelto
        return figlio_da_ruotare
    #endregion

    #region Stampa
    def stampa_albero(self, radice=None, livello=0, prefisso="Radice: "):
        """
        Stampa i rami dell'albero indentando ad ogni ricorsione in modo tale da avere uno schemino carino
        """

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
    # Istanzio l'albero binario
    albero = AlberoBinario()
    
    # Faccio inserire i nodi a piacere
    num_nodi = int(input("Inserisci il numero di nodi dell'albero:"))

    # Inserimento
    for i in range(num_nodi):
        valore = int(input(f"Inserisci il nodo ({i+1}/{num_nodi}):"))
        prio = random.randint(0,100)
        
        # Chiamo la funzione di inserimento (in realtà del primo inserimento, è gestito tutto qua)
        albero.primo_inserimento(valore, prio)

    # Stampa dell'albero con la funzione stampa_albero
    print("\nAlbero:")
    albero.stampa_albero()

#------------------------------------------------------------------------------------------
# La complessità è : O(n*log(n))
# L'inserimento ha complessità O(log(n)) dato che il caso peggiore 
# prevede di inserire alle foglie dell'albero, scorrendo l'albero in altezza.
# La parte degli scambi ha invece complessità O(n*log(n)) dato che il caso peggiore 
# prevede di scambiare l'ultimo elemento aggiunto con la radice, risalendo intero l'altezza dell'albero.
# Se supponiamo di farlo per tutti gli n elementi abbiamo O(n*log(n))
# La complessità totale è quindi O(n*log(n))