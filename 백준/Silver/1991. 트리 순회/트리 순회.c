#include <stdio.h>
#include <stdlib.h>

char tree[30][3];
int n = 0;
void preorder_traverse(int start)
{
    printf("%c", start + 'A');
    if (tree[start][0] != '.')
        preorder_traverse(tree[start][0] - 'A');
    if (tree[start][1] != '.')
        preorder_traverse(tree[start][1] - 'A');
}
void inorder_traverse(int start)
{
    if (tree[start][0] != '.')
        inorder_traverse(tree[start][0] - 'A');
    printf("%c", start + 'A');
    if (tree[start][1] != '.')
        inorder_traverse(tree[start][1] - 'A');
}
void postorder_traverse(int start)
{
    if (tree[start][0] != '.')
        postorder_traverse(tree[start][0] - 'A');
    if (tree[start][1] != '.')
        postorder_traverse(tree[start][1] - 'A');
    printf("%c", start + 'A');
}

int main()
{
    int Test;
    char x;
    scanf("%d%c", &Test,&x);
    char c;
    char left;
    char right;
    for (int i = 0; i < Test; i++)
    {
        scanf("%c %c %c%c", &c, &left, &right, &x);
        tree[c - 'A'][0] = left;
        tree[c - 'A'][1] = right;
    }
    
    preorder_traverse(0);
    printf("\n");
    inorder_traverse(0);
    printf("\n");
    postorder_traverse(0);
    printf("\n");
}
/*
 7
 a b c
 b d .
 c e f
 e . .
 f . g
 d . .
 g . .
 */
