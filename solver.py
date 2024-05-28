def main():
    dominoes = list(list())
    length = int(input("How many dominoes do you have? "))
    for i in range(length):
        dominoes.append([int(input(f"Domino {i+1}: What is the top number? ")), int(input(f"Domino {i+1}: What is the bottom number? "))])

    start = int(input("What is the starting number? "))

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
    
    print("Starter Candidates: ")
    print(starters)
    print()

    train = list(list())
    for s in starters:
        t = list()
        t.append(s)
        d = dominoes.copy()
        d.remove(s)
        print(f"Starter: {s}")
        possible_train = solve(d, t, length-1)
        print('---------------')
        print(f"  Possible Train: {possible_train}")
        if len(possible_train) >= len(train):
            train = possible_train.copy()

    print(f"This is the longest train:\n{train}")


#TODO: make it so the program checks all possible connections instead of just the first one
def solve(dominoes, train, domLen):
    print('---------------')
    print(f"  Dominos Left: {dominoes}")
    print(f"  Train: {train}")

    if dominoes == []:
        return train
    
    for d in dominoes:
        if CheckIfConnects(d, train[len(train)-1]):
            train.append(d)
            dominoes.remove(train[len(train)-1])
            solve(dominoes, train, len(dominoes))
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