#include <stdio.h>
#include <stdlib.h>

int main() {
	int n, i, j;
	int value = -1;
	int* array;
	int* stack;
	int* result;
	int size = -1;
	
	scanf("%d", &n);
	array = malloc(sizeof(int) * n);
	stack = calloc(n, sizeof(int));
	result = malloc(sizeof(int) * n);
	
	for(i = 0; i < n; i++) {
		scanf("%d", &array[i]);
	}
	
	for(i = 0; i < n; i++) {
	    while(size!=-1 && array[stack[size]] < array[i]){
	        result[stack[size]] = array[i] + 1;
	        --size;
	    }
	    stack[++size] = i;
	}
	
	for(i = 0; i < n; i++) {
	    printf("%d ", result[i] - 1);
	}
	
	
	return 0;
	
}