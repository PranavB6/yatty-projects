def main():

    # Setup variables before the while loop
    # I have already setup these 4 variables, you may want to setup more
    lives_left = 5
    letters_guessed = []
    secret_word_guessed = False
    secret_word = pick_secret_word()

    print_current_game_state(lives_left, secret_word, letters_guessed)

    while lives_left > 0 and not secret_word_guessed:
        # Write code here!
        # Get the users input
        # Validate the users input
        # Update variables like letters_guessed

        print_current_game_state(lives_left, secret_word, letters_guessed)
        
        # If the input was invalid, print "Invalid input, please enter a single valid letter!"
        # Otherwise, was the letter they picked in the secret word? If so then print a message like "Good job! letter a is there!" or if it wasn't then print something like "There is no letter e!"
        

    # If this part of the code is reached, then they either won or lost
    # Check if they won or lost and print out the appropriate response
    
    return


def pick_secret_word():
    """ Randomly pick a secret word from a list
    
    Create a list of words from which the secret word will be chosen. Use the 'random' library to randomly choose a word from that list.
    
    :return: A string that is the secret word. ie "yatrik"    
    """
    
    return


def print_current_game_state(lives_left, secret_word, letters_guessed):
    """ Print the current game state
   
    ❤❤❤❤| _ a _ _ _ _
    -ae-
    
    The number of hearts is the number of lives they have left.
    
    Every '_' is one letter in the secret word. If the user has already guessed a particular letter, then show the actual letter instead of '_'. 
    So for example if the secret word is 'eleven' and the user already guessed 'e' then show 'e _ e _ e _'.
    
    The letters at the bottom are the letters they already guessed. ie if the letters guessed was ["a", "b", "c"] then show '- abc -'    
    
    :param lives_left: How many lives the user has left
    :param secret_word: The secret_word as a string. ie "yatrik" 
    :param letters_guessed: A list of all the letters the user has already guessed. ie ["a", "e"]
    :return: Nothing
    """

    return


main()
