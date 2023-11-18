#3-1. 거스름돈

n = 1260
count = 0

#IDEA) 큰 단위 화폐부터 차례대로
coinTypes = [500,100,50,10]

for coin in coinTypes:
    count += n//coin  #동전 몇 개?
    n %= coin

print(count)


#3-2. 큰 수의 법칙
#단순하게 푸는 첫번째 방법

n,m,k = map(int, input().split())       #N,M,K 공백 구분해 입력받기
data = list(map(int,input().split()))   #N개의 수를 공백 구분해 입력받기

data.sort()     #정렬
first = data[n-1]   #가장 큰수
second = data[n-2]  #두번째 큰수

result = 0

while True:
    for i in range(k):
        if m==0: break  #반복문 탈출(여기서 끝날때)
        result += first
        m-=1    #더할 때마다 1씩 빼기
    if m==0: break      #반복문 탈출(여기서 끝날때)

    result += second
    m-=1

print(result)

#M이 매우 커진다면? 두번째 방법
#IDEA) first와 second가 더해지는 '횟수'를 먼저 구하기

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) *k     #first가 더해지는 횟수계산
count += m%(k+1)            #안나눠떨어질때는 나머지도 횟수에 포함

result = 0
result += (count)*first      #가장큰수 더하고
result += (m-count)*first    #두번째큰수 더함

print(result)

#3-3. 숫자 카드 게임
#min() 사용하는 첫번째 풀이

n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    minValue = min(data)            #해당 행에서 min값 찾기
    result = max(result, minValue)  #min값들 중 max값 찾기

print(result)

#2중 반복문 이용하는 두번째 풀이

n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    minValue = 10001        #10000까지 입력가능하므로 10001로 초기화
    for a in data:
        minValue = min(minValue, a) #해당 행에서 min값 찾기
    result = max(result, minValue)  #min값들 중 max값 찾기

print(result)

#3-4. 1이 될 때까지
#단순하게 푸는 첫번째 방법
n,k = map(int,input().split())
result = 0

while n >= k:       # n이 k 이상이면 k로 계속 나누기(숨은조건?)
    while n%k !=0:  # n이 k로 나눠떨어질때까지 1씩 뺌
        n -= 1
        result +=1
    n //= k
    result += 1

while n>1:      # n이 k보다 작아졌을 때
    n -= 1
    result += 1

    print(result)

#N이 10만 초과일 경우 두번째 방법
n,k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k     #n에서 처음으로 나눌수 있을 때까지 뺀값 한번에
    result += (n-target)    #result에 더함
    n=target

    if n<k:                 # n이 k보다 작아졌을 때 반복문 탈출
        break
    result += 1
    n //= k

result += (n-1)             #1이 될때까지 빼는 것이므로
print(result)