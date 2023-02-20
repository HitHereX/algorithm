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
