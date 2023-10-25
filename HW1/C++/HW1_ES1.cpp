#include <iostream>

using namespace std;

#define DIM 5

int merge(int v[], int const left, int const mid, int const right){

	int const n1 = mid-left+1;
	int const n2 = right-mid;
	
	int i, j;
	int conteggio = 0;

	
	//array temporanei utilizzati per l'ordinamento
	int *leftArray = new int[n1];
	int *rightArray = new int[n2];
	
	//popolo gli array
	for(i=0; i<n1; i++){
		leftArray[i] = v[left+i]; 
	}
	
	for(j=0; j<n2; j++){
		rightArray[j] = v[j+mid+1];
	}
	
	int indexOfSubarray1 = 0;
	int indexOfSubarray2 = 0;
	int indexOfMergedArray = left;
	
	//merge
	
	while(indexOfSubarray1 < n1 && indexOfSubarray2 < n2){
		
		if(leftArray[indexOfSubarray1] < rightArray[indexOfSubarray2]){
			
			v[indexOfMergedArray] = leftArray[indexOfSubarray1];
			indexOfSubarray1++;
			
		}else{
			
			v[indexOfMergedArray] = rightArray[indexOfSubarray2];
			indexOfSubarray2++;
			
			/*
			Quando si verifica una inversione (cio�, quando un elemento da rightArray � minore di un elemento da leftArray), 
			significa che tutti gli elementi rimanenti in leftArray sono maggiori di quell'elemento da rightArray. Pertanto, 
			il numero di inversioni � uguale al numero di elementi rimanenti in leftArray, che � subArrayOne - indexOfSubArrayOne
			Quando un elemento da rightArray viene collocato prima di un elemento da leftArray, incrementiamo il conteggio delle 
			inversioni di questo valore. In altre parole, stiamo contando quante inversioni ci sono quando un elemento da rightArray 
			viene posizionato prima di pi� di un elemento consecutivo da leftArray.
			*/
			
			conteggio += (n1-indexOfSubarray1);
			
		}
		indexOfMergedArray++;
	}
	
	//copio i restanti elementi se ne esistono
	
	while(indexOfSubarray1 < n1){
		
		v[indexOfMergedArray] = leftArray[indexOfSubarray1];
		indexOfMergedArray++;
		indexOfSubarray1++;
			
	}
	
	while(indexOfSubarray2 < n2){
		
		v[indexOfMergedArray] = rightArray[indexOfSubarray2];
		indexOfMergedArray++;
		indexOfSubarray2++;
			
	}
	
	delete[] leftArray;
	delete[] rightArray;
	
	return conteggio;
}

int mergesort(int v[], int const left, int const right, int &conteggioInversioni){
	int mid;
	int conteggio = 0; //conteggio in questa ricorsione
	
	if(left<right){
		mid = left + (right - left)/2; //deve essere calcolato cos� dato che si pu� riferire ad una sottosequenza diversa dal vettore iniziale
	} else {
		return 0;
	}
	
	//conto gli scambi ad ogni chiamata ricorsiva e a seguito edl merge
	conteggio += mergesort(v, left, mid, conteggioInversioni);
	conteggio += mergesort(v, mid+1, right, conteggioInversioni);
	conteggio += merge(v, left, mid, right);
	
	return conteggio;
	
}

void stampaVettore(int v[], int size){
	for(int i=0; i<size; i++){
		cout<<"v["<<i<<"]: "<<v[i]<<" "<<endl;
	}
}

int main(){
	
	int size=0;
	
	int vettore[size];
	int conteggio = 0;
	int casiTest;
	
	//cout<<"Size vettore: "<<size;
	cout <<"Inserire numero di casi di Test: "<<endl;
	cin>>casiTest;
	while(casiTest > 0){
		cout<<"Inserire size del vettore: "<<endl;
		cin>>size;
		cout<<"Inserire un vettore di  "<<size<<" elementi: "<<endl;
		for(int i = 0; i < size;i++){
			cin>>vettore[i];
		}	
	
	/*	cout<<"Array non ordinato: "<<endl;
		stampaVettore(vettore, size);*/
		
		conteggio = mergesort(vettore, 0, size-1, conteggio);
	
		cout<<"conteggio: "<<conteggio<<endl ;
	
	/*	cout<<" Array ordinato: "<<endl;
		stampaVettore(vettore, size);*/
		
		casiTest--;
			
	}
	
	return 0;
	
}

//La complessità dell'algoritmo è O(nlogn)