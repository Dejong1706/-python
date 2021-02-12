# 그룹 단어 체커
# 입력할 문자의 개수(N)을 받고, 입력할 문자열 들을 입력받음
# ex) abc = 그룹단어, aabbcc = 그룹단어, aabbcca = 그룹단어(x)
# find함수는 입력받은 글자의 최초 index를 반환한다(사용자가 따로 다른 것을 입력하지 않는 이상)
a, b = 0, 0
N = int(input()) # 반복횟수 입력
for i in range(N):  
    S = input().lower() # 문자열 입력(소문자가아닐시 강제 변환)
    for j in range(1, len(S)):  # 1부터 문자열의 길이까지
        a = S.find(S[j-1])  
        b = S.find(S[j])  
        if a > b:   # 앞글자 인덱스와 뒷글자 인덱스를 비교하여 뒷글자 인덱스가 앞글자보다 작을시 N감소
            N -= 1
            break
print(N)

        

