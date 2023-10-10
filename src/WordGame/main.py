#Eddie Li | Hangman WordLogic

# Start
# Generate a word at random and store it in a variable
# Display the length of the word to the user
# Initialize variable LIVES = 6
# while loop runs while LIVES > 0
# Prompt user to guess a letter a through z
# if Condition 1: check if letters match don’t match
# if true, variable LIVES decrease by 1
# elif: letter match
# if true, replace the blank with said letter
# if condition 2: check if word is equal to random word
# if true: print “Congratulation you win!” and end loop
# if condition 3: check whether LIVES = 0
# if true: print “You lose” and end loop
# End while loop
import random
from words import word_list
LIVES = 6
word = random.choice(word_list)

# def word():
#     word = random.choice(word_list)
#     return word
# def display_hangman(LIVES):
#   stages = [ """
#                  --------
#                  |       |
#                  |       O
#                  |      \|/ 
#                  |       |
#                  |      / \
#               """,
#               """
#                  --------
#                  |       |
#                  |       O
#                  |      \|/ 
#                  |       |
#                  |      /
#               """,
#               """
#               --------
#                  |       |
#                  |       O
#                  |      \|/ 
#                  |       |
#                  |      
#               """,
#               """
#                  --------
#                  |       |
#                  |       O
#                  |      \| 
#                  |       |
#                  |     
#               """,
#               """
#                  --------
#                  |       |
#                  |       O
#                  |       |
#                  |       |
#                  |      
#               """,
#               """
#                  --------
#                  |       |
#                  |       O
#                  |       
#                  |       
#                  |      
#               """,
#               """
#                  --------
#                  |       |
#                  |       
#                  |       
#                  |       
#                  |     
#               """
#             ]
#   return stages[LIVES]

# display_hangman(LIVES)

def play(word):
  # blank = "_" * len(word)
  length = len(word)
  print("Length of word: " + str(length))
  LIVES = 6
  guesses = ""
  while LIVES > 0:
     print("Lives: " + str(LIVES))
     guess = input("Guess a letter: ")
     guesses += guess
     for char in word:
       if char in guesses:
         print(char)
       else:
         print("_")
     if guess not in word:
        LIVES -= 1
     # if guess in word:
     #     print(word.replace(_, guess))
     # elif guess not in word:
     #     LIVES-=1
     if guess == word:
         print("Congratulations you win!")
         break
     if LIVES == 0:
         print("You lose")
         break
  return



play(word)
