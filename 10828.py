# 자료구조 스택 문제
# 스택 구현 기능 프로그램 만들기
# 1. push X : 정수 X를 스택에 넣는 연산
# 2. pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없을 경우에는 -1을 출력한다.
# 3. size : 스택에 들어있는 정수의 개수를 출력한다
# 4. empty : 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5. top : 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 병근이의 답
print("병근이의 자료구조 스택 구현하기 ~ !!")
print("***STACK 메뉴얼***")
print("1. push X")
print("2. pop ")
print("3. size ")
print("4. empty ")
print("5. top ")
print("6. 종료")
stack = []
menu = 0
push, pop, size, empty, top = 0, 0, 0, 0, 0
while(menu != 6):
    print("***STACK 메뉴얼***")
    print("1. push X")
    print("2. pop ")
    print("3. size ")
    print("4. empty ")
    print("5. top ")
    print("6. 종료")
    menu = int(input("원하시는 메뉴를 입력 하세요 : "))
    if (menu == 1):
        print("스택에 넣을 값을 입력해주세요")
        push = int(input(""))
        stack.append(push)
    elif (menu == 2):
        if(len(stack) != 0):
            pop = stack.pop()
            print("pop으로 추출된 수 : %d"%pop)
        else :
            print(-1)
    elif (menu == 3):
        size = len(stack)
        print(size)
    elif (menu == 4):
        if (len(stack) != 0):
            print(0)
        else :
            print(1)
    elif (menu == 5):
        if(len(stack) != 0):
            top = stack[-1]
            print(top)
        else :
            print(-1)
    elif (menu == 6):
        break
    else : 
        print("입력 오류")


# 백준 답

class Stack:
    def __init__(self):
        self.container = []
        self.count = 0
    
    def push(self, value):
        self.container.append(value)
        self.count += 1
        
    def pop(self):
        if self.count == 0:
            return -1
        self.count -= 1
        return self.container.pop()
        
    def size(self):
        return self.count
    
    def empty(self):
        if self.count == 0:
            return 1
        else:
            return 0
        
    def top(self):
        if self.count == 0:
            return -1
        return self.container[-1]
import sys       
stack = Stack()
N = int(sys.stdin.readline())
for _ in range(N):
    #commnd = input().split()
    commnd = sys.stdin.readline().split()
    if commnd[0] == 'push':
        stack.push(commnd[1])
    elif commnd[0] == 'pop':
        print(stack.pop())
    elif commnd[0] == 'size':
        print(stack.size())
    elif commnd[0] =='empty':
        print(stack.empty())
    else:
        print(stack.top())