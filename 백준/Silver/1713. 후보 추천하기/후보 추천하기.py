N = int(input()) # 사진틀 개수
Vote = int(input()) # 총 추천 회수
students = list(map(int, input().split())) # 추천 학생 번호
picture = [] # 사진틀
score = [] # 사진틀 인덱스와 매치해서 추천수 저장할 리스트

for i in range(Vote):
    if students[i] in picture: # 사진틀에 있으면
        for j in range(len(picture)): #이부분 N으로 놓고 계속 틀렸음.. ㅋㅋㅋㅋㅋ
            if students[i] == picture[j]:
                score[j] += 1 #점수증가
    else: # 사진틀에 없고
        if len(picture) >= N: # 사진틀 꽉차있으면
            for j in range(N):
                if score[j] == min(score): #가장 작은 점수 찾고
                    del picture[j]
                    del score[j]
                    break #먼저 찾으면 스탑 왜냐면 오래된거일수록 인덱스 앞에 있음
        picture.append(students[i]) #새로운거 뒤에 더해줌
        score.append(1)

picture.sort()
print(' '.join(map(str, picture)))