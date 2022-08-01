secretNumber = 5
guessLimit = 0
maxGuess = 3

while guessLimit < maxGuess:
    guess = int(input('guess: '))
    guessLimit += 1
    if guess == secretNumber:
        print('you won...!!!')
        break
else:
    print('sorry you failed')
