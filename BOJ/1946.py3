import sys
reps = int(input())

for i in range(reps):
  applicants = []
  admit = 1
  num = int(input())
  for j in range(num):
    applicants.append(list(map(int, sys.stdin.readline().split())))

  applicants.sort()
  interview = applicants[0][1]
  
  for j in range(1,num):
    if applicants[j][1] < interview:
      admit += 1
      interview = applicants[j][1]
    
  #print(applicants)
  print(admit)
