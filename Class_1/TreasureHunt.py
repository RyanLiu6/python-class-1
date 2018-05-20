import urllib.request

def main():
    print("Start of Treasure Hunt")
    controlPlayer(getInfo())


def getInfo():
    # Get information from website
    treasure = []
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/treasure.txt")
    html = response.readline().decode("utf-8")

    while len(html) > 0:
        try:
            treasure.append(int(html[:-1]))
        except:
            treasure.append(html[:-1])
        html = response.readline().decode("utf-8")

    return treasure


def controlPlayer(treasureList):
    # Control Player
    userPos = int(input("Where would you want to start? (Please Enter a Number)\n"))
    knapsack = {}
    numMoves = 0

    while userPos < len(treasureList):
        if isNumber(treasureList[userPos]):
            userPos = treasureList[userPos]
        else:
            # First, see if treasureList[userPos] exists
            # Second, if it does, get the value and increment by 1
            # If it doesn't, set knapsack[treasureList[userPos]] = 1
            knapsack[treasureList[userPos]] = knapsack.get(treasureList[userPos], 0) + 1

            # Ask user if they wish to continue
            print("Press 0 to quit and 1 to continue")
            userInput = input("")
            if userInput == "0":
                tallyScore(numMoves, knapsack)
                return
            elif userInput == "1":
                userPos = int(input("Please enter a new starting position.\n"))

        numMoves+=1

    tallyScore(numMoves, {})


def tallyScore(numMoves, knapsack):
    # Compute and return Score
    score = numMoves

    for item in knapsack:
        if item == "gold":
            score += 5
        elif item == "silver coins":
            score += 10
        elif item == "candy":
            score += 2
        elif item == "cell phone":
            score += 100

    print("You got: ")
    print(score)


def isNumber(a):
    # will be True also for 'NaN'
    try:
        number = float(a)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
