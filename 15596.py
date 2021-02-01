# 정수 n개의 합
# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
# a = 합을 구해야 하는 정수 n개가 저장되어 있는 리스트
# 리턴값 : a에 포함되어 있는 정수 n개의 합(정수)

# 나의 답
def solve(C):
    ans = 0
    for i in range(len(C)):
        ans = ans + C[i]
    return ans
hap = 0
C = list(map(int,input().split()))
hap = solve(C)
print(hap)

# 백준 답
def solve(a):
    return sum(a)









