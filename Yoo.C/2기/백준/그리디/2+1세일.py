n= int(input())
lst=[]
for _ in range(n):
    tmp=int(input())
    lst.append(tmp)
lst.sort(reverse=True)
sm=0
for i in range(len(lst)):
    if (i+1) %3 ==0:
        continue
    else:
        sm+=lst[i]
print(sm)
        