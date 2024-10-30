t = int(input())

for _ in range(t):
  n = int(input())
  start = 1
  end = n
  result = 0

  while start <= end:
      mid = (start + end) // 2
      if ((mid+1) * mid ) // 2 <= n: # 건널 수가 징검다리 개수보다 작으면
        start = mid + 1
        result = mid
      else: # 징검다리 개수보다 큰경우
        end  = mid - 1
  print(result)