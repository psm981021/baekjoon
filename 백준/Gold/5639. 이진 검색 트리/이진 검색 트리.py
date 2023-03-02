import sys
sys.setrecursionlimit(10**4)  # 재귀 깊이 제한 설정

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is  None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.value)


preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

root = Node(preorder[0])
for value in preorder[1:]:
    root.insert(value)
def post_order_print(left, right):
    if left > right:
        return
    else:
        middle = right + 1
        # 현재 구간에서 루트노드보다 큰 노드가 나오는 포인트 찾기
        for i in range(left + 1, right + 1):
            if preorder[i] > preorder[left]:
                middle = i
                break

        post_order_print(left + 1, middle - 1)
        post_order_print(middle, right)
        print(preorder[left])
post_order_print(0, len(preorder) - 1)