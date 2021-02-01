#곱셈 문제

num1 = int(input(""))
num2 = int(input(""))
n, n1, hap = 0, 0, 0
hap = num1*num2
list = []
while(True):
    if num2 > 100 :
        n = num2 // 100
        list.append(n)
        num2 = num2 % 100
    elif ((num2 < 100) and (num2 > 10)):
        n = num2 // 10
        list.append(n)
        num2 = num2 % 10
    else :
        list.append(num2)
        break
for i in range(2,-1,-1):
    n1 = list[i] * num1
    print(n1)
print(hap)



