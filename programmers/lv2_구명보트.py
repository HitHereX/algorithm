from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)
    answer = 0
    limit += 1
    
    while people:
        heavy = people.popleft()
        if len(people)>0:
            if people[-1]+heavy < limit:
                people.pop()
        answer += 1

    return answer

# 1. 역순정렬해서 제일 무거운사람부터 나오게
# 2. people이 살아있는 동안 
#     1. popleft로 가장 무거운 사람 뽑고
#     2. 만약  popleft를 했을 때 deque에 남아 있는 게 있다면 ← 이거 처리 안해서 계속 헛돔!
#     3. 제일 가벼운사람(people[-1]) 뽑아서 2-a.랑 합해서 heavy 랑 대조해보고, limit안이면 얘도 삭제
#     4. 배 한번 떠났으니 += 1
