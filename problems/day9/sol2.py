ans = 0

def solve(L):
    diff = [L[i] - L[i - 1] for i in range(1, len(L))]
    if diff[-1] == 0:
        return L[0]
    
    return L[0] - solve(diff)
    


while True:
    try:
        line = input().split()
        line = [int(x) for x in line]
        ans += solve(line)
        
    except EOFError:
        break

print(ans)