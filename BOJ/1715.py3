import sys
import heapq


reps = int(sys.stdin.readline())
cards = []
ans = 0
for i in range(reps):
  heapq.heappush(cards, int(sys.stdin.readline()))

length = len(cards)

if length == 1:
  ans = 0

elif length == 2:
  ans = sum(cards)

else:
  while len(cards) > 1:
    temp1 = heapq.heappop(cards)
    temp2 = heapq.heappop(cards)
    temp = temp1+temp2
    
    ans += temp
    heapq.heappush(cards, temp)
    
print(ans)
