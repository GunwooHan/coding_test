from collections import deque

n = int(input())

for i in range(n):
    docu_count, target_idx = list(map(int,input().split()))
    docu_list = deque(list(map(int,input().split())))
    count = 0

    while True:
        temp_max = max(docu_list)
        
        temp = docu_list.popleft()
        if temp_max == temp:
            count+=1
            if target_idx == 0:
                break
        else:
            docu_list.append(temp)        
    
        if target_idx > 0:
            target_idx-=1
        else:
            target_idx = len(docu_list)-1
        
    print(count)