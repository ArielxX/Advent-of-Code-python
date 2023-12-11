M = []

rows = []
cols = []

idx = 0

while True:
    try:
        M.append(input())
        for j in range(len(M[-1])):
            if M[-1][j] == '#':
                cols.append(j)
                rows.append(idx)
        idx += 1
    except EOFError:
        break

# check the columns full of .

col_2 = [0 for i in range(len(M[0]))]

for j in range(len(M[0])):
    if j:
        col_2[j] = col_2[j - 1]
    col_2[j] += 1
    flag = True
    for i in range(len(M)):
        if M[i][j] != '.':
            flag = False
            break
    if flag:
        col_2[j] += 1000000 - 1

# check the rows full of .

row_2 = [0 for i in range(len(M))]

for i in range(len(M)):
    if i:
        row_2[i] = row_2[i - 1]
    row_2[i] += 1
    flag = True
    for j in range(len(M[0])):
        if M[i][j] != '.':
            flag = False
            break
    if flag:
        row_2[i] += 1000000 - 1

rows.sort()
cols.sort()

ans = 0

n = len(rows)

for i in range(len(rows)):
    ans += row_2[rows[i]] * (2*i - n + 1)

for j in range(len(cols)):
    ans += col_2[cols[j]] * (2*j - n + 1)

print(ans)