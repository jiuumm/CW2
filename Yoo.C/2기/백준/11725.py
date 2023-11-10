n= int(input())
tree =[[]for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
#print(tree)

parents = [0 for _ in range(n+1)]
