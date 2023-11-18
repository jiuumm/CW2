n, k= map(int, input().split())
lst = list(map(int, input().split()))
m= int(input())

cnt=0
def dfs(L,S, sm):
    global cnt
    if L==k:
        if sm % m==0:
            cnt+=1
        
    else:
        for i in range(S, n):
            dfs(L+1, i+1, sm+lst[i])
            
dfs(0,0,0)
print(cnt)