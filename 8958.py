# 1. 반복할 테스트 케이스의 수가 주어짐
# 2. 반복된 행위는 O 와 X로 표기하는 문자열임
# 3. O는 1점이고 x는 0점임
# 4. O가 계속되서 있을 경우 첫 번째 O 다음 두 번째 O는 2점임

# 병근 답
# N = int(input())
# list = []
# list2 = []
# num = 1
# hap = 0
# for i in range(N):
#     C = input("")
#     for j in range(len(C)):
#         if C[j] == "o":
#             list.append(1)
#         elif C[j] == "x":
#             list.append(0)
#     for h in range(len(list)):
#         if list[h] == 1:
#             list2.append(num)
#             num = num + 1
#         else :
#             list2.append(0)
#             num = 1
#     for k in range(len(list2)):
#         hap = hap + list2[k]
#     print(hap)
#     list = []
#     list2 = []
#     hap = 0

# 백준 답
# a = int(input())
# for i in range(a):
#     b = input()
#     s = list(b)
#     sum = 0
#     c = 1
#     for i in s:
#         if i == 'O':
#             sum += c
#             c += 1
#         else:
#             c = 1
#     print(sum)



OX = list(input())
c = []
count = 1
for i in range(0, len(OX)):
    if OX[i] == 'O':
        c.append(count)
        count = count + 1
    else:
        c.append(0)
        count = 1

print(c)
