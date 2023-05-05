n = int(input())
trees = list(map(int, input().split()))
growth = list(map(int, input().split()))
optimal = 0
tree_growth = []

for i in range(n):
    tree_growth.append((trees[i],growth[i]))

tree_growth.sort(key = lambda x: x[1])

#print(tree_growth)
for i in range(n):
    optimal += tree_growth[i][0] + tree_growth[i][1]*i

print(optimal)


#처음에 bruteforcing 문제가 풀고싶어서 찾아 들어갔는데, 
#bruteforcing에 집착하다가 문제의 본질인 그리디를 놓침. 문제를 잘 읽자! 
#대신 그래도 람다 연습은 많이 한 문제
