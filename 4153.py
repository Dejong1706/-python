# 직각삼각형
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오
''' 
입력
- 여러개의 테스트 케이스로 주어지며 마지막줄은 0,0,0이 이볅됨
- 각 테스트 케이스는모두 3만 보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다
출력
- 각 입력에 대해 직각삼각형이 맞다면 "right", 아니라면 "wrong"을 출력
'''
while(True):
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a > b and a > c :
        if a*a == (b*b) + (c*c):
            print("right")
        else :
            print("wrong")
    elif b > a and b > c :
        if b*b == (a*a) + (c*c):
            print("right")
        else :
            print("wrong")
    else :
        if c*c == (a*a) + (b*b):
            print("right")
        else :
            print("wrong")                