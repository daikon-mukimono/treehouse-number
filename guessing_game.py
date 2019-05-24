###guessing game version 800 (Python WebDev TechDegree)
import random

#init global vars
low_score       = 1000
play_counts     = 0

def start_game():
    """Pseudo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    #access globals
    global low_score
    global play_counts
    play_counts += 1
    guess_count = 0
    guess = 0
    game_over = False

    #get secret numbers
    secret_number = random.randrange(100)+1 #range starts at 1 and goes to 100

    #INTRO MESSAGE
    print("Welcome to the number guessing game!\nHow many tries will it take you to guess a number between 1 and 100?")
    if play_counts > 1:
        print("The score to beat is {}".format(low_score))
    while game_over == False:  
        try:
            #possible errors: ValueError, NameError
            guess = int(input("Enter your guess!\n>"))
            if guess < 1 or guess > 100:
                raise ValueError
        except NameError:
            print("Please enter a number between 1 and 100!!")     
        except ValueError:
            print("Enter a number between 1 and 100!")
        else:
            print("Your guess was " + str(guess))
            guess_count += 1
            print("You have guessed {} times".format(guess_count))
            if secret_number > guess:
                print("The number I'm thinking of is higher. Guess again!")
            elif secret_number < guess:
                print("The number I'm thinking of is lower. Guess again!")
            else:
                print("You win! You guessed in {} tries\n".format(guess_count))
                
                game_over = True;
                if guess_count < low_score:
                    low_score = guess_count
                    print("It's a new record!")
                
                play_again = input("Enter Y to play again, any other key to quit.\n")
                if play_again.lower() == "y":
                    start_game()
                else:
                    print("You have chosen to exit the game. Goodbye!")



if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()