# 벌집만들기
hap, room, six = 1, 1, 6
N = int(input())
if N == 1:
    print(1)
else :
    while True:
        hap = hap + six
        room = room + 1
        if hap >= N :
            print(room)
            break
        else :
            six = six + 6

