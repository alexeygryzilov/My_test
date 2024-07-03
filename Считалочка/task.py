def counting_rhyme(people: int, trigger: int) ->int:

    players = [i for i in range(1, people + 1)]
    idx = 0

    while len(players) > 1:
        for _ in range(trigger):
            if idx == len(players):
                idx = 0
            idx += 1
        idx -= 1
        del players[idx]
    return players[0]

if __name__ == '__main__':

    print(counting_rhyme(10, 4))  #5