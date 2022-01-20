score = 0  # setting value for score


def t_score():  # function to do score addition
    global score
    score = score + 1
    return score


print("Welcome to Quizzer 9000. \nToday you will be faced with 8 questions.")
print("At the end of the quiz your score will be talied ")

# TF question 1
print("Section 1. True or False \nQuestion 1) Pranav has a job at Telus.")
answer = input().upper()
if answer == "TRUE" or answer == "T":
    t_score()

# TF question 2
print("Question 2) Valorant is a FPS game that we play.")
answer = input().upper()
if answer == "True" or answer == "T":
    t_score()

# Tf question 3
print("Question 3) The Earth is flat.")
answer = input().upper()
if answer == "False" or answer == "F":
    t_score()

# Multiple choice question 1
print(
    "Section 2. Multiple choice questions \nQuestion 1) Who is the President of USA \nA)Donald Trump \nB)Barrack Obama \nC)Joe Biden \nD)Osama bin Ladin"
)
answer = input().upper()
if answer == "C":
    t_score()

# Multiple choice question 2
print(
    "Question 2) How many wheels do trucks have? \nA)4 \nB)6 \nC)8 \nD)all of the above"
)
answer = input().upper()
if answer == "D":
    t_score()

# Multiple choice question 3
print(
    "Question 3) In the movie Avengers what role did Mark Ruffalo? \n A)Iron Man \nB)Hulk \nC)Thor \nD)Captain America"
)
answer = input().upper()
if answer == "B":
    t_score()

# Section 3 Short Answer
print("Section 3. Short answer questions. Please keep your answers to one word.")
print("Question 1) What is the equipment which is used for skating on ice?")
answer = input().upper()
if answer == "ICE SKATING":
    t_score()

print("Question 2) What is the capital of Czechia?")
answer = input().upper()
if answer == "PRAGUE":
    t_score()

percentage = score / 8

if percentage <= 0.5:
    print(f"{score} / 8 You failed, try again!")
elif 0.5 < percentage < 0.8:
    print(f"{score} / 8 You passed!")
else:
    print(f"{score} / 8 You passed with flying colors!")
