ans = 0

while True:
    try:
        line = input()

        numbers = ''

        for x in line:
            if x.isdigit():
                numbers += x

        if numbers != '':
            ans += 10*int(numbers[0]) + int(numbers[-1])

    except EOFError:
        break

print(ans)