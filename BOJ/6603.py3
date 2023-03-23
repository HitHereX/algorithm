from itertools import combinations

while True:
    temp = input()

    if temp == '0': break
    else:
        temp = list(map(int, temp.split()))
        s = temp[1:]
        s.sort()
        cand = combinations(s, 6)
    
        for i in cand:
            print(*i)
        print("")
