n, m = map(int, input().split())
res=[0]*(m)
ch=[0]*(n+1)
def dfs(L,S):
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
    else:
        for i in range(S,n+1):
            if ch[i]==0:
                res[L]=i
                ch[i]=1
                dfs(L+1, i+1)
                ch[i]=0
                    
    
    
    

dfs(0,1)