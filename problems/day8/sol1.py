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
        
    except EOFError:
        break

cur = get_value('AAA')

end = get_value('ZZZ')

while cur != end:
    com = commands[index % len(commands)]
    if com == 'L':
        cur = M[cur][0]
    else:
        cur = M[cur][1]

    index += 1

print(index)