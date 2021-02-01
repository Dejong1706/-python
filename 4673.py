
def d(): # 함수 생성
    list = [] # self number인 수들을 받을 리스트
    nself_num = 0
    for i in range(1,10001): # 1부터 10000까지의 반복을 통해 self number들을 리스트에 추가함
        if i < 10:
            nself_num = i + i
            list.append(nself_num)
        elif i < 100:
            nself_num = i + (i//10) + i%10
            list.append(nself_num)
        elif i < 1000:
            nself_num = i + (i//100) + ((i%100) - (i%10)) + (i%10)
            list.append(nself_num)
        elif i < 10000:
            nself_num = i + (i//1000) + ((i%1000) - (i%100) - (i%10)) + ((i%100) - (i%10)) + (i%10)
            list.append(nself_num)
        list.sort() # 리스트 내의 중복된 숫자들을 제거하고 정렬함
    for j in range(1,10001): # 1부터 10000까지 해당 숫자가 리스트 내의 없다면 값을 출력하게 함
        if j in list:
            pass
        else :
            print(j)
d()



        



    


        
        
