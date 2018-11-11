#HANGMAN GAME
#Sathvik's Massive Project

LISTOFWORDS=("COUPLE","POKEMON","SACHIN","BAAHUBALI","PYTHON")
import random
word=random.choice(LISTOFWORDS)
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |  | | |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |  | | |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |  | | |
 |    |
 |   | |
 |   | |
 |  
----------
""")
wrong=0
maxwrong=len(HANGMAN) - 1
length=len(word)
used=[]
sofar= "-" * len(word)
while wrong < maxwrong and sofar!=word:
    print(HANGMAN[wrong])
    print("The word is",sofar)
    guess=input("Enter your guess letter :")
    guess=guess.upper()
    used.append(guess)
    print("------------------------------------------------")
    print("Used Words :", used)
    print("------------------------------------------------")
    new=""
    if guess in word:
        for i in range(length):
            if guess==word[i]:
                new += guess
            else:
                new += sofar[i]
        sofar=new
    else:
        print("Sorry ,The word ",guess," is not in the word")
        wrong+=1
if wrong==maxwrong:
    print(HANGMAN[wrong])
    print("GAME OVER, You had been hanged :'(")
    print("The correct word is :",word)
else:
    print("Congrats, u guessed the word correctly")

input("press any key to terminate")
