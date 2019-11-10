#include <stdio.h>

void printarray(int arr[], int size){
	for (int i = 0; i<size; ++i)
		printf("%d\t",arr[i]);
}

void merge(int arr[], int l, int mid, int r){
	int n = mid-l+1;
	int m = r-mid;

	int left[n];
	int right[m];

	for(int i=0 ; i<n ; i++)
		left[i] = arr[i+l];

	for(int i=0 ; i<m ; i++)
		right[i] = arr[i+mid+1];

	int i = 0;
	int j = 0;
	int k = l;

	while(i<n && j<m){
		if(left[i] <= right[j]){
			arr[k] = left[i];
			i++;
		}
		else{
			arr[k] = right[j];
			j++;
		}
		k++;
	}

	while(i<n){
		arr[k] = left[i];
		i++;
		k++;
	}

	while(j<m){
		arr[k] = right[j];
		j++;
		k++;
	}

}

void mergeSort(int arr[], int l, int r){
	if(l<r){
		int mid = (l+r)/2;
		mergeSort(arr, l, mid);
		mergeSort(arr, mid+1, r);
		merge(arr, l, mid, r);
	}
}

int main(){
	int arr[] = {2,67,1,34,58,2,0};
	int size = sizeof(arr)/sizeof(arr[0]);

	mergeSort(arr, 0, size-1);

	printarray(arr, size);
}