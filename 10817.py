A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
second = 0
if ((A > B and B > C) or (B > A and B < C)) :
    second = B
elif ((B > A and A > C) or (A > B and A < C)) :
    second = A
elif ((C > A and C <B) or (C < A and C > B)) :
    second = C
else :
    print("error")

print("%d" %second)
## 병근 풀이

## 정답 풀이
a, b, c = map(int, input().split(' '))

if(a >= b):
    if(a >= c):
        if(b >= c):
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if(b >= c):
        if(a >= c):
            print(a)
        else:
            print(c)
    else:
        print(b)