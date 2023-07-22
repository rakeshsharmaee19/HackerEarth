for _ in range(int(input())):
    n = input()
    if '21' in n:
        print('The streak is broken!')
    else:
        if int(n)%21==0:
            print('The streak is broken!')
        else:
            print('The streak lives still in our heart!')
