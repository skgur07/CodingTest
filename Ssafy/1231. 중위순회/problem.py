import sys

sys.stdin = open('input.txt', 'r')

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def in_order(root):
    global result
    if root:
        in_order(root.left)
        result += root.val
        in_order(root.right)


for tc in range(1, 11):
    N = int(input())
    tree = {}
    result = ''
    for i in range(1, N + 1):
        tree[str(i)] = TreeNode(None)

    for _ in range(N):
        info = input().split()
        tree[info[0]].val = info[1]
        
        if len(info) >= 3:
            tree[info[0]].left = tree[info[2]]
        if len(info) >= 4:
            tree[info[0]].right = tree[info[3]]
    
    in_order(tree['1'])
    print(f"#{tc} {result}")