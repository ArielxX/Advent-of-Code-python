times = input().split(':')[1].split()
times = [int(x) for x in times]
distances = input().split(':')[1].split()
distances = [int(x) for x in distances]

ans = 1

for tm, ds in zip(times, distances):
    bg = 0
    for i in range(int(tm)):
        if (tm - i) * i > ds:
            bg = i
            break

    end = tm
    for i in range(int(tm), 0, -1):
        if (tm - i) * i > ds:
            end = i
            break

    cur = max(0, end - bg + 1)

    ans *= cur

print(ans)