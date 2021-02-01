# 나머지
# 병근 답
A = []
for i in range(10):
    B = int(input(""))
    B = B % 42
    A.append(B)
A = set(A)
print(len(A))

# 백준 답
num_list = []
for _ in range(10):
    num = int(input())
    num_list.append(num % 42)
num_list = set(num_list)
print(len(num_list))






