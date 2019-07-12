import random

def main():
    print("guess between 1-100")
    randomnumber = random.randint(1, 100);
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
