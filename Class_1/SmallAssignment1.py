def main():
    print("Hello")
    inputList = userInput()
    checkMenu(inputList)


def userInput():
    inputNum = []

    print("Hello, please enter a positive integer")
    currInput = input("Enter a number: ")
    inputNum.append(int(currInput))

    while currInput != "999":
        print(currInput)
        currInput = input("Enter a number: ")
        if currInput != "999":
            inputNum.append(int(currInput))

    print("We're done")

    return inputNum


def checkMenu(inputList):
    print("Choose average or max")
    print("Press 1 for average")
    print("Press 2 for maximum")
    currInput = input("")

    if currInput == "1":
        print(getAverage(inputList))
    if currInput == "2":
        print(getMaximum(inputList))


def getAverage(inputList):
    if len(inputList) == 0:
        return 999

    currSum = 0
    for num in inputList:
        currSum += num

    return currSum / len(inputList)


def getMaximum(inputList):
    if len(inputList) == 0:
        return 999

    max = -1
    for num in inputList:
        if num > max:
            max = num

    return max


if __name__ == "__main__":
    main()
