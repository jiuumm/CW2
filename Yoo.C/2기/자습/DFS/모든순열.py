def dfs(l):
    global n, res
    if l==n:
        for i in range(n):
            print(res[i], end=" ")
        print()
        return
    else:
        for i in range(1, n+1):
            if i not in res:
                res[l]=i
                dfs(l+1)
                res[l]=0
            

if __name__=='__main__':
    n= int(input())
    res = [0]*n
    dfs(0)
