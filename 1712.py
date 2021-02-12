# 손익분기점 문제
# 노트북 회사는 노트북 판매 대수와 상관없이 A만원의 고정 비용듬
# 한 대의 노트북의 재료비와 인건비는 B만원의 비용이듬 노트북의 비용은 C임
# A만원 + B만원 < C만원 * num = 이되게 하는 num(손익분기점)을 구하여라
# 손익분기점을 넘기지 못했을 경우 -1을 출력하라 
'''
A, B, C = map(int, input().split()) 
num = 1
while(True):
    if B < C:
        if A+(B*num) < C*num:
            break
        else :
            num += 1
    else :
        num = -1
        break
print(num)
'''
import sys
A, B, C = map(int, sys.stdin.readline().split())
if B < C:
    num = A//(C-B) + 1
    print(num)
else :
    print(-1)
