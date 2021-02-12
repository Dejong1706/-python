# 직사각형에서 탈출
# 한수는 지금 (x, y)에 있다. 직사각형의 왼쪽 아래 꼭짓점은 (0, 0)에 있고, 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 x, y, w, h가 주어진다
# 출력 : 첫째 줄에 문제의 정답을 출력한다.
# 왼쪽과 아랫쪽 변에 거리도 생각해야함...
x, y, w, h = map(int, input().split())
fx, fy = 0, 0
if x > abs(x-w):
    fx = abs(x-w)
else :
    fx = x
if y > abs(y-h):
    fy = abs(y-h)
else :
    fy = y

if fx > fy :
    print(fy)
else :
    print(fx)

