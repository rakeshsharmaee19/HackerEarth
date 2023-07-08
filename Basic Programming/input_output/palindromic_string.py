s = input()
i = 0
j = len(s)-1
check = 'YES'
while i<=j:
    if s[i]!=s[j]:
        check='NO'
        break
    i+=1
    j-=1
print(check)
