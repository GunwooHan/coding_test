count = int(input())
member=[]
for i in range(count):
    member.append(list(map(int,input().split())))

result = []
rank = 1
for i in range(count):
    for j in range(count):
        if member[i][0] < member[j][0] and member[i][1] < member[j][1]:
            rank+=1
    result.append(rank)
    rank=1
for i in result:
    if i != result[-1]:
        print(i,end=" ")
    else:
        print(i)

