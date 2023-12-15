ans = 0

L = input().split(',')

for s in L:
    sm = 0
    for x in s:
        sm += ord(x)
        sm *= 17
        sm %= 256
    ans += sm
    print(sm)

print(ans)