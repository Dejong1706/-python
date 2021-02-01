
while(True):
    A, B = map(int, input().split())
    if(((A < 0) or (B > 10)) or ((A == 0) and (B == 0))):
        break
    print(A+B)