
# 런타임 오류가 나지만 평범한 답안
while(True):
    A, B = map(int, input().split())
    if((A < 0) or (B > 10)):
        break
    print(A+B)


# 백준이 원하는 답
while True:
    try:
        a,b=map(int,input().split())
    except EOFError:
        break
    print(a+b)