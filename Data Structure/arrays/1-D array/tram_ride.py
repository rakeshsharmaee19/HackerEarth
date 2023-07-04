def solve (N, start, finish, Ticket_cost):
    # Write your code here
    if start<finish:
        cl_sm = sum(Ticket_cost[start-1:finish-1])
        if start==1:
            ac_sm = sum(Ticket_cost[N-1:finish-2:-1])
        else:
            ac_sm = sum(Ticket_cost[start-2::-1]+Ticket_cost[N-1:finish-2:-1])
        return min(cl_sm,ac_sm)
    else:
        ac_sm = sum(Ticket_cost[start-1:N-1]+Ticket_cost[0:finish-1])
        cl_sm = sum(Ticket_cost[start-2:finish-2:-1])
        return min(cl_sm,ac_sm)

N = int(input())
start = int(input())
finish = int(input())
Ticket_cost = list(map(int, input().split()))

out_ = solve(N, start, finish, Ticket_cost)
print (out_)
