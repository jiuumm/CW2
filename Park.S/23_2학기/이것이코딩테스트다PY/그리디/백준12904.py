#A와 B(골드5)
#그리디

#IDEA) S > T가 아닌 거꾸로 T > S로 생각하기!
#      T의 맨마지막이 A인지 B인지 나눠지기 때문!

import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)
