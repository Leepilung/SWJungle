# 백준 알고리즘 - 1991 트리 순회
# https://www.acmicpc.net/problem/1991
# 시도 횟수 : 2
# 실패 : 0
# 통과 : 2
# Python3이 pypy3ㅁ보다 메모리도 압도적으로 덜먹고 속도도 빨랐음.
import sys

class Node:
    def __init__(self, data,left_node,right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def preorder(node): # 전위 순회
    print(node.data, end= "")
    if node.left_node != ".":
        preorder(tree[node.left_node])
    if node.right_node != ".":
        preorder(tree[node.right_node])
        
def postorder(node):    # 후위 순회
    if node.left_node != ".":
        postorder(tree[node.left_node])
    if node.right_node != ".":
        postorder(tree[node.right_node])
    print(node.data, end= "")


def inorder(node):   # 중위 순회
    if node.left_node != ".":
        inorder(tree[node.left_node])
    print(node.data, end= "")
    if node.right_node != ".":
        inorder(tree[node.right_node])

N = int(sys.stdin.readline())
tree = {}

for i in range(N):
    data, left_node, right_node = sys.stdin.readline().split()
    if left_node == ".":
        left_node = "."
    if right_node == ".":
        right_node = "."
    tree[data] = Node(data, left_node,right_node)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])