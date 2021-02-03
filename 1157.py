# 알파벳 대소문자로 된 단어가 주어지면, 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램
# 대소문자 구분 X
# 많이 사용된 알파벳이 여러개일경우 ?를 출력

A = input().upper()         # 알파벳을 입력받음과 동시에 대문자로 변환
count, max, maxi = 0, 0, ""
for i in A :                # 한 단어마다 검사
    count = A.count(i)      # count변수의 단어의 개수를 대입
    if count > max :        # max보다 count가 크면 max에 count를 대입하고  
        max = count         # maxi에 현재 단어를 대입
        maxi = i
    elif count == max:      # count가 max와 값이 같다면
        if maxi == i:       # 지금 확인하는 단어와 그전에 maxi에 있는 단어가 같다면 maxi에 ?대입
            continue
        maxi = "?"
print(maxi)

# 11:30분시작 11:55분 해결


    



    
    
     
