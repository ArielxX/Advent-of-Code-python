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
sx = x
sy = y
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

Before = {}
mx = 0
mx_x = (x,y)
Before[(x,y)] = (-1,-1)

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
        Before[(nx, ny)] = (x, y)

        if mx < D[nx][ny]:
            mx = D[nx][ny]
            mx_x = (nx,ny)



Dx[-1] = []
MM = [[0 for i in range(len(M[0]))] for j in range(len(M))]

Q = [mx_x]
MM[mx_x[0]][mx_x[1]] = 1

while len(Q) > 0:
    x, y = Q.pop(0)

    dd = mp[M[x][y]]

    for dx, dy in Dx[dd]:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= len(M) or ny < 0 or ny >= len(M[0]):
            continue

        if MM[nx][ny]:
            continue

        MM[nx][ny] = 1
        Q.append((nx, ny))
    
x = sx
y = sy


# update S to its corresponding pipe
# up
if x - 1 >= 0:
    dd = mp[M[x - 1][y]]
    if [1, 0] in Dx[dd] and MM[x-1][y]:
        Dx[7].append([-1, 0])
# down
if x + 1 < len(M):
    dd = mp[M[x + 1][y]]
    if [-1, 0] in Dx[dd] and MM[x+1][y]:
        Dx[7].append([1, 0])
# left
if y - 1 >= 0:
    dd = mp[M[x][y - 1]]
    if [0, 1] in Dx[dd] and MM[x][y-1]:
        Dx[7].append([0, -1])
# right
if y + 1 < len(M[0]):
    dd = mp[M[x][y + 1]]
    if [0, -1] in Dx[dd] and MM[x][y+1]:
        Dx[7].append([0, 1])
    
H = ['' for i in range(len(M[0]))]
H_cnt = [0 for i in range(len(M[0]))]

for i in range(len(M)):
    vert = ''
    vert_cnt = 0
    for j in range(len(M[0])):

        if MM[i][j]:
            if [1,0] in Dx[mp[M[i][j]]] or [-1,0] in Dx[mp[M[i][j]]]:
                if vert == '':
                    vert = M[i][j]
                    if vert == '|':
                        vert_cnt += 1
                else:
                    if vert == 'L':
                        if M[i][j] == '7':
                            vert = '7'
                            vert_cnt += 1
                        elif M[i][j] == 'J':
                            vert = ''
                    elif vert == 'F':
                        if M[i][j] == '7':
                            vert = ''
                        elif M[i][j] == 'J':
                            vert = 'J'
                            vert_cnt += 1
                    elif [0,1] in Dx[mp[M[i][j]]]:
                        vert = M[i][j]
                    else:
                        vert = ''
                        vert_cnt += 1
            
            if [0,1] in Dx[mp[M[i][j]]] or [0,-1] in Dx[mp[M[i][j]]]:
                if H[j] == '':
                    H[j] = M[i][j]
                    if H[j] == '-':
                        H_cnt[j] += 1
                else:
                    if H[j] == '7':
                        if M[i][j] == 'L':
                            H[j] = 'L'
                            H_cnt[j] += 1
                        elif M[i][j] == 'J':
                            H[j] = ''
                    elif H[j] == 'F':
                        if M[i][j] == 'L':
                            H[j] = ''
                        elif M[i][j] == 'J':
                            H[j] = 'J'
                            H_cnt[j] += 1
                    elif [1,0] in Dx[mp[M[i][j]]]:
                        H[j] = M[i][j]
                    else:
                        H[j] = ''
                        H_cnt[j] += 1
            
            continue

        
        if vert_cnt % 2 == 1 and H_cnt[j] % 2 == 1:
            MM[i][j] = 2
            ans += 1

# for mm in MM:
#     for m in mm:
#         print('O*I'[m], end='')
#     print()


print(ans)

