def solve (N, keyboard, word):
    # Write your code here
    count=0
    # print(keyboard)
    for i in keyboard:
        if word[0] in i:
            break
        count+=1
    val = 0
    for i in word:
        if i in keyboard[count]:
            val = 1
        else:
            val=0
            break
    return val


N = int(input())
keyboard = []
for _ in range(N):
    keyboard.append(input())
word = input()

out_ = solve(N, keyboard, word)
print (out_)
