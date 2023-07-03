n = int(input())
a = input().split()
num = ''
for i in a:
    num+= i[-1]
if int(num[-1])==0:
    print("Yes")
else:
    print('No')
