line1 = '.' + input() + '.'
line0 = '.' * len(line1)
taken = set()

line_index = 1

M = {}

def solve_line(line0, line1, line2, M, index):
    cur_num = ''
    counting = set()

    for i in range(1, len(line1)):
        if line1[i] == '.':
            if cur_num != '':
                for c in counting:
                    if c not in M:
                        M[c] = []
                    M[c].append(int(cur_num))

            cur_num = ''
            counting = set()
            continue
        
        if line1[i].isdigit():
            cur_num += line1[i]
            for j in range(i - 1, i + 2):
                if line0[j] == '*':
                    counting.add((index - 1, j))
                if line2[j] == '*':
                    counting.add((index + 1, j))

        elif line1[i] == '*':
            if cur_num != '':
                counting.add((index, i))
                for c in counting:
                    if c not in M:
                        M[c] = []
                    M[c].append(int(cur_num))

            counting = set()
            counting.add((index, i))
            cur_num = ''


while True:
    try:
        line2 = '.' + input() + '.'
        
        solve_line(line0, line1, line2, M, line_index)

        line0 = line1
        line1 = line2
        line_index += 1

    except EOFError:
        line2 = '.' * len(line1)
        solve_line(line0, line1, line2, M, line_index)
        break

ans = 0

for k in M:
    if len(M[k]) == 2:
        ans += M[k][0] * M[k][1]

print(ans)