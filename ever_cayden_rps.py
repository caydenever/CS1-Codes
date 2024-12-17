#cat
import pygame #importing the code to use the sound
import random #importing the code to use random
import os #importing the code to clear string
import time #importing the code to use time
pygame.init() #initiating sound system
pygame.mixer.init() #initiate mixer
filepath = "c:/Users/cever28/Downloads/CS1 2024/welcome_music.mp3" #finding the exact location of the mp3 file
pygame.mixer.music.load(filepath) #load up the mp3 file
pygame.mixer.music.set_volume(0.9) #set volume
pygame.mixer.music.play() #play the sound

print ('''
               .__                               
__  _  __ ____ |  |   ____  ____   _____   ____  
\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
 \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >
             \/          \/            \/     \/ 

''') #display this ART
time.sleep(2) #wait 2 seconds
print("directions: the code will ask you which game mode to play. If you win the game your score goes up by 3! if you loose you get 0 points.") #display this
time.sleep(2)
print("Enjoy the Game!") #display this
time.sleep(3) #wait 3 seconds
print ("PS there will be sound effects") #display this
time.sleep(2) #wait 2 seconds
pygame.quit() #stop the time
def sound(): # make a function so that I dont have to repeat it every time I use
    pygame.init() #initiate pygame
    pygame.mixer.init() #initiate pigame mixer
    filepath2 = "c:/Users/cever28/Downloads/CS1 2024/winning_sound_effect.mp3" #find exact location of file
    pygame.mixer.music.load(filepath2) #load up the file
    pygame.mixer.music.set_volume(0.9) #set volume
    pygame.mixer.music.play() #play the music
    time.sleep(2)
    pygame.quit() #quit

rps = ["rock", "paper", "scissors"] #making a list of RPS
p1name = input ("player 1 what is your name?: ") #asking player 1 name
p1score = 0
p2score = 0

while True: #forever loop
    user_game_choice = input("twoplayer or computer: ") #allowing user to choose between twoplayer or computer

    if user_game_choice == "twoplayer": # if user says twoplayer
        p2name = input("player 2 what is your name?: ") #p2 name is set to this input
        break #break the loop
    elif user_game_choice == "computer":#ìf user game choice is computer
        p2name = "bot" #setting player 2 name to bot if its computer
        break #break loop
    elif user_game_choice == "player1win" or user_game_choice == "player2win": #special code
        p2name = input ("player 2 what is your name?: ") #Asking playerwhat their name is
        if user_game_choice == "player1win": #if it = the special code
            winner, loser = p1name, p2name #set winner, then loser 
        elif user_game_choice == "player2win": #if it is player 2 win
            winner, loser = p2name, p1name #seet winner, then loser to the names
        os.system("cls") #clear screen
        player1 = (input (f"{p1name} rock, paper, or scissors: ")).lower() #asking player RPS
        os.system("cls") #clear screen
        player2 = (input(f"{p2name} rock, paper, or scissors: ")).lower()#asking player RPS
        os.system("cls") #clear screen
        print (f"{winner} destroys {loser}") #print variable winner destroys loser
        sound() #play my sound
    elif user_game_choice == "quit":
        exit()
    else: #any other response
        print("invalid") #display invalid

while True: #forever loop
    player1 = (input (f"{p1name} rock, paper, or scissors: ")).lower() #asking player 1 RPS
    os.system("cls")#clear screen

    if user_game_choice == "twoplayer": #if it is twoplayer
        player2 = (input (f"{p2name}: rock, paper, or scissors: ")).lower() #ask player 2 for RPS
        os.system("cls") #clear screen
    else:
        player2 = random.choice(rps) #any other response will make it a random computer
    
    if player1 == "quit":#if the person says quit
        exit() #leave
    elif player2 == "quit": #if the person says quit
        exit() #leave
    elif player1 == player2: #if player 1 response = player2
        print ("You TIED") #print u tied
        sound() #play sound
        print (f"{p1name}'s score is {p1score}") #print p1name's score
        print (f"{p2name}'s score is {p2score}") #p2 name score
    elif player1 == "rock" and player2 == "paper": #if p1 = rock and p2 = paper
        print (f"{p2name} Destroys {p1name}!") #print p2name beats p1name
        sound() #play sound
        p2score +=3 #add 3 to p2score
        print (f"{p1name}'s score is {p1score}") #display p1 score
        print (f"{p2name}'s score is {p2score}") #display p2 score
    elif player1 == "paper" and player2 == "scissors": #if p1 = paper and p2 = scissors
        sound() #play sound
        p2score +=3
        print (f"{p2name} gets a victory over {p1name}!")#display p2name beats p1name
        print (f"{p1name}'s score is {p1score}") #display p1 name score
        print (f"{p2name}'s score is {p2score}") #display p2 name score
    elif player1 == "scissors" and player2 == "rock": #if p1 = scissors and p2 = rock
        sound() #play sound 
        print (f"{p2name} crushes {p1name}!") #p2name beats p1 name
        p2score +=3 #add 3 to p2score
        print (f"{p1name}'s score is {p1score}") #display p1name score
        print (f"{p2name}'s score is {p2score}") #display p2name score
    elif player2 == "rock" and player1 == "paper": #if p2 = rock and p1 = paper
        sound() #play sound
        print (f"{p1name} dominates {p2name}!") #display p1name beats p2name
        p1score+=3 #add 3 to p1score
        print (f"{p1name}'s score is {p1score}") #print p1 name score
        print (f"{p2name}'s score is {p2score}")#print p2name score
    elif player2 == "paper" and player1 == "scissors":#if p2 = paper and p1 = scissors
        sound() #play sound
        print (f"{p1name} Wins!") #print p1 wins
        p1score+=3 #add 3 to p1 score
        print (f"{p1name}'s score is {p1score}") #print p1name score
        print (f"{p2name}'s score is {p2score}") #print p2 name score
    elif player2 == "scissors" and player1 == "rock": #if p2 = scissors and p1 = rock
        sound() #play sound
        print (f"{p1name} beats {p2name}!")# display p1 beats p2
        p1score+=3 #add 3 to p3 score
        print (f"{p1name}'s score is {p1score}") #display p1name score
        print (f"{p2name}'s score is {p2score}") #display p2name score
    else: #any other input
        print ("invalid response") #display this