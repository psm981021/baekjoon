import sys

n,m =map(int,sys.stdin.readline().split())
tree = list(map(int,sys.stdin.readline().split()))

def binarysearch(mid):
    result = sum(map(lambda x: 0 if x < mid else (x - mid), tree))
    return result >= m

start, end = 0, max(tree)
while start <= end:
    mid = (start+end) // 2
    if binarysearch(mid):
        start = mid +1
    else:
        end = mid -1
print(end)
