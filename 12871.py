s = input("word1 : ") # 문자 s입력
t = input("word2 : ") # 문자 t입력
n = 1
while(True):         # s를 fs로 t를 ft로 각각 무한 문자열을 생성
    fs = s * n
    ft = t * n
    n = n + 1
    if len(fs) == 300:  # 실행시간 관계로 fs가 300자리가 되면 무한문자열 생성 중지
        break
    elif len(ft) == 300:    #실행시간 관계로 ft가 300자리가 되면 무한문자열 생성 중지
        break

if len(s) > len(t):     # 문자열 s가 t보다 클경우
    if ft in fs:         # 무한문자열 fs안에 문자열 t가 있으면 1 없으면 0출력
        print(1)
    else :
        print(0)
else :                  # 문자열 t가 s보다 클경우
    if fs in ft:         # 무한문자열 ft안에 문자열 s가 있으면 1 없으면 0출력
        print(1)
    else :
        print(0)

# 소요시간 : 25분? 30분?