ans = 0

class BIT:
    # binary indexed tree
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    # _update from index until the end
    def _update(self, index, x):
        while index <= self.n:
            self.tree[index] += x
            index += index & (-index)

    # update sum x to interval [l, r]
    def update(self, l, r, x):
        self._update(l, x)
        self._update(r + 1, -x)

    # get value in a single index
    def get(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & (-index)
        return res

bit = BIT(300)
index = 1

while True:
    try:
        amount = bit.get(index) + 1

        line = input()

        game = line.split(':')[1].split('|')

        card = game[0].split()
        numbers = game[1].split()

        points = 0

        for num in numbers:
            if num in card:
                points += 1

        ans += amount
        
        if points:
            # update from  index + 1 to index + points the value of amount
            bit.update(index + 1, index + points, amount)

        index += 1
        
    except EOFError:
        break


print(ans)
