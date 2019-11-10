#include<iostream>
using namespace std;

bool isPair(int arr[], int lp, int rp, int k){

	while(lp < rp){
		if(arr[lp] + arr[rp] == k)
			return true;

		else if(arr[lp] + arr[rp] > k)
			rp--;

		else
			lp++;
	}

	return false;

}

int main(){
	int arr[] = {2,3,4,8,9,20,40};
	int size = sizeof(arr)/sizeof(arr[0]);
	int k = 15;
	bool flag = false;

	for(int i = 0 ; i < size-1 ; i++){
		flag = isPair(arr, i+1, size-1, k-arr[i]) ;
		if(flag)
			break;
	}

	if(flag)
		cout << "Triplet Sum found" << endl ;

	else
		cout << "Triplet sum not found" << endl ;
}