line = input()
line = line.split(':')[1].split()
line = [int(x) for x in line]
seeds = []
for i in range(0, len(line), 2):
    seeds.append([line[i], line[i] + line[i + 1] - 1])
input()

def change(seeds, maps):
    new_seeds = []

    seeds = sorted(seeds)

    # sort the maps for the 2nd element
    maps = sorted(maps, key=lambda x: x[1])

    cur = 0

    for map in maps:
        while cur < len(seeds) and seeds[cur][1] < map[1]:
            new_seeds.append(seeds[cur])
            cur += 1

        if cur < len(seeds) and seeds[cur][0] < map[1]:
            new_seeds.append([seeds[cur][0], map[1] - 1])
            seeds[cur][0] = map[1]

        while cur < len(seeds) and seeds[cur][1] < map[1] + map[2]:
            new_seeds.append([map[0] + seeds[cur][0] - map[1], map[0] + seeds[cur][1] - map[1]])
            cur += 1

        if cur < len(seeds) and seeds[cur][0] < map[1] + map[2]:
            new_seeds.append([map[0] + seeds[cur][0] - map[1], map[0] + map[2] - 1])
            seeds[cur][0] = map[1] + map[2]

    while cur < len(seeds):
        new_seeds.append(seeds[cur])
        cur += 1

    return new_seeds


while True:
    try:
        line = input()
        maps = []
        while True:            
            line = input()
            if line == '':
                break
            map = line.split()
            map = [int(x) for x in map]
            maps.append(map)

        seeds = change(seeds, maps)

    except EOFError:
        break

print(min(seeds))