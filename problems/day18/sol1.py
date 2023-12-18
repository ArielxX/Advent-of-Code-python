
x = 0
y = 0

M = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

L = [[x,y]]

p = 0

def convert_hexadecimal2decimal(s):
    return int(s, 16)


while True:
    try:
        line = input().split()
        dir = line[0]
        cnt = int(line[1])
        color = line[2]

        cnt = int(color[2:7], 16)
        dir = 'RDLU'[int(color[-2])]


        p += cnt

        (dx, dy) = M[dir]


        x += dx * cnt
        y += dy * cnt

        if (x,y) != (0,0):
            L.append([x,y])

    except EOFError:
        break

# calculate the area of the polygon
    
    
area = 0
for i in range(len(L)):
    area += (L[i][0] + L[(i+1) % len(L)][0]) * (L[i][1] - L[(i+1) % len(L)][1])


area = abs(area) / 2 + p / 2 + 1

print(area)
