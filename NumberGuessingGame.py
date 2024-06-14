import random, time

print("---WELCOME TO NUMBER GUESSING GAME---".center(100))
print("---GUESS THE NUMBER BETWEEN 0 and 100 (in 10 Tries/Chances)---".center(100))

n = random.randint(1, 100)
print(n)


def main():
    guess = 1
    while (guess <= 10):
        print()
        time.sleep(1)
        print(f"You have {11 - guess} Tries Left!!\n")
        time.sleep(1)
        k = int(input(f"Guess the Target number:"))
        time.sleep(0.5)

        if (k == n):
            if (guess == 1):
                print("Wow..You are Just Awesome..!!")
                print(f'You Won the Game!!!')
                print(f"Your score:{(11 - guess) * 100}")
                break
            else:
                print(f'Congratulations....!!You Won the Game in {guess - 1} tries!!!')
                print(f"Your score:{(11 - guess) * 100}")
                break
        elif (k < n):
            print("Your guess the less than the Target Number!!\nTry Again Dude...")
        else:
            if (k > 100):
                print("You entered the number greater than 100..")
                print("Hey You...Please Guess the number between 0 and 100")
            else:
                print("Your guess the Greater than the Target Number!!\nTry Again Dude...")
        guess += 1
    else:
        print("No Tries...Left!!\nSORRY\nYou lost the game....")
        print(f"The Target number is {n}")


if __name__ == "__main__":
    main()