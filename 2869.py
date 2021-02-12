# 달팽이가 높이 V미터인 나무 막대를 올라간다
# 달팽이는 낮에 A미터를 올라갈 수 있다
# 달팽이는 밤에 자는 동안 B미터를 미끄러진다
# 정상에 올라간 후에는 미끄러지지 않는다
# 달팽이가 정상에 올라가는데 몇 일이 걸리는지 구하시오

# 첫째줄 입력 (A, B, V)
# ex) 2 1 5
import sys
import math
A, B, V = map(int, sys.stdin.readline().split()) 
hap = (V-B) / (A-B)
print(math.ceil(hap))

    
