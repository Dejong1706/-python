# 다이얼 문제
# 숫자 1을 걸면 총 2초가 필요, 다음 숫자마다 +1초씩 걸림
# 각 숫자에는 알파벳 문자가 있음
# 문자열을 입력받고 다이얼프로그램으로 돌렸을 때 몇초가 나오는지 구해야함

def calltime(s):
    time = 0
    for i in s:
        for j in range(65,91):
            if i == chr(j):
                if j < 68:
                    time += 3
                elif j < 71:
                    time += 4
                elif j < 74:
                    time += 5
                elif j < 77:
                    time += 6
                elif j < 80:
                    time += 7
                elif j < 84:
                    time += 8
                elif j < 87:
                    time += 9
                elif j <= 90:
                    time += 10
    return time
if __name__ == "__main__":
    s = input()
    s = s.upper()
    print(calltime(s))

