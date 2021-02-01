n=int(input())

count=0
def trans(char):
    return ord(char)-97

for i in range(n):
    check = 1
    flag = [False] * 26
    s = list(map(trans,list(input())))
    while s:
        temp=s.pop()
        if flag[temp]:
            check = 0
            break
        else:
            flag[temp]=True
        while s and s[-1]==temp:
            s.pop()
    if not s:
        count+=check
    # else:
    #     pass
print(count)