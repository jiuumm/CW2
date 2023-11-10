n, m= map(int, input().split())
lst=[]
for i in range(n):
    tmp=list(map(int, input().split()))
    lst.append(tmp)
lst_2=[]
for i in range(n):
    tmp=lst[i][0]
    for j in range(1,m):
        if lst[i][j]<tmp:
            tmp= lst[i][j]
    lst_2.append(tmp)
lst_2.sort()

print(lst_2[-1])
        