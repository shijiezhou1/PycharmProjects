import random


class GuessGame:

    def __init__(self, min, max):
        self.showGameRule(min, max)
        self.randomnum = random.randint(min, max)

    def showGameRule(self, min, max):
        print("Guess number between " + str(min) +  " - " + str(max))

    # def randomnumbergenerator(self):
    # return random.randint(1, 100)


def main():
    randomnumber = GuessGame(1, 100);
    randomnumber = randomnumber.randomnum
    found = False  # flag variable to see

    while not found:
        userGuess = input("Your Guess: ")

        if int(userGuess) == randomnumber:
            print("You got it")
            found = True
        elif int(userGuess) > randomnumber:
            print("Guess lower!")
        else:
            print("Guess higher!")


if __name__ == "__main__":
    main()
