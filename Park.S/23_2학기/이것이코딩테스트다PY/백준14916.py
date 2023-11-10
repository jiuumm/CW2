#거스름돈(실버5)
#그리디

def min_coin_count(money):
    count = 0

    while money > 0:
        if money % 5 == 0:
            count += money // 5
            break
        else:
            money -= 2
            count += 1

    if money < 0:
        return -1
    else:
        return count

if __name__ == '__main__':
    money = int(input())

    result = min_coin_count(money)

    print(result)
