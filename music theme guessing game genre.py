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

#import the built in method random to generate an automatic secret number from random import
#Generate automatic secret genre
clues_genre = random(1,7)

#Get a guessing genre from user
guess_genre = str(input("Guess the secret genre between A and G:"))
 
#Check guessing genre is correct or false
if clues_genre == guess_genre:
    print("Your guess is correct")
elif clues_genre != guess_genre:
    print("Please try again")    

#this is a sample clues
clues = [
    "1 for Rock"
    "2 for R & B"
    "3 for Jazz "
    "4 for Kpop"
    "5 for country"
    "6 for Ballad"
    "7 for Hiphop"]   

welcome_statement()
    

