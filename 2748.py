'''피보나치 수열 구하기'''


def fibonachi(n):
    if n > 2 :
        return fibonachi(n-1) + fibonachi(n-2)
    else :
        return 1

n = int(input("피보나치 수열 입력 : "))
print("%d번째 피보나치 수열 : %d"%(n,fibonachi(n)))
