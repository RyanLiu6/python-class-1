def main():
    print(checkforXYZ("xyz"))


def square(n):
    if n is 0:
        return 0
    else:
        return square(n-1) + 2*n - 1


def removeVowel(str):
    if not str:
        return str
    elif str[0] in "aeiouAEIOU":
        return removeVowel(str[1:])
    return str[0] + removeVowel(str[1:])


def guessNum():
    low = 0
    high = 100
    currGuess = 50

    print("Please think of a number between " + str(low) + " and " + str(high))
    print("Is " + str(currGuess) + " your number?")
    userInput = input("Enter Y or N\n")

    while userInput is not "Y":
        userInput = input("Enter H for too high or L for too low\n")
        if userInput is "H":
            high = currGuess
        if userInput is "L":
            low = currGuess + 1

        currGuess = (low+high)//2
        print("Is " + str(currGuess) + " your number?")
        userInput = input("Enter Y or N\n")

    print("Your number is: " + str(currGuess))


def checkforXYZ(str):
    first = second = False
    if "xyz" in str:
        first = True

    # Check if character before xyz is a period
    pos = str.find("xyz")
    if str[pos-1] is ".":
        second = False
    else:
        second = True

    return first and second


if __name__ == "__main__":
    main()
