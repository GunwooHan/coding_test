n = int(input())
member = []
answer = []

for i in range(n):
    member.append(list(map(int,input().split())))

rank = 1
for i in range(n):
    for j in range(n):
        if member[i][0] < member[j][0] and member[i][1] < member[j][1]:
            rank+=1
    answer.append(rank)
    rank=1

print(*answer)