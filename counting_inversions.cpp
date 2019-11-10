#include <iostream>
#include<cmath>
#include<vector>
using namespace std;

int merge(int A[], int l, int m, int r , int* count){
    int n1 = m - l + 1;
    int n2 = r - m;
    
    vector<int> x(n1);
    vector<int> y(n2);
    
    for(int i = 0 ; i < n1 ; i++)
        x[i] = A[l+i];
    for(int j = 0 ; j < n2 ; j++)    
        y[j] = A[m+1+j];
        
    int i = 0, j = 0, k = l ;
    
    while(i < n1 && j < n2){
        if(x[i] <= y[j]){
            A[k] = x[i];
            i++;
        }
        else{
            A[k] = y[j];
            j++;
            *count += n1 - i ;
        }
        k++;
    }
    
    while(i < n1){
        A[k] = x[i];
        i++;
        k++;
    }
    while(j < n2){
        A[k] = y[j];
        j++;
        k++;
    }
    
    //cout << count << endl;
    return 0;
}


int mergesort(int A[], int l, int r){
    
    static int count;
    
    if(r>l){
        int m = floor((l+r)/2);
        mergesort(A,l,m);
        mergesort(A,m+1,r);
        merge(A,l,m,r,&count);
        
    }
    
    return count;
}


int main() {
	// your code goes here
	int A[] = {10,9,8,7,6,5,4,3,2,1,0};
	int size = sizeof(A)/sizeof(A[0]);
	int count = mergesort(A,0,size-1);
	
	cout << count << endl;
	
	for(int i = 0 ; i < size ; i++)
	    cout << A[i] << "\t" ;
	
	return 0;
}
