import sys
input = sys.stdin.readline

count = 8
N = int(input())

i = 1
while True:
    if N - (2**i) == 0:
        count = count + i + 2
        break
    elif N - (2**i) < 0:
        count = count + i + 1
        break

    i += 1

print(count)