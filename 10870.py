# 피보나치 수 5 (브2)

# 동적계획법 X
def fibo(n):
    if n <= 1:
        return n
    else :
        return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))

# 동적계획법 O
f = [0 for i in range(100)]
def fibo(n):
    if f[n] != 0 :
        return f[n]
    else :
        if n == 1 or n == 2:
            f[n] = 1
        else : 
            f[n] = fibo(n-1) + fibo(n-2)
        return f[n]
n = int(input())
print(fibo(n))