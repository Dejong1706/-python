# 팩토리얼 문제
def facto(n):
    if n == 1:
        return 1
    else :
        return n * facto(n-1)
N = int(input())
print(facto(N))

# 순열

def P(n, r):
    return (facto(n) / facto(n-r))

# 조합
def C(n, r):
    return (P(n,r) / facto(r))


