import random

WinningNumber = random.randint(1,100)

Guesses = 0

while True:
    Guesses += 1
    UserGuess = int(input("Enter Your Guess : "))
    if UserGuess == WinningNumber:
        print("You Win!")
        print(f"You guessed the number in {Guesses} guesses")
        with open("score.txt", "r") as f:
            score = int(f.read())
        if score == 0 or Guesses < score:
            with open("score.txt", "w") as f:
                f.write(str(Guesses))
        break
    elif UserGuess < WinningNumber:
        print("Too Low")
    else:
        print("Too High")
