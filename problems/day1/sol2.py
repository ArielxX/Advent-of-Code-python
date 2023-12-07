M = {}

M['one'] = 1
M['two'] = 2
M['three'] = 3
M['four'] = 4
M['five'] = 5
M['six'] = 6
M['seven'] = 7
M['eight'] = 8
M['nine'] = 9

ans = 0

while True:
    try:
        line = input()

        first = ''

        for i in range(len(line)):
            if line[i].isdigit():
                first = line[i]
                break
            
            for k in M:
                if i + len(k) <= len(line) and line[i:i+len(k)] == k:
                    first = M[k]
                    break

            if first != '':
                break


        last = ''

        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                last = line[i]
                break
            
            for k in M:
                if i + len(k) <= len(line) and line[i:i+len(k)] == k:
                    last = M[k]
                    break  

            if last != '':
                break             

        ans += int(first) * 10 + int(last)

    except EOFError:
        break

print(ans)