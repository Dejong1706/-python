# 네 번째 점
# 세 점이 주어졌을 떄, "축에 평행한 직사각형"을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성
# 입력 : 세 점의 좌표가 한 줄에 하나씩 주어짐, 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수
# 출력 : 직사각형의 네 번째 점의 좌표를 출력함

x, y = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = 0, 0
if y == y2 :
    y4 = y3
elif y == y3:
    y4 = y2
else :
    y4 = y
    
if x == x2 :
    x4 = x3
elif x == x3:
    x4 = x2
else :
    x4 = x
print(x4, y4)


    