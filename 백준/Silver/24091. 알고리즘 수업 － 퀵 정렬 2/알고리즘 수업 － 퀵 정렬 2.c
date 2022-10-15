#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int cnt = 0 ;
int target;
int n,N;
int *copy;

void swap(int A[], int a, int b)
{
    int tmp =A[a];
    A[a] = A[b];
    A[b]= tmp;
    cnt++;
    if(cnt == target)
        memmove(copy,A,sizeof(int)*N);
}

int partition(int A[],int p, int r)
{

    int pivot = A[r];
    int i = p-1;
    
    for(int j=p;j<r;j++)
    {
        if(A[j] <= pivot )
            swap(A,++i,j);
    }
    if(i+1 != r)
        swap(A,i+1,r);

    return i+1;
}
void quick_sort(int A[], int p, int r)
{
    if(p<r)
    {
        int q = partition(A,p,r);
        quick_sort(A,p,q-1);
        quick_sort(A,q+1,r);
    }
}

void printarray(int A[], int N)
{
    int i;
    for(i=0;i<N;i++)
        printf("%d ",A[i]);
    printf("\n");
}
int main()
{
    scanf("%d %d",&N,&target);
    
    int *A;
    A = (int *)malloc(sizeof(int) * N);
    copy = (int *)malloc(sizeof(int) * N);

    for(int i=0;i<N;i++)
        scanf("%d",&A[i]);
    quick_sort(A,0,N-1);
    if(target > cnt)
        printf("-1");
    else
        printarray(copy,N);
    
    return 0;
}
