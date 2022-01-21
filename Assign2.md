# Assignment 2 - Hangman Dangman

Due: Feb 04, 2021 11:59pm (hand in on discord)

## Purpose

The purpose of this assignment is to get you more comfortable with thinking like a programmer - working with lists, loops and functions

## Description

Create a hangman game in the terminal. At the start of the game, the computer picks a secret word from a list and shows how many letters the word has in the terminal. 

On each turn the user guess a letter. If the letter is part of the secret word, then the computer reveals the part(s) of the word that contain that letter. If the letter that the user guessed is not a part of the word, then they lose a life. The user starts out with 5 lives.

At the end of the game, if they guess all of the letters of the word without losing all of their lives, they win! On the other hand, if they lose all of their lives before they guess all of the letters, they lose.

## Other Rules 

* Invalid user input
  * If the user enters invalid input, then it doesn't count as a turn (they don't lose any lives)
  * Invalid input includes:
    * More than one letter
    * A letter that they already guessed
    * anything other than letters (ie numbers, symbols)
* No global variables allowed
* The only external library you need is `random`
  * Use `random.choice(list)` to randomly select an item from a list: [Link](https://stackoverflow.com/questions/306400/how-can-i-randomly-select-an-item-from-a-list)

### Tips

* How to print a heart: `print("\u2764")` will print `❤`
* How to print on the same line:

```py
# Code:
print("--")
print("-->")

# Output:
--
-->
```

```py
# Code:
print("--", end="")
print("-->")

# Output:
---->
```

```py
# Code:
print("--", end="abc")
print("-->")

# Output:
--abc-->

# This means that by default, end="\n"
```

## Example
You output should look like this:

```bash
> python3 main.py

Welcome to Hangman Dangman!

❤❤❤❤❤| _ _ _ _ _ _

Lets start the game!

Guess a letter: 'a' 
# the user just entered the letter a, I'm just using the ' symbol to show that its the user's input


❤❤❤❤❤| _ a _ _ _ _
-a-
Good job! letter a is there!

Guess a letter: 'e'


❤❤❤❤| _ a _ _ _ _
-ae-
There is no letter e!

Guess a letter: 't'


❤❤❤❤| _ a t _ _ _
-aet-
Good job! letter t is there!

Guess a letter: 'e'


❤❤❤❤| _ a t _ _ _
-aet-
You already tried letter e! Guess again!

Guess a letter: 'ascsa'


❤❤❤❤| _ a t _ _ _
-aet-
Invalid input, please enter a single valid letter!

Guess a letter: '5'


❤❤❤❤| _ a t _ _ _
-aet-
Invalid input, please enter a single valid letter!

Guess a letter: 'y'


❤❤❤❤| y a t _ _ _
-aety-
Good job! letter y is there!

Guess a letter: 'r'


❤❤❤❤| y a t r _ _
-aetyr-
Good job! letter r is there!

Guess a letter: 'i'


❤❤❤❤| y a t r i _
-aetyri-
Good job! letter i is there!

Guess a letter: 'k'


❤❤❤❤| y a t r i k
-aetyrik-
Good job! letter k is there!

Congratulations! You got it!
```

Here is an example of what should happen if a player loses:

```
❤| _ a t _ _ _
-aetqwu-
There is no letter u!

Guess a letter: 'b'


| _ a t _ _ _
-aetqwu-
There is no letter b!

You're out of lives! You lose!!!
```