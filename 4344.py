# 평균은 넘겠지문제
# 1. 첫줄에 케이스 수 C 부여
# 2. 부여된 케이스 수 만큼의 학생들 점수 입력
# 3. 받은 학생들의 점수의 평균을 구함
# 4. 구한 평균을 넘는 학생의 비율을 소수 세번째 자리까지 출력

# 나의 답
C = int(input(""))
A, averge = 0, 0
G = 0
for i in range(C):
    N = list(map(int, input().split(" ")))
    averge = sum(N) / N[0]
    G = 0
    for j in range(N[0]):
        if N[j+1] > averge :
            G = G + 1
    print("%0.3f"%((G/N[0])*100))

# 백준 답
# C = int(input())
# for i in range(C):
#     N = list(map(int, input().split(' ')))
#     avg = sum(N[1:]) / N[0]
#     cnt = 0
#     for j in N[1:]:
#         if j > avg : 
#             cnt += 1
            
#     print(str("%.3f" %round((cnt/N[0])*100, 3))+"%")
