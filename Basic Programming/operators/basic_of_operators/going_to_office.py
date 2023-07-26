d = int(input())
oc,of,od = list(map(int, input().split()))
cs,cb,cm,cd = list(map(int, input().split()))
ot = oc+(d-of)*od
oft = cb + ((d/cs)*cm) + (d*cd)
if ot<=oft:
    print('Online Taxi')
else:
    print('Classic Taxi')
