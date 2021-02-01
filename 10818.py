# 최대 최소 숫자 찾기
# 1. 첫번째 줄에는 개수 N을 입력받음
# 2. 두번째 줄에는 N개 만큼 정수를 입력받음
# 입력받은 정수들 중에서 가장 큰 수와 가장 작은 수를 출력함
# 내 답(제대로 출력 됨)
max = 0
min = 0
N = int(input())
A = list(map(int,input().split(' ')))
min = A[0]
max = A[0]
if len(A) == N:
    for i in range(1,N):
        if max > A[i]:
            pass
        else :
            max = A[i]
    for j in range(1,N-1):
        if min > A[i]:
            min = A[i]
        else :
            pass
print("최대값 : %d, 최소값 : %d"%(max,min))
 
# 백준 답
a = int(input())
b = list(map(int,input().split()))
print("%d %d" %(max(b), min(b)))