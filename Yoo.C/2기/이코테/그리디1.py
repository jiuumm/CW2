n=int(input())
coin=[500, 100, 50, 10]

answer=0
for i in coin:
    tmp= n//i
    answer+=tmp
    n= n%i
print(answer)