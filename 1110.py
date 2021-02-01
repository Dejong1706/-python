'''
1. 0보다 크면서 99보다 작은 수 입력받음
2. 상황 2개
- 입력한 수가 10보다 작으면 앞에 0을 붙여 각자리의 수를 합한 후 뒷자리를 앞으로 보내고 합한수를 뒤로 보냄
- 입력한 수가 10보다 클 경우
3. 상황을 계속 반복하다보면 어느 순간 원래 자신의 수로 돌아옴

f. 이 과정들을 거쳐 몇번만의 자신의 수로 돌아오느냐를 구하는 문제
'''
# 병근 답
num = int(input("수 입력 : "))
new_num = num
count = 1
n1, n2, n3 = 0, 0, 0
if(num >= 10):
    n1 = num // 10
    n2 = num % 10
    n3 = n1 + n2
    if (n3 >= 10):
        n3 = n3 - 10
    else :
        pass
    num = n2*10 + n3
else :
    num = num*10 + num
while(num != new_num):
    if(num >= 10):
        n1 = num // 10
        n2 = num % 10
        n3 = n1 + n2
        if (n3 >= 10):
            n3 = n3 - 10
        else :
            pass
        num = n2*10 + n3
    else :
        num = num*10 + num
    count = count + 1
print(count)
# 병근 답

# 백준 답 
tmp = inp = int(input())
count = 0
while True:
    ten = tmp//10
    one = tmp%10
    res = ten + one
    count += 1
    tmp = int(str(tmp%10)+str(res%10))
 
    if (inp==tmp):
        break
print(count)