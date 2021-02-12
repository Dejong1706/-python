# 분수찾기
# (1)1/1 -> (2)(1/2 -> 2/1) -> (3)(3/1 -> 2/2 -> 1/3) -> (4)(1/4 -> 2/3 -> 3/2 -> 4/1)
# (5)(5/1 -> 4/2 -> 3/3 -> 2/4 -> 1/5)
# 홀수번째 선은 n/1으로 시작하며 짝수번째 선은 1/n으로 시작함
# 선마다 n번째는 n개의 분수로 이루어져있음
# 입력한 X번째의 분수가 몇번째 에 위치해있는지 찾아내야됨

''' 병근 답
list = ['1']
num = int(input())
for i in range(2, 6):
  n = 1
  j = i
  if i % 2 == 0:
    while(n < i+1):
      list.append('%d/%d'%(n,j))
      n = n + 1
      j = j - 1
  else :
    while(n < i+1):
      list.append('%d/%d'%(j,n))
      j = j - 1
      n = n + 1
print(list[num-1])
'''
# 다른답
'''
num = int(input())
line, max_num = 0, 0
while num > max_num :
  line += 1
  max_num += line

gap = max_num - num
if num%2 == 0:
  bottom = line - gap
  top = line - bottom + 1
else :
  top = line - gap
  bottom = line - top + 1

print('%d / %d'%(top,bottom))
'''
