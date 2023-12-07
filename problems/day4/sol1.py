ans = 0

while True:
    try:
        line = input()

        game = line.split(':')[1].split('|')

        card = game[0].split()
        numbers = game[1].split()

        points = 0

        for num in numbers:
            if num in card:
                points += 1

        if points:
            ans += 2**(points - 1)
        
    except EOFError:
        break

print(ans)
