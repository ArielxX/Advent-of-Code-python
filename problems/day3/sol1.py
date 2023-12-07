line1 = '.' + input() + '.'
line0 = '.' * len(line1)
taken = set()

line_index = 1


def solve_line(line0, line1, line2):
    cur_num = ''
    ans = 0
    counting = False

    for i in range(1, len(line1)):
        if line1[i] == '.':
            if cur_num != '' and counting:
                ans += int(cur_num)

            cur_num = ''
            counting = False
            continue
        
        if line1[i].isdigit():
            cur_num += line1[i]

            if not counting:
                for j in range(-1, 2):
                    if line0[i+j] != '.' and not line0[i+j].isdigit():
                        counting = True
                        break
                    if line2[i+j] != '.' and not line2[i+j].isdigit():
                        counting = True
                        break
                

        else:
            if cur_num != '':
                ans += int(cur_num)

            counting = True
            cur_num = ''

    return ans


ans = 0

while True:
    try:
        line2 = '.' + input() + '.'
        
        ans += solve_line(line0, line1, line2)

        line0 = line1
        line1 = line2
            
    except EOFError:
        line2 = '.' * len(line1)
        ans += solve_line(line0, line1, line2)
        break


print(ans)