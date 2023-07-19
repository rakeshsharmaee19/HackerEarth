def solve (N, workload):
    i = 0
    mx=0
    count = 0
    while i<N:
        if workload[i]>6:
            count+=1
        else:
            mx = count if mx<count else mx
            count = 0
        i+=1
    mx = count if mx<count else mx
    return mx
    # Write your code here

N = int(input())
workload = list(map(int, input().split()))

out_ = solve(N, workload)
print (out_)
