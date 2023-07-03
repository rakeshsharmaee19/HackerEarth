s = input()
countZ = s.upper().count('Z')
countO = s.upper().count('O')
if countZ*2 == countO:
    print('Yes')
else:
    print('No')
