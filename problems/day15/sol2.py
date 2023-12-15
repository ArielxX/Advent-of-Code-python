L = input().split(',')

def hash(s):
    sm = 0
    for x in s:
        sm += ord(x)
        sm *= 17
        sm %= 256
    return sm

M = {}
Boxes = [[] for i in range(256)]


for s in L:
    add = True
    if s[-1] == '-':
        ss = s[:-1]
        add = False
    else:
        s = s.split('=')
        ss = s[0]
        lens = int(s[1])
    
    if ss not in M:
        M[ss] = hash(ss)

    box = M[ss]
    if add:
        found = False
        for x in Boxes[box]:
            if x[0] == ss:
                x[1] = lens
                found = True
                break
        if not found:
            Boxes[box].append([ss, lens])
    else:
        for x in Boxes[box]:
            if x[0] == ss:
                Boxes[box].remove(x)
                break

ans = 0

for i in range(len(Boxes)):
    for j in range(len(Boxes[i])):
        ans += (i + 1) * (j + 1) * Boxes[i][j][1]

print(ans)