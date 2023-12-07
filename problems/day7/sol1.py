from functools import cmp_to_key

games = []

while True:
    try:
        game = input().split()
        # a game has a 5 str elemnt as cards and points
        games.append(game)
    except EOFError:
        break

def get_type(cards):
    M = {}
    for card in cards:
        if not card in M:
            M[card] = 1
        else:
            M[card] += 1

    L = []

    for card in M:
        L.append(M[card])

    L.sort()
    L = L[::-1]

    if len(L) == 1:
        return 1
    elif L[0] == 4:
        return 2
    elif L[0] == 3 and L[1] == 2:
        return 3
    elif L[0] == 3:
        return 4
    elif L[0] == 2 and L[1] == 2:
        return 5
    elif L[0] == 2:
        return 6
    else:
        return 7

order = '23456789TJQKA'

def compare2cards(card1, card2):
    return order.index(card1) > order.index(card2)


def srt(game1, game2):
    type1 = get_type(game1[0])
    type2 = get_type(game2[0])

    if type1 < type2:
        return -1
    elif type1 > type2:
        return 1
    else:
        for i in range(5):
            if game1[0][i] != game2[0][i]:
                if compare2cards(game1[0][i], game2[0][i]):
                    return -1
                else:
                    return 1
    return 0
                

# sort all games 
games.sort(key=cmp_to_key(srt))
# reverse the list
games = games[::-1]

ans = 0

for i in range(len(games)):
    ans += (i + 1) * int(games[i][1])

print(ans)
