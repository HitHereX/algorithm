import sys
from collections import deque
reps = int(sys.stdin.readline())

for i in range(reps):
    #INPUT
    orders = sys.stdin.readline().rstrip()
    len_arr = int(sys.stdin.readline())
    temp_arr = sys.stdin.readline()[1:-2]

    if len_arr == 0:
        arr = deque([])
    else:
        arr = deque(temp_arr.split(','))

    #FLAGS
    rotate = False
    err = False

    #ACT ORDER
    for order in orders:
        if order == 'R':
            if rotate == False: rotate = True
            else: rotate = False

        elif order == 'D':
            if len(arr) == 0:
                err = True
                break
            else:
                if rotate ==  True:
                    arr.pop()
                elif rotate == False:
                    arr.popleft()

    
    if err == True: print('error')
    else: 
        if rotate == False: print('['+','.join(arr)+']')
        else: print('['+','.join(list(arr)[::-1])+']')
