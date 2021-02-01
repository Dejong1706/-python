# 1. N의 몇 개의 시험을 받는지 입력
# 2. 시험 점수 입력
# 3. 최고 점을 제외한 나머지 점들을 기존 점수/최고점수*100 으로 다시 구함
# 4. 그렇게 구해진 점수들로 새로운 평균을 구함

# 나의 답
N = int(input("몇 개의 시험을 치루셨나요 ? : "))
subject, Max = 0, 0
list = []
score, hap, New_hap, averge, New_averge = 0, 0, 0, 0, 0
for i in range(0,N):
    subject = int(input("%d번째 과목의 점수를 입력해주세요 : "%(i+1)))
    list.append(subject)
    hap = hap + list[i]
    if Max < list[i] :
        Max = list[i]
    else :
        pass
print(Max)
for j in range(0,N):
    if Max == list[j] :
        pass
    score = list[j] / Max * 100
    New_hap = New_hap + score
averge = hap / N
New_averge = New_hap / N
print("점수 변경전 평균 : %0.1f, 점수 변경후 평균 : %f"%(averge, New_averge))

# 백준 답

num = int(input())
max = 0
avg = 0
inArr = list(map(float, input().split()))
for i in range(num):
        if max < inArr[i]:
                max = inArr[i]
 
for i in range(num):
        inArr[i] = inArr[i]/max*100.0
        avg += inArr[i]
 
print(round(avg/num, 2))

# 재훈 답
def calc_mean(n, m, s):
    re_s = [0]*n
    tmp = 0
    for i in range(n):
        re_s[i] = s[i]/m*100
        tmp += re_s[i]    
    result = tmp/n
    print(result)

if __name__=='__main__':
    N = int(input())
    score = list(map(int, input().split()))
    M = max(score)
    calc_mean(N, M, score)
    