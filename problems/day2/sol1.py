ans = 0

while True:
    try:
        line = input()
        line = line.split(':')
        id = line[0].split()[1]

        M = {}
        M['red'] = 0
        M['green'] = 0
        M['blue'] = 0

        games = line[1].split(';')

        for game in games:
            game = game.split(',')
            
            for cubes in game:
                color = cubes.split()[1]
                cant = int(cubes.split()[0])

                M[color] = max(M[color], cant)

        if M['red'] <= 12 and M['green'] <= 13 and M['blue'] <= 14:
            ans += int(id)

    except EOFError:
        break

print(ans)