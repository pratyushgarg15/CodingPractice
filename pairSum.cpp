#include<iostream>
using namespace std;

bool isPair(int arr[], int lp, int rp, int k){

	while(lp < rp){
		if(arr[lp] + arr[rp] == k){
			cout << arr[lp] << " + " << arr[rp] << " = " << arr[lp] + arr[rp] << endl ;
			return true;
		}

		else if(arr[lp] + arr[rp] > k)
			rp--;

		else
			lp++;
	}

	return false;

}

int main(){
	int arr[] = {2,4,6,7,11,15};
	int size = sizeof(arr)/sizeof(arr[0]);
	int k = 15;

	cout << isPair(arr, 0, size-1, k) << endl;
	
}