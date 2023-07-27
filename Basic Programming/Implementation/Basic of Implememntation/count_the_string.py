def solve (S, k):
    # Write your code here
    return list(S).count(k)
    # pass

T = int(input())
for _ in range(T):
    S = input()
    k = input()

    out_ = solve(S, k)
    print (out_)
