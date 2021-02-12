# 부녀회장이 될테야

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    p = []
    for j in range(1,n+1): # 0층에 사는 인간들 리스트에 누적 인구수 넣어놓고
        p.append(j)
    for a in range(k):  # k층 까지 반복
        for b in range(1,n):    # 1호 제외하고 2호부터 n호까지 층마다 누적인구수 다시 넣어놈 
            p[b] = p[b] + p[b-1]
    print(p[n-1]) # 원하는 호에 해당하는 리스트의 값 출력