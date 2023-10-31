import random

#asks the user if they want to play and initializes game if yes
play_time = input("Are you ready to play (Y or N): ")
play_time = play_time.upper()
game_on = None

#function to run the guessing 
def guessing_game():

    #initialize a random number as the answer
    answer = random.randint(1, 20)
    
    #Creats a while loop giving the player 4 guesses and upon a correct guess or runs out of guesses ends the game
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

#creates a function to allow the user to keep playing or quit after playing 1 or more times
def playing ():
    keep_playing = input("Do you want to play again (Y or N)? ")
    keep_playing = keep_playing.upper()
    if keep_playing == "N":
        print("Goodbye")
        quit()    

#initializes the game for the first run
if play_time == "Y":
    game_on = True
else:
    game_on = False

#runs the game by calling the game function and keeps game going by calling the playing function    
while game_on != False:
    guessing_game()
    playing()

#If the player doesn't want to keep playing, this quits the game
print("Goodbye!")
quit()
