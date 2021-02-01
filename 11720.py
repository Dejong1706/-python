N = int(input())
num_list = list(input(""))
hap = 0
for i in range(len(num_list)):
    hap += int(num_list[i])
print(hap)