#include <stdio.h>

#define HEAP_SIZE 100000

int h[HEAP_SIZE];
int h_count;

int get_parent(int i)
{
    return (i - 1) / 2;
}

int get_child(int i)
{
    return 2 * i + 1;
}

void reheap_down(int node)
{
    int child = get_child(node);

    while (child < h_count)
    {
        int left = h[child];
        int right = child + 1 < h_count ? h[child + 1] : 0;

        int max;
            if (child + 1 < h_count)
            max = left > right ? child : child + 1;
        else
            max = child;

        if (h[node] >= h[max])
            break;
        
        int temp = h[node];
        h[node] = h[max];
        h[max] = temp;

        node = max;
        child = get_child(node);
    }
}

void heapify()
{
    int n = h_count;
    if (n % 2 == 0)
        n--;

    while (n > 0)
    {
        int parent = get_parent(n);
        reheap_down(parent);
        n -= 2;
    }
}

void push(int i)
{
    h[h_count++] = i;

    int node = h_count - 1;
    int parnet = get_parent(node);
    while (parnet >= 0)
    {
        if (h[parnet] >= h[node])
            break;
        
        int temp = h[parnet];
        h[parnet] = h[node];
        h[node] = temp;

        node = parnet;
        parnet = get_parent(node);
    }
}

int pop()
{
    if (h_count == 0)
        return 0;

    int ret = h[0];
    h[0] = h[--h_count];
    h[h_count + 1] = 0;

    reheap_down(0);

    return ret;
}

int N;

int main(void)
{
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        int temp;
        scanf("%d", &temp);

        if (temp != 0)
            push(temp);
        else
            printf("%d\n", pop());
    }

    return 0;
}
