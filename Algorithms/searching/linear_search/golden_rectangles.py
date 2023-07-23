count = 0
for _ in range(int(input())):
    w, h = list(map(int, input().split()))
    if w>h:
        if int(w)/int(h)>=1.6 and int(w)/int(h)<=1.7:
            count+=1
    else:
        if int(h)/int(w)>=1.6 and int(h)/int(w)<=1.7:
            count+=1
print(count)
