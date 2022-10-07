#include <stdio.h>
#include <stdlib.h>
#include<string.h>

int size = 0;
int front = 0;
int rear = -1;

int *arr[2000000];

void push(int num)
{
    arr[++rear] = num;
    size++;
}

int pop()
{
    if(size != 0 )
    {
        size--;
        return arr[front++];
        
    }
    else
        return -1;
}

int main()
{
    int N,num;
    char order[20];
    scanf("%d",&N);
    
    //int *arr = (int *)malloc(sizeof(int)*N);
    for(int i=0;i<N;i++)
    {
        getchar();
        scanf("%s",order);
        if( strcmp(order,"push") == 0)
        {
            scanf("%d",&num);
            push(num);
        }
        else if( strcmp(order,"pop") == 0)
        {
            printf("%d\n",pop());
        }
        else if( strcmp(order,"size") == 0)
        {
            printf("%d\n",size);
        }
        else if( strcmp(order,"empty") == 0)
        {
            if(size == 0)
                printf("1\n");
            else
                printf("0\n");
        }
        else if( strcmp(order,"front") == 0)
        {
            if(size!= 0)
                printf("%d\n",arr[front]);
            else
                printf("-1\n");
        }
        else if( strcmp(order,"back") == 0)
        {
            if(size!= 0)
                printf("%d\n",arr[rear]);
            else
                printf("-1\n");
        }
    }
        
}
