M = []

while True:
    try:
        M.append(input())
    except EOFError:
        break

V = [M]

def go_up(M):
    n = len(M)
    new_M = [[] for _ in range(n)]
    m = len(M[0])
    for i in range(m):
        cur = 0
        for j in range(n):
            if M[j][i] == '.':
                new_M[i].append('.')
                continue
            if M[j][i] == '#':
                new_M[i].append('#')
                cur = j + 1
            else:
                new_M[i].append('.')
                new_M[i][cur] = 'O'
                cur += 1
    
    new_M = list(map(lambda x: ''.join(x), new_M))

    return new_M

def go_down(M):
    n = len(M)
    m = len(M[0])
    new_M = [['.' for _ in range(n)] for _ in range(m)]
    for i in range(m):
        cur = n - 1
        for j in range(n-1, -1, -1):
            if M[j][i] == '.':
                new_M[i][j] = '.'
                continue
            if M[j][i] == '#':
                new_M[i][j] = '#'
                cur = j - 1
            else:
                new_M[i][j] = '.'
                new_M[i][cur] = 'O'
                cur -= 1
    
    new_M = list(map(lambda x: ''.join(x), new_M))
    return new_M

def simulate_cycle(M):
    M = go_up(M)
    M = go_up(M)
    M = go_down(M)
    M = go_down(M)
    return M


cnt = 1000000000

for i in range(1, cnt + 1):
    M = simulate_cycle(M)

    if M in V:
        # found cycle
        cycle_len = i - V.index(M)
        M = V[(cnt - i) % cycle_len + V.index(M)]
        break

    V.append(M)

def solve(M):
    ans = 0
    n = len(M)

    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'O':
                ans += n - i

    return ans

print(solve(M))




    