import sys
input  = sys.stdin.readline
n= int(input())
lst=[]
for i in range(n):
    tmp=int(input())
    lst.append(tmp)
lst.sort(reverse=True)
answer=0
for i in range(len(lst)):
    tmp=lst[i]-(i)
    if tmp<0:
        answer+=0
    else:
        answer+=tmp
    
print(answer)