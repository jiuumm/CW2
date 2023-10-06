n, k = map(int, input().split())

data = ['?'] * n                                    #초기값 '?'로 초기화
idx = 0
check = True

for i in range(k):
    num, alphabet = input().split()
    idx = (idx + int(num)) % n                      #인덱스 설정 - 원형인 것 고려
    if data[idx] != '?':                            #알파벳 존재하는 경우
        if data[idx] == alphabet:                   #같은 알파벳인 경우 괜찮음
            continue
        check = False                               #해당하는 바퀴가 없는 것으로 처리
    else:
        data[idx] = alphabet                        #위의 경우가 아닌 경우 알파벳 삽입

for i in range(n):
    if data[i] == '?':                              #?는 포함 X(중복가능)
        continue
    for j in range(i + 1, n):
        if data[i] == data[j]:                      #중복된 값이 존재하는 경우
            check = False                           #해당하는 행운의 바퀴 없음
            break

if check:                                           #해당하는 행운의 바퀴가 있는 경우
    for _ in range(n):
        print(data[idx], end='')
        idx = (idx - 1) % n
else:                                               #해당하는 행운의 바퀴가 없는 경우
    print('!')