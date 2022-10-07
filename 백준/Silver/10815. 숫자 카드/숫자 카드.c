#include <stdio.h>
#include <stdlib.h>

int S[600000];
int C[600000];
int N=0;

int static compare (const void* first, const void* second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}

void insertion_sort()
{
    int temp;
    int i;
    
    for(i=0;i<N;i++)
    {
        temp =S[i];
        int j =i;
        while(j>=1 && temp <= S[j-1])
        {
            S[j] = S[j-1];
            S[j-1] = temp;
            j--;
        }
    }
}

int binary_section(int start, int end, int num)
{
    int middle;
    while (start <= end)
    {
        middle = (end + start)/2;
        if(S[middle] > num)
            end = middle-1;
        else if(S[middle] < num)
            start = middle+1;
        else
            return 1;
    }
    return 0;
    
    
}

int main()
{
    int n,m,i;
    scanf("%d", &n);
    for(i=0;i<n;i++)
    {
        scanf("%d",S+(N++));
    }
    //insertion_sort();
    
    qsort(S, n, sizeof(int), compare);

    
    scanf("%d", &m);
    for(i=0;i<m;i++)
    {
        scanf("%d",C+i);
    }
     
     
     for(i=0;i<m;i++)
     {
         printf("%d ",binary_section(0,n-1,C[i]));
     }
     
     
}
//6 3 2 10 -10
//10 9 -5 2 3 4 5 -10
