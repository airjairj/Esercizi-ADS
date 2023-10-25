#include <iostream>
#include <vector>
using namespace std;


string cercaSottostringa(string strinLeft, string strinRight) {
    string prefisso = "";
    int lunghezzaMin = 0; //la chiamo m, ossia la minima lunghezza della stringa (per il calcolo della complessità)
    int lunghezza1 = strinLeft.size();
    int lunghezza2 = strinRight.size();

 

    if (lunghezza1 < lunghezza2) {
        lunghezzaMin = lunghezza1;
    } else {
        lunghezzaMin = lunghezza2;
    }

 

    for (int i = 0; i < lunghezzaMin; i++) {
        if (strinLeft[i] == strinRight[i]) {
            prefisso += strinRight[i];
        } else {
            break;
        }
    }

 

    return prefisso;
}

 

string ordina(vector<string>& stringhe, int left, int right) {
	
	int mid = 0;
	string prefissoLeft = "";
	string prefissoRight = "";
	string prefisso = "";
	
	if (left == right) {
        return stringhe[left];
    }

	mid = (left + right)/2; 


    prefissoLeft = ordina(stringhe, left, mid);
    prefissoRight = ordina(stringhe, mid + 1, right);
 

    prefisso = cercaSottostringa(prefissoLeft, prefissoRight);
    
    return prefisso;
}

 

int main() {
    vector<string> stringhe;
    string sequenza;
    int casiTest;
 

    cout << "Inserire numero di casi di Test: ";
    cin >> casiTest;

 

    while(casiTest > 0) {
        string input;
        
       
        while(input != "q"){
        	cout << "Inserire stringa o premere 'q' per terminare: ";
        	cin >> input;
        	if(input != "q")
        		stringhe.push_back(input);
		} 
		sequenza = ordina(stringhe, 0, stringhe.size() - 1);
    	cout << "Sequenza comune: " << sequenza << endl;
    	casiTest--;
		stringhe.clear();
		
    }


    return 0;
}

//la complessità dell'algoritmo è pari a O(m*logn), dove m è la minima lunghezza della sottostringa più grande

// CASI DI TEST:
// Sample Input (N.B. per terminare il caso di test premere q ed inviare)
// 1
// apple
// ape
// april
// applied
// 
// Sample Output
// ap

// Sample Input 
// 2
// fiore
// albero
// casa
// fiorire
// alberto
//
// Sample Output
//
// pesca
// partita
// partire
// peso
//
// Sample Output
// p

// Sample Input
// 1
// fiore
// fiorellino
// fioraio
// fiorista
// fiori
//
// Sample Output
// fior