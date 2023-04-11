import sys
def HANOI(x, y, z, cnt):
    if cnt == 0:
        return
    # n-1 번째 원반 두번째 기둥으로 옮겨야 함 
    HANOI(x, z, y, cnt - 1)
    # 가장 큰 크기 원반 출력 1->3
    print(x,z)
    # n-1번째 원반들을 3번째로 옮겨야 함 
    HANOI(y, x, z, cnt - 1)

N = int(sys.stdin.readline())
# 비트연산자로 2의 제곱 연산
print((1 << N) - 1)
# print(2 ** N - 1)
if N <= 20:
    HANOI(1, 2, 3, N)