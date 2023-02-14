from itertools import permutations

def solution(k, dungeons):
    
    cases = []
    for idx in permutations([i for i in range(len(dungeons))]):
        hp = k
        success = 0
        for i in idx:
            if hp >= dungeons[i][0]:
                success += 1
                hp -= dungeons[i][1]
            else:
                break
        cases.append(success)
    
    return max(cases)

#LEARNED:
#순서를 조정한 완탐을 해야 한다면 
#permutations를 이용해서 가능한 순서조합을 모두 만들 수 있다
