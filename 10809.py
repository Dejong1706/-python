# 알파벳 소문자로만 이루어진 단어 S가 주어짐
# 단어의 길이는 100을 넘지 않고, 알파벳 소문자로만 이루어짐
# 입력받은 단어안에 각 단어들의 첫번째 위치를 출력하고 없는 단어의 경우 -1을 출력한다

# S = input().lower()
Alpha = []
V = ''
for a in range(97,122):
    if chr(a) in S:
        V = S.find(chr(a))
        Alpha.append(V)
    else :
        Alpha.append(-1)   
for b in range(0,27):
    print(Alpha[b], end = ' ')
     
# 백준 답
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 