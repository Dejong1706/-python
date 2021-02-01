# 1. 9개의 서로 다른 자연수 입력
# 2. 9개 중 최댓값 구하기
# 3. 최댓값이 몇 번째에 위치해 있는지 구하기

Max, num1, num2 = 0, 0, 0
list = []
for i in range(9):
    N = int(input(""))
    list.append(N)
    if N > Max :
        Max = N
for j in range(9):
    num = list[j]
    if (num == Max):
        num2 = j + 1
        break
print(Max)
print(num2)

    

