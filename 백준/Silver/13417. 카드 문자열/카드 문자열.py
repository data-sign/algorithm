## 카드 문자열 
t = int(input())
for _ in range(t): 
    n = int(input())
    card = list(input().split())

    s = card[0]
    for i in card[1:]: 
        if i + s > s: 
            s = s + i
        else: 
            s = i + s
    print(s)
