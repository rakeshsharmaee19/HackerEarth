s = input()
vowels = 'AEIOUY'
check='invalid'
c =True
if len(s)==9:
    if s[2] not in vowels:
        if (int(s[0])+int(s[1]))%2==0 and (int(s[3])+int(s[4]))%2==0 and (int(s[4])+int(s[5]))%2==0 and (int(s[7])+int(s[8]))%2==0:
                check='valid'
print(check)
