#A와 B - 그리디

#맨뒤에 A추가
#뒤집고 B추가

s = input()
t = input()

while len(t) > len(s):
    if t[-1] == "A":
        t = t[:-1]  # 마지막 문자 제거
    else:
        t = t[:-1]  # 마지막 문자 제거
        t = ''.join(reversed(t))  # 다시 문자열 뒤집기

if t == s:
    result = 1
else:
    result = 0

print(result)