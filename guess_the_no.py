n=20
number_of_guesses=1
print("Number of guesses is limited to 9 times: ")
while (number_of_guesses<=9):
    guess_number=int(input("Guess the no :\n"))
    if guess_number<20:
        print("please input greater no:\n")
    elif guess_number>20:
        print("please enter less no:\n")
    else:
        print("you won\n")
        print (number_of_gueeses, "number of guesses he took to finish.")
        break
    print(9-number_of_guesses, "number of guesses left")
    number_of_guesses = number_of_guesses + 1
if(number_of_guesses>9):
    print("Game Over")