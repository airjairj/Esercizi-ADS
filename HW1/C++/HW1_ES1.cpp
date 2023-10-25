#include <iostream>

using namespace std;

#define DIM 5

int merge(int v[], int const left, int const mid, int const right) {
    int const n1 = mid - left + 1;
    int const n2 = right - mid;

    int i, j;
    int conteggio = 0;

    // Array temporanei utilizzati per l'ordinamento
    int *leftArray = new int[n1];
    int *rightArray = new int[n2];

    // Popolo gli array
    for (i = 0; i < n1; i++) {
        leftArray[i] = v[left + i];
    }

    for (j = 0; j < n2; j++) {
        rightArray[j] = v[mid + 1 + j];
    }

    int indexOfSubarray1 = 0;
    int indexOfSubarray2 = 0;
    int indexOfMergedArray = left;

    // Merge
    while (indexOfSubarray1 < n1 && indexOfSubarray2 < n2) {
        if (leftArray[indexOfSubarray1] <= rightArray[indexOfSubarray2]) {
            v[indexOfMergedArray] = leftArray[indexOfSubarray1];
            indexOfSubarray1++;
        } else {
            v[indexOfMergedArray] = rightArray[indexOfSubarray2];
            indexOfSubarray2++;
            conteggio += n1 - indexOfSubarray1;
        }
        indexOfMergedArray++;
    }

    // Copio i restanti elementi se ne esistono
    while (indexOfSubarray1 < n1) {
        v[indexOfMergedArray] = leftArray[indexOfSubarray1];
        indexOfMergedArray++;
        indexOfSubarray1++;
    }

    while (indexOfSubarray2 < n2) {
        v[indexOfMergedArray] = rightArray[indexOfSubarray2];
        indexOfMergedArray++;
        indexOfSubarray2++;
    }

    delete[] leftArray;
    delete[] rightArray;

    return conteggio;
}

int mergesort(int v[], int const left, int const right) {
    int conteggio = 0; // conteggio in questa ricorsione

    if (left < right) {
        int mid = left + (right - left) / 2; // deve essere calcolato cos� dato che si pu� riferire a una sottosequenza diversa dal vettore iniziale
        // Count inversioni in questa chiamata ricorsiva
        conteggio += mergesort(v, left, mid);
        conteggio += mergesort(v, mid + 1, right);
        conteggio += merge(v, left, mid, right);
    }

    return conteggio;
}


int main() {
    int size = 0;

    cout << "Inserire size del vettore: ";
    cin >> size;
    int vettore[size];
    int conteggio = 0;

    cout << "Inserire un vettore di " << size << " elementi: " << endl;
    for (int i = 0; i < size; i++) {
        cin >> vettore[i];
    }

    // Count inversioni
    conteggio = mergesort(vettore, 0, size - 1);

    cout << "conteggio: " << conteggio << endl;


    return 0;
}

//La complessità dell'algoritmo è O(nlogn)


// CASI DI TEST:
// Sample Input 
// 10
// 9
// 8
// 6
// 3
// 2
// 0
// 1
// 5
// 4
// 7
// Sample Output
// 29

// Sample Input 
// 6
// 9
// 1
// 0
// 5
// 4
// 71
// Sample Output
// 6

// Sample Input 
// 3
// 1
// 2
// 3
// Sample Output
// 0
