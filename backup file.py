#guess the music theme

import random

#This is for welcome statement
def welcome_statement():
    """Start the music theme guessing game"""
    print("Hello player!!")
    print("The computer will generate a random music genre")
    print("You have to guess the right genre")
    print("You have 5 attempt to guess it.")

#list of selected music genre
genre = [
    "hiphop",
    "Jazz",
    "ballad",
    "R & B",
    "Kpop",
    "Rock",
    "Country"
    ] 

#this is when guess need to input answer
x = random.choices(genre)
guess = None   

while x != guess:

    guess = str(input("Pick a music genre correctly: "))

    if x == guess:
        print("You are incredible!")
    elif x != guess:
        print("Try the genre that most people love")
        
welcome_statement()