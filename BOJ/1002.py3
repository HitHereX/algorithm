from math import sqrt

reps = int(input())

for i in range(reps):
    ui = list(map(int, input().split()))
    x = [ui[0], ui[3]]
    y = [ui[1], ui[4]]
    r = [ui[2], ui[5]]

    dist = sqrt(abs(x[1]-x[0])**2 + abs(y[1]-y[0])**2)
    print(dist)

    #case 0: infinite
    if x[0] == x[1] and y[0] == y[1] and r[0] == r[1] : print(-1)
    #case 1
    elif dist > sum(r) : print(0)
    #case 2
    elif dist == sum(r) : print(1)
    else:
        #case 4
        if max(r) == dist + min(r): print(1)
        #case 5
        elif max(r) > dist + min(r) : print(0)
        #case 3
        else: print(2)
