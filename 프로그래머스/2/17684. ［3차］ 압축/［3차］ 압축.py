def solution(msg):
    d = dict()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for idx, alpha in enumerate(alpha): 
        d[alpha] = idx+1

    word = msg
    num = 26
    answer = []
    while word: 
        for i in range(len(word), 0, -1): 
            w = word[:i]
            try: 
                if d[w]: 
                    # print(w, d[w], i)
                    answer.append(d[w])
                    num += 1
                    d[word[:i+1]] = num
                    # 입력에서 제거 
                    word = word[i:]
                    # print(word)
                    # print("dict", d)
                    break
            except: 
                continue 
    return answer