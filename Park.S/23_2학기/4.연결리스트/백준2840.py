#231006(FRI) / 연결 리스트 / 실버4
#원형 이중 연결 리스트
#idea) 돌림판을 고정시키고 화살표를 움직인다!

#오류수정필요
import sys
n, k = map(int, input().split())
x = [0 for _ in range(n)]
idx = 1
for i in range(k):
    a, b = input().split()
    idx -= int(a)
    if x[idx % n] == 0:
        x[idx % n] = b
    elif x[idx % n] != b:
        print('!')
        sys.exit()
for i in x:
    if i != 0 and x.count(i) > 1:
        print('!')
        sys.exit()
        
x.reverse()
i = x.index(b)
cnt = 0
while cnt < n:
    if x[i] == 0: 
        print('?',end='')
    else: 
        print(x[i],end='')
    cnt += 1
    i -= 1