commands = input()
input()

index = 0

M = {}
mp = {}

def get_value(x):
    if x in mp:
        return mp[x]
    mp[x] = len(mp)
    return mp[x]

def get_cycle_length(start, end):
    cur = start
    cnt = 0

    while True:
        com = commands[cnt % len(commands)]
        cnt += 1
        if com == 'L':
            cur = M[cur][0]
        else:
            cur = M[cur][1]

        if cur in end and cur != start:
            print('Found it another ending node', cur, cnt)

        if cur == start:
            return cnt

start = []
end = set()

while True:
    try:
        line = input()
        line = line.split(' = ')
        name = line[0]
        id = get_value(name)
        values = line[1][1:-1].split(', ')
        val1 = get_value(values[0])
        val2 = get_value(values[1])

        M[id] = (val1, val2)

        if name[-1] == 'A':
            start.append(id)
        
        if name[-1] == 'Z':
            end.add(id)
        
    except EOFError:
        break


cnt = 0
steps = []

for x in start:
    cur = x
    cnt = 0

    while True:
        com = commands[cnt % len(commands)]
        cnt += 1
        if com == 'L':
            cur = M[cur][0]
        else:
            cur = M[cur][1]

        if cur in end:
            # For every start node we can see that the cycle length of the corresponding
            # end node is the same that amount of steps we need to reach it.
            # Also we can check that this cycle doesn't contain any other end nodes.
            # So we can just calculate the cycle length of every start node and get the
            # least common multiple of all of them.
        
            print(x, cnt, get_cycle_length(cur, end))

            break
    
    steps.append(cnt)

# get lcm of all steps
from math import gcd
ans = steps[0]
for x in steps[1:]:
    ans = ans * x // gcd(ans, x)


print(ans)