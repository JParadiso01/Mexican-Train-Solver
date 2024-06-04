#global variables
possible_trains = list(list())
longest_trains = list(list())

def main():
    #get dominoes and starter
    dominoes = list(list())
    length = int(input("How many dominoes do you have? "))
    for i in range(length):
        dominoes.append([int(input(f"Domino {i+1}: What is the top number? ")), int(input(f"Domino {i+1}: What is the bottom number? "))])

    start = int(input("What is the starting number? "))

    #figure out which dominoes can be possible starter pieces
    starters = list(list())
    for d in dominoes:
        if (d[0] == start):
            starters.append(d)
        elif d[1] == start:
            #rotates domino
            d[1], d[0] = d[0], d[1]
            starters.append(d)
    
    if starters == []:
        print("You do not have any starters.\nYou cannot start a train :(")
        exit(0)
    
    #print("Starter Candidates: ")
    #print(starters)
    #print()

    #go thorugh starters and find longest train
    for s in starters:
        t = list()
        t.append(s)
        d = dominoes.copy()
        d.remove(s)
        #print(f"Starter: {s}")
        solve(d, t)
        #print('---------------')

    max = 0
    for t in possible_trains:
        if len(t) >= max:
            max = len(t)

    for t in possible_trains:
        if len(t) == max:
            longest_trains.append(t)
    if (len(longest_trains) == 1):
        print(f"\nThis the longest train:\n{longest_trains}")
    else:
        print(f'\nThese are the longest possible trains:')
        for t in longest_trains:
            print(t)

#recursively check for longest train
def solve(dominoes, train):
    #print('---------------')
    #print(f"  Dominos Left: {dominoes}")
    #print(f"  Train: {train}")

    if dominoes == []:
        return train
    
    connector = train[len(train)-1]
    for d in dominoes:
        
        if CheckIfConnects(d, connector):
            t_c = train.copy()
            d_c = dominoes.copy()
            t_c.append(d)
            d_c.remove(d)
            possible_trains.append(solve(d_c, t_c))
    return train


def CheckIfConnects(d1, d2):
    if (d1[0] == d2[1]):
        return True
    elif (d1[1] == d2[1]):
        # rotates domino if needed
        d1[1], d1[0] = d1[0], d1[1]
        return True
    else:
        return False
    

if __name__ == '__main__':
    main()