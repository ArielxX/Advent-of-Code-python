M = []

x = 0
y = 0

while True:
    try:
        M.append(input())
        for i in range(len(M[-1])):
            if M[-1][i] == 'S':
                x = len(M) - 1
                y = i
                
    except EOFError:
        break

Q = [(x, y)]
visited = set()
visited.add((x, y))
D = [[-1 for i in range(len(M[0]))] for j in range(len(M))]
D[x][y] = 0

ans = 0

mp = {}
mp['|'] = 0
mp['-'] = 1
mp['L'] = 2
mp['J'] = 3
mp['7'] = 4
mp['F'] = 5
mp['.'] = 6
mp['S'] = 7

Dx = []
Dx.append([[1, 0], [-1, 0]])
Dx.append([[0, 1], [0, -1]])
Dx.append([[-1, 0], [0, 1]])
Dx.append([[-1, 0], [0, -1]])
Dx.append([[1, 0], [0, -1]])
Dx.append([[1, 0], [0, 1]])
Dx.append([])
Dx.append([])

# check which pipe is connected with S
# up
if x - 1 >= 0:
    dd = mp[M[x - 1][y]]
    if [1, 0] in Dx[dd]:
        Dx[7].append([-1, 0])
# down
if x + 1 < len(M):
    dd = mp[M[x + 1][y]]
    if [-1, 0] in Dx[dd]:
        Dx[7].append([1, 0])
# left
if y - 1 >= 0:
    dd = mp[M[x][y - 1]]
    if [0, 1] in Dx[dd]:
        Dx[7].append([0, -1])
# right
if y + 1 < len(M[0]):
    dd = mp[M[x][y + 1]]
    if [0, -1] in Dx[dd]:
        Dx[7].append([0, 1])


while len(Q) > 0:
    x, y = Q.pop(0)

    dd = mp[M[x][y]]

    for dx, dy in Dx[dd]:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= len(M) or ny < 0 or ny >= len(M[0]):
            continue

        if (nx, ny) in visited:
            continue

        if M[nx][ny] == '.':
            continue

        visited.add((nx, ny))
        D[nx][ny] = D[x][y] + 1
        Q.append((nx, ny))
    
        ans = max(ans, D[nx][ny])

print(ans)

# for d in D:
#     print(d)

