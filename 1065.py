# 한수 구하기

N = int(input(""))
hansu = 0
for i in range(1,N+1):
    if i <= 99:
        hansu += 1
    else :
        num = list(str(i))
        if(int(num[0]) - int(num[1]) == int(num[1]) - int(num[2])):
            hansu += 1
print(hansu)        
