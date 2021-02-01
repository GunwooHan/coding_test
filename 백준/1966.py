loop = int(input())
for i in range(loop):
    _,pos=list(map(int,input().split()))
    nums = list(map(int,input().split()))
    result = 0
    while nums:
        max_value = max(nums)
        temp = nums.pop()
        if temp == max_value:
            if pos == len(nums):
                result+=1
                break
            elif pos > 0:
                pos += 1
                result +=1
            else:
                pos = len(nums)-1
                result += 1
        else:
            nums.insert(0,temp)
            result += 1
            if pos > 0:
                pos -= 1
                result +=1
            else:
                pos = len(nums)-1
                result += 1

    print(result)
