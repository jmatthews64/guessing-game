import random


play_time = input("Are you ready to play (Y or N): ")
play_time = play_time.upper()
game_on = None

def guessing_game():
    answer = random.randint(1, 20)
    print(answer)
    count = 4
    while count > 0:
        print("You have ", count, "guesses remaining.")
        guess = int(input("Guess a number between 1 and 20: "))
        if guess == answer:
            print("Congrats!  You win!")
            break
        elif guess < answer:
            print("Too low")
        else:
            print("Too high")
        count -= 1
    print("Game over.  The correct answer was: ", answer)

def playing ():
    keep_playing = input("Do you want to play again (Y or N)? ")
    keep_playing = keep_playing.upper()
    if keep_playing == "N":
        print("Goodbye")
        quit()    

if play_time == "Y":
    game_on = True
else:
    game_on = False
    
while game_on != False:
    guessing_game()
    playing()

print("Goodbye!")
quit()
