ans = 0


def solve(board, nums, acc, i, pos, dp):
    if pos == len(nums):
        # check there is not any '#' left in board from i to end
        for j in range(i, len(board)):
            if board[j] == '#':
                return 0
        return 1

    if i == len(board):
        return acc == nums[pos] and pos == len(nums) - 1
    
    if dp[acc][i][pos] != -1:
        return dp[acc][i][pos]
    
    if board[i] == '#':
        acc += 1
        if acc > nums[pos]:
            dp[acc][i][pos] = 0
            return 0
        dp[acc][i][pos] = solve(board, nums, acc, i+1, pos, dp)
    elif board[i] == '.':
        if acc > 0:
            if acc != nums[pos]:
                dp[acc][i][pos] = 0
            else:
                dp[acc][i][pos] = solve(board, nums, 0, i+1, pos+1, dp)
        else:
            dp[acc][i][pos] = solve(board, nums, 0, i+1, pos, dp)
    # board[i] == '?'
    else:
        if acc > 0:
            if acc == nums[pos]:
                # check if the next char is '.'
                dp[acc][i][pos] = solve(board, nums, 0, i+1, pos+1, dp)
            else:
                if acc + 1 == nums[pos]:
                    if i + 1 < len(board) and board[i+1] != '#':
                        dp[acc][i][pos] = solve(board, nums, 0, i+2, pos+1, dp)
                    else:
                        dp[acc][i][pos] = solve(board, nums, acc+1, i+1, pos, dp)
                else:
                    dp[acc][i][pos] = solve(board, nums, acc + 1, i+1, pos, dp)
        else:
            dp[acc][i][pos] = solve(board, nums, 1, i+1, pos, dp) + solve(board, nums, 0, i+1, pos, dp)
    
    return dp[acc][i][pos]

while True:
    try:
        line = input().split()

        board = line[0]
        # concat board 5 times with a '?' in between
        board = board + '?' + board + '?' + board + '?' + board + '?' + board
        nums = line[1].split(',')
        nums = [int(x) for x in nums]
        # concat nums 5 times
        nums = nums + nums + nums + nums + nums

        dp = [[[-1 for _ in range(len(nums) + 1)] for _ in range(len(board) + 1)] for _ in range(max(nums) + 2)]

        cur = solve(board, nums, 0, 0, 0, dp)
        ans += cur
    except EOFError:
        break

print(ans)
