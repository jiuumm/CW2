
def DFS(L,start):
    if L==m:
        for j in range(m):
            print(res[j], end= ' ')
            
        print()
    else:
        for i in range(start, n+1):
            if ch[i]==0:
                res[L]=i
                ch[i]=1
                DFS(L+1, i+1)
                ch[i]=0
                
if __name__=='__main__':
    
    n,m = map(int, input().split())
    res= [0]*m
    ch=[0]*(n+1)
    DFS(0,1)
