ans_h = 0
ans_v = 0

M = []

def solve_H(M):
    for i in range(len(M) - 2, -1, -1):
        ln = min(i + 1, len(M) - i - 1)
        A = M[i - ln + 1:i + 1]
        B = M[i + 1:i + ln + 1]
        B.reverse()
        # check if the difference between every element in the two lists is exactly 1
        diff = 0
        for j in range(len(A)):
            diff += sum([1 if A[j][k] != B[j][k] else 0 for k in range(len(A[j]))])
            
            if diff > 1:
                break
        if diff == 1:
            return i + 1
    return 0


def solve(M):
    global ans_h, ans_v

    ans_h += solve_H(M)
    ans_v += solve_H(list(zip(*M)))
    

while True:
    try:
        line = input()
        if line == '':
            solve(M)
            M = []
        else:
            M.append(line)
    except EOFError:
        break

solve(M)

print(100 * ans_h + ans_v)

