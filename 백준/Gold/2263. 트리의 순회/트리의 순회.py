#https://www.acmicpc.net/problem/2263
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def preorder(in_order_start, in_order_end, post_order_start, post_order_end):
    if in_order_start > in_order_end or post_order_start > post_order_end:
        return
    root = post_order[post_order_end]
    print(root, end=' ')
    idx = idx_dict[root]
    left_size = idx - in_order_start
    preorder(in_order_start, idx-1, post_order_start, post_order_start+left_size-1)
    preorder(idx+1, in_order_end, post_order_start+left_size, post_order_end-1)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

idx_dict = {val:idx for idx, val in enumerate(in_order)}

preorder(0, n-1, 0, n-1)