'''조건
귀차니즘 상근이의 설탕배달 ~
가게에 3, 5kg 봉지가 있는데 무게가 주어지면 최소한의 봉지로 담아감
ex) 18kg일 때 5kg 3개와 3kg 1개를 들고가면됨
'''

print("==========상근이의 설탕배달==========")

def sugar_delivery(sugar):
    s5, s3 = 0, 0
    if (sugar%5 == 0):
        s5 = sugar/5
    elif ((sugar%3 == 0) and (sugar%5 != 0)):
        if (((sugar%5)%3) == 0):
            s5 = sugar/5
            s3 = (sugar%5)/3
        else :
            s3 = sugar/3
    elif ((sugar%3 != 0) and (sugar%5 != 0)):
        if (((sugar%5)%3) == 0):
            s5 = sugar/5
            s3 = (sugar%5)/3
        else :
            pass
    else :
        pass
    return s3, s5

    n = int(input("배달할 설탕의 무게를 입력해주세요 : "))
    s3, s5 = sugar_delivery(n)
    if((s3 > 0) or (s5 > 0)):   
        print("%dkg의 설탕을 담기 위해서는 3kg봉지는 %d봉지, 5kg봉지는 %d봉지가 필요합니다"%(n,s3,s5))
    else :
        print("-1")


'''
백준 정답
inp = int(input())
Box = 0
while True:
    if (inp % 5) == 0:
        Box = Box + (inp//5)
        print(Box)
        break
    inp = inp-3
    Box += 1
    if inp < 0:
        print("-1")
        break
'''
