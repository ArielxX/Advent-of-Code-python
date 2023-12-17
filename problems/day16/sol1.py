import sys
sys.setrecursionlimit(10000000)

M = []

while True:
    try:
        line = input()
        M.append(line)
    except EOFError:
        break

H = {}

# dir -> 0 = left, 1 = down, 2 = right, 3 = up

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_next(x, y, dir):
    xx = x + dx[dir]
    yy = y + dy[dir]

    return xx, yy

def solve(x, y, dir):
    if x < 0 or x >= len(M) or y < 0 or y >= len(M[0]):
        return
    if not (x, y) in H:
        H[(x, y)] = set()

    if dir in H[(x, y)]:
        return
    
    H[(x, y)].add(dir)
    
    if M[x][y] == '/':
        # 0 <-> 3, 1 <-> 2
        new_dir = (2 * (dir // 2) + (1 - dir % 2) + 2) % 4
        x, y = get_next(x, y, new_dir)
        solve(x, y, new_dir)
    elif M[x][y] == '\\':
        # 0 <-> 1, 2 <-> 3
        new_dir = (2 * (dir // 2) + (1 - dir % 2)) % 4
        x, y = get_next(x, y, new_dir)
        solve(x, y, new_dir)
    elif M[x][y] == '-' and dir % 2 == 1:
        xx, yy = get_next(x, y, 0)
        solve(xx, yy, 0)
        xx, yy = get_next(x, y, 2)
        solve(xx, yy, 2)
    elif M[x][y] == '|' and dir % 2 == 0:
        xx, yy = get_next(x, y, 1)
        solve(xx, yy, 1)
        xx, yy = get_next(x, y, 3)
        solve(xx, yy, 3)
    else:
        xx, yy = get_next(x, y, dir)
        solve(xx, yy, dir)

solve(0, 0, 0)

# for i in range(len(M)):
#     for j in range(len(M[0])):
#         if not (i, j) in H:
#             print('.', end='')
#         else:
#             print('#', end='')
#     print()
print(len(H))
        
