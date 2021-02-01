# 소수 찾기
# 1. 첫번째 줄의 개수 N이 주어지고
# 2. 두번째 줄의는 N개의 수가 주어짐
# 3. 주어진 수들중 소수의 개수를 출력하면 된다.
# 내 답지(이것도 원하는 답에 출력에는 성공)
from random import *
l = [ ]
N = int(input())
for i in range(1,N+1):
    l.append(randrange(1,1000))
print(l)
for j in range(0,N):
    if l[j]%2 == 0:
        pass
    elif l[j]%3 == 0:
        pass
    elif l[j]%4 == 0:
        pass
    elif l[j]%5 == 0:
        pass
    elif l[j]%6 == 0:
        pass
    elif l[j]%7 == 0:
        pass
    elif l[j]%8 == 0:
        pass
    elif l[j]%9 == 0:
        pass
    else :
        print("%d" %l[j])

# 다른 정답
num = input()
count = int(num)
nums = list(map(int,input().split(' ')))
if len(nums) == int(num):
    for i in nums:
        if i != 1:
            for j in range(2,i):
                if (i/j) % 1 == 0:
                    count -=1
                    break
        else:
            count -=1
else:
    pass
print(count)