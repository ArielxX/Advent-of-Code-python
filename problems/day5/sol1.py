line = input()
seeds = line.split(':')[1].split()
input()
seeds = [int(x) for x in seeds]

def change(seeds, maps):
    new_seeds = []

    seeds = sorted(seeds)

    # sort the maps for the 2nd element
    maps = sorted(maps, key=lambda x: x[1])

    cur = 0

    for map in maps:
        while cur < len(seeds) and seeds[cur] < map[1]:
            new_seeds.append(seeds[cur])
            cur += 1

        while cur < len(seeds) and seeds[cur] < map[1] + map[2]:
            new_seeds.append(map[0] + seeds[cur] - map[1])
            cur += 1

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