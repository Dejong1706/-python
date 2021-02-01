C = int(input())
for i in range(C):
    N, T = input().split()
    moonja = ""
    for i in T:
        moonja = moonja + int(N)*i
    print(moonja)