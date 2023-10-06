#230930(SAT) / 스택 / 실버4
#에디터랑 비슷... 스택 2개로 풀기

n = int(input())

for _ in range(n):
    left = []
    right = []
    cmd = input()

    for i in cmd:
        if i== '<':       # left stack to right
            if left:
                right.append(left.pop())
        elif i == '>':    # right stack to left
            if right:
                left.append(right.pop())
        elif i == '-':    # left stack에서 pop
            if left:
                left.pop()
        else:
            left.append(i)

    # right stack의 문자들은 뒤집은 후 붙여야 함!
    left.extend(reversed(right))

    print(''.join(left))