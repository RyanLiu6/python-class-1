import random
import string
from datetime import datetime


class Puzzle:
    def __init__(self):
        self._prepPuz()
        self._setPuz()

        self.p1 = input("Enter Player 1's name: ")
        self.p1Bank = 0
        self.p2 = input("Enter Player 2's name: ")
        self.p2Bank = 0
        self.turnBank = 0

        self.gameDone = False

        self.currGuess = []
        for i in range(len(self.currPuz[1])):
            self.currGuess.append("_")

        self.guessedChar = []

        self.alphabet = list(string.ascii_lowercase)
        self.vowel = ["a", "e", "i", "o", "u"]
        self.freqMap = [1]*26

    def _prepPuz(self):
        # Remember to turn everything to lowercase
        self.puzList = []
        # For now, we just have 3 secret words
        # self.puzList.append(("university", "queen's"))
        # self.puzList.append(("city", "kingston"))
        self.puzList.append(("city", "vancouver"))

    def _setPuz(self):
        n = len(self.puzList)
        random.seed(datetime.now())
        randNum = random.randint(0, n - 1)

        self.currPuz = self.puzList[randNum]

    def playGame(self):
        self.playerID = 0

        while not self.gameDone:
            print("___________________________________________________________")
            self.updateScreen()
            # Print options
            print("Options: (Please enter the number) ")
            print("1. quit the game")
            print("2. solve the puzzle")
            print("3. spin the wheel")
            userInput = input("4. buy a vowel\n")

            if userInput == "1":
                break
            elif userInput == "2":
                self.solvePuz()
            elif userInput == "3":
                self.spinWheel()
            else:
                self.buyVowel()

    def updateScreen(self):
        # Print Players
        if self.playerID == 0:
            print(self.p1 + "'s turn")
            # Print P1's money
        else:
            print(self.p2 + "'s turn")
            # Print P2's money
        self.playerID = (self.playerID + 1) % 2

        self.printHang()

    def solvePuz(self):
        userInput = input("Enter your guess for the secret word: ").lower()

        if userInput == self.currPuz[1]:
            # Grant money and end puzzle
            self.identifyWinner()

        # Remember to continue turn
        self.keepTurn()

    def spinWheel(self):
        wheelNum = random.randint(0, 21)
        if wheelNum == 0:
            # Change player turn money to 0
            return
        elif wheelNum == 21:
            return
        else:
            # Error check for consonant
            userInput = input("Enter a consonant: ").lower()
            while userInput in self.vowel:
                userInput = input("Enter a consonant, not vowel: ").lower()

            self.freqMap[ord(userInput) - 97]-=1
            self.guessedChar.append(userInput)

            # check if userInput is in secret word
            if userInput in self.currPuz[1]:
                for i in range(len(self.currGuess)):
                    if self.currPuz[1][i] == userInput:
                        self.currGuess[i] = userInput

                # Add money to bank
                print("You found a character!")
                userInput = input("Would you like to spin again? Y/N ")
                if userInput == "N":
                    return
                else:
                    self.keepTurn()
                    self.printHang()
                    self.spinWheel()
            else:
                # Deduct wheelNum from bank
                print("Deducting money")

    def buyVowel(self):
        userInput = input("Which vowel would you like to purchase? ").lower()
        while userInput not in self.vowel:
            userInput = input("Enter a vowel. ").lower()

        # check if userInput is in secret word
        if userInput in self.currPuz[1]:
            for i in range(len(self.currGuess)):
                if self.currPuz[1][i] == userInput:
                    self.currGuess[i] = userInput

            # Remember to continue turn
            self.keepTurn()

        # Remove $25 and update list of characters
        self.freqMap[ord(userInput) - 97]-=1
        self.guessedChar.append(userInput)

    def identifyWinner(self):
        if self.p1Bank > self.p2Bank:
            print(self.p1 + " is the winner!")
        else:
            print(self.p2 + " is the winner!")

        self.gameDone = True

    def keepTurn(self):
        currPlayer = self.playerID - 1
        self.playerID = currPlayer % 2

    def printHang(self):
        # Print state of game
        print("Category: " + self.currPuz[0], end="")
        print("                       ", end="")
        print("Secret Word: ", end="")
        for i in range(len(self.currGuess)):
            print(self.currGuess[i] + " ", end="")
        print()

        print("Guessed Letter: ", end="")
        for guess in self.guessedChar:
            print(guess + " ", end="")
        print()

        print("Available Letters: ", end="")
        for i in range(len(self.freqMap)):
            if self.freqMap[i] > 0:
                print(self.alphabet[i] + " ", end="")
            else:
                print("* ", end="")
        print()

def main():
    print("You are playing with a human friend")
    puz = Puzzle()
    puz.playGame()


if __name__ == "__main__":
    main()
