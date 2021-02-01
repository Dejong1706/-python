# 숫자의 개수
# 세 개의 자연수 A,B,C 가 주어지고 그 세 수의 곱의 결과에서
# 0,1,2....9까지 각 숫자들이 몇번 쓰였는지 구하는 프로그램

A, B, C = map(int, input().split(' '))
hap = 0
hap = A*B*C
hap = str(hap)
num0, num1, num2, num3, num4, num5, num6, num7, num8, num9 = 0,0,0,0,0,0,0,0,0,0
num0 = hap.count('0')
num1 = hap.count('1')
num2 = hap.count('2')
num3 = hap.count('3')
num4 = hap.count('4')
num5 = hap.count('5')
num6 = hap.count('6')
num7 = hap.count('7')
num8 = hap.count('8')
num9 = hap.count('9')
print(num0)
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
print(num7)
print(num8)
print(num9)



    