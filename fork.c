#include <stdio.h>
#include <sys/types.h>

int main(){
	File *fp = fopen("test.txt","w");
	fprintf(fp,"Hello");
	fork();
}