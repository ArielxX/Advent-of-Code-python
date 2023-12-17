import heapq
import sys
sys.setrecursionlimit(10000000)

M = []

while True:
    try:
        M.append(input())
    except:
        break

# dir -> 0 = left, 1 = down, 2 = right, 3 = up
    
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def get_next(x, y, dir):
    xx = x + dx[dir]
    yy = y + dy[dir]

    return xx, yy


def solve():
    # get minimum distance from 0,0 to buttom right using dijkstra

    # priority queue
    Q = []

    D = [[[sys.maxsize for _ in range(4)] for _ in range(len(M[0]))] for _ in range(len(M))]

    heapq.heappush(Q, (0, 0, 0, 1))
    heapq.heappush(Q, (0, 0, 0, 2))

    while len(Q) > 0:
        d, x, y, dir = heapq.heappop(Q)

        if d < D[x][y][dir]:
            D[x][y][dir] = d
        else:
            continue

        for i in range(4):
            if i:
                if d < D[x][y][(dir + 1) % 4]:
                    heapq.heappush(Q, (d, x, y, (dir + 1) % 4))
                if d < D[x][y][(dir + 3) % 4]:
                    heapq.heappush(Q, (d, x, y, (dir + 3) % 4))
            
            x, y = get_next(x, y, dir)

            if x < 0 or x >= len(M) or y < 0 or y >= len(M[0]):
                break

            d += int(M[x][y])

    return min(D[len(M) - 1][len(M[0]) - 1])
    
ans = solve()


# dp[0][0][2][0] = solve(0, 1, 2, 0) + int(M[0][0])
# dp[0][0][1][0] = solve(1, 0, 1, 0) + int(M[0][0]) 
# ans = solve(0, 0, 0, 0) - int(M[0][0])

print(ans)

