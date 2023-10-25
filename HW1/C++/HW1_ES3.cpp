#include <iostream>
#include <stdlib.h>
#include <time.h>  

class Nodo {

public:

    Nodo(int c_val, int p_val, Nodo* genitore) : chiave(c_val), priorita(p_val), sin(NULL), des(NULL), padre(genitore) {}

    int chiave;
    int priorita;
    Nodo* sin;
    Nodo* des;
    Nodo* padre;
};

 

class AlberoBinario {

public:

    AlberoBinario() : radice(NULL) {}

    void primo_inserimento(int c_val, int p_val) {

        if (radice == NULL) {

            radice = new Nodo(c_val, p_val, NULL);

        }

        else {

            inserimento(c_val, radice, p_val);

        }

    }

 

    void inserimento(int c_val, Nodo* rad, int p_val) {

        if (c_val < rad->chiave) {

            if (rad->sin == NULL) {

                rad->sin = new Nodo(c_val, p_val, rad);

            }

            else {

                inserimento(c_val, rad->sin, p_val);

            }

        }

        else {

            if (rad->des == NULL) {

                rad->des = new Nodo(c_val, p_val, rad);

            }

            else {

                inserimento(c_val, rad->des, p_val);

            }

        }

 

        scambi(rad);

    }

 

    Nodo* scambi(Nodo* nodo) {

        while (nodo->sin && nodo->sin->priorita < nodo->priorita) {

            nodo = scambio_sinistra(nodo);

        }

 

        while (nodo->des && nodo->des->priorita < nodo->priorita) {

            nodo = scambio_destra(nodo);

        }

 

        return nodo;

    }

 

    Nodo* scambio_sinistra(Nodo* nodo) {

        Nodo* figlio_da_ruotare = nodo->sin;

        Nodo* nodo_originale = nodo;

        Nodo* padre_originale = nodo->padre;

 

        nodo->sin = figlio_da_ruotare->des;

        if (nodo->sin) {

            nodo->sin->padre = nodo;

        }

 

        figlio_da_ruotare->des = nodo_originale;

        figlio_da_ruotare->des->padre = figlio_da_ruotare;

        figlio_da_ruotare->padre = padre_originale;

 

        if (padre_originale) {

            if (padre_originale->sin == nodo_originale) {

                padre_originale->sin = figlio_da_ruotare;

            }

            else {

                padre_originale->des = figlio_da_ruotare;

            }

        }

        else {

            radice = figlio_da_ruotare;

        }

 

        return figlio_da_ruotare;

    }

 

    Nodo* scambio_destra(Nodo* nodo) {

        Nodo* figlio_da_ruotare = nodo->des;

        Nodo* nodo_originale = nodo;

        Nodo* padre_originale = nodo->padre;

 

        nodo->des = figlio_da_ruotare->sin;

        if (nodo->des) {

            nodo->des->padre = nodo;

        }

 

        figlio_da_ruotare->sin = nodo_originale;

        figlio_da_ruotare->sin->padre = figlio_da_ruotare;

        figlio_da_ruotare->padre = padre_originale;

 

        if (padre_originale) {

            if (padre_originale->sin == nodo_originale) {

                padre_originale->sin = figlio_da_ruotare;

            }

            else {

                padre_originale->des = figlio_da_ruotare;

            }

        }

        else {

            radice = figlio_da_ruotare;

        }

 

        return figlio_da_ruotare;

    }

 

    void stampa_albero(Nodo* radice = NULL, int livello = 0, const std::string& prefisso = "Radice: ") {

        if (radice == NULL) {

            radice = this->radice;

        }

 

        if (radice != NULL) {

            std::cout << std::string(livello * 4, ' ') << prefisso << radice->chiave << " (Pri: " << radice->priorita << ")\n";

            if (radice->sin != NULL || radice->des != NULL) {

                if (radice->sin != NULL) {

                    stampa_albero(radice->sin, livello + 1, "Sin: ");

                }

                if (radice->des != NULL) {

                    stampa_albero(radice->des, livello + 1, "Des: ");

                }

            }

        }

    }

 

private:

    Nodo* radice;

};

 

int main() {

    AlberoBinario albero;

 

    int num_nodi;

    std::cout << "Inserisci il numero di nodi dell'albero: ";

    std::cin >> num_nodi;

    srand(time(NULL));

    for (int i = 0; i < num_nodi; i++) {

        int valore, prio;

        std::cout << "Inserisci il nodo (" << i + 1 << "/" << num_nodi << "): ";

        std::cin >> valore;

        prio = rand() %100;

        albero.primo_inserimento(valore, prio);

    }

 

    std::cout << "\nAlbero:\n";

    albero.stampa_albero();

 

    return 0;

}

//------------------------------------------------------------------------------------------
// La complessità è : O(n*log(n))
// L'inserimento ha complessità O(log(n)) dato che il caso peggiore 
// prevede di inserire alle foglie dell'albero, scorrendo l'albero in altezza.
// La parte degli scambi ha invece complessità O(n*log(n)) dato che il caso peggiore 
// prevede di scambiare l'ultimo elemento aggiunto con la radice, risalendo intero l'altezza dell'albero.
// Se supponiamo di farlo per tutti gli n elementi abbiamo O(n*log(n))
// La complessità totale è quindi O(n*log(n))

// Sample Input
// Inserisci il numero di nodi dell'albero: 5
// Inserisci il nodo (1/5): 7
// Inserisci il nodo (2/5): 5
// Inserisci il nodo (3/5): 3
// Inserisci il nodo (4/5): 9
// Inserisci il nodo (5/5): 1
//
// Sample Output
// Albero:
// Radice: 9 (Pri: 31)
//     Sin: 5 (Pri: 39)
//         Sin: 3 (Pri: 93)
//             Sin: 1 (Pri: 93)
//         Des: 7 (Pri: 69)

// Sample Input
// Inserisci il numero di nodi dell'albero: 10
// Inserisci il nodo (1/10): 6
// Inserisci il nodo (2/10): 7
// Inserisci il nodo (3/10): 9
// Inserisci il nodo (4/10): 99
// Inserisci il nodo (5/10): 8
// Inserisci il nodo (6/10): 2
// Inserisci il nodo (7/10): 3
// Inserisci il nodo (8/10): 11
// Inserisci il nodo (9/10): 1
// Inserisci il nodo (10/10): 5
// Sample Outpuy
// Albero:
// Radice: 99 (Pri: 5)
//     Sin: 2 (Pri: 16)
//         Sin: 1 (Pri: 46)
//         Des: 11 (Pri: 29)
//            Sin: 8 (Pri: 44)
//                Sin: 3 (Pri: 55)
//                    Des: 6 (Pri: 67)
//                        Sin: 5 (Pri: 74)
//                        Des: 7 (Pri: 79)
//                Des: 9 (Pri: 65)

// Sample Input
// Inserisci il numero di nodi dell'albero: 4
// Inserisci il nodo (1/4): 11
// Inserisci il nodo (2/4): 22
// Inserisci il nodo (3/4): 44
// Inserisci il nodo (4/4): 66
// Sample Output
// Albero:
// Radice: 44 (Pri: 8)
//    Sin: 22 (Pri: 32)
//        Sin: 11 (Pri: 34)
//    Des: 66 (Pri: 81)