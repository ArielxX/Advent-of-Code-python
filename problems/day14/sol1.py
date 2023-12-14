M = []

while True:
    try:
        M.append(input())
    except EOFError:
        break

ans = 0
n = len(M)

for i in range(len(M[0])):
    cur = 0
    for j in range(n):
        if M[j][i] == '.':
            continue
        if M[j][i] == '#':
            cur = j + 1
        else:
            ans += n - cur
            cur += 1

print(ans)