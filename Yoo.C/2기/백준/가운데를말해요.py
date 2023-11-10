import sys
input = sys.stdin.readline

    
def 전위순회(root):
    if root != ".":
        print(root, end="")
        전위순회(tree[root][0])
        전위순회(tree[root][1])
def 중위순회(root):
    if root !=".":
        중위순회(tree[root][0])
        print(root, end="")
        중위순회(tree[root][1])
def 후위순회(root):
    if root !=".":
        후위순회(tree[root][0])
        후위순회(tree[root][1])
        print(root, end="")
if __name__=='__main__':
    
    n=int(input())
    tree={}

    for i in range(n):
        root, left, right =map(str, input().split())
        tree[root] =[left, right]
        
    전위순회('A')
    print()
    중위순회('A')
    print()
    후위순회('A')