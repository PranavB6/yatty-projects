def main():

    # Setup variables before the while loop

    lives_left = 5
    letters_guessed = []
    secret_word_guessed = False

    secret_word = pick_secret_word()

    print_current_game_state(lives_left, secret_word, letters_guessed)

    while lives_left > 0 and not secret_word_guessed:
        # get the users input
        # validate the users input
        # update variables

        print_current_game_state(lives_left, secret_word, letters_guessed)

        # show some message

    # check if they won or lost and print out the appropriate response

    return


# Return a word
def pick_secret_word():

    pass


def print_current_game_state(lives_left, secret_word, letters_guessed):
    # sue the function parameters to print somthing like this:
    # ❤❤❤❤| _ a _ _ _ _
    # -ae-
    pass


main()
