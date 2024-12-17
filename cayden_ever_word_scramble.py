import random #random library is imported 
import time #time library is imported
user_name = input ("Hello, what is your name?") #displays message asking for name
print ("Directions: A scrambled word will be displayed, and you must guess the word. You have 5 guesses before the round is over.") #displays directions
time.sleep (3) #wait 3 seconds
print (f"good luck, {user_name}") #display good luck, name
words = ["computer", "science", "programming", "python", "logic", "board","game","condition"] #create list with words
games = 0 #set games to 0
wins = 0 #set wins to 0
time.sleep(1) #wait 1 second

while True: #forever loop
    word = random.choice(words) # word = random selection of words
    display = list(word) #set display to list of words
    random.shuffle (display) #shuffle display list
    scrambled_word = "".join(display) #turn this list of random letters in the word to one word with no spaces
    turns = 5 #set turns to 5
    
    while turns > 0: #while turns is > 0
        print(f"the scrambled word is: {scrambled_word}") #print the scrambled word
        user_word = input ("enter your guess for the word here!: ") #ask user the question to enter the word here
        
        if user_word == word: #if guess is correct
            print ("good job lil boy, you got it!") #display message 
            wins +=1 #add 1 to win
            break #terminate loop

        while True: #forever loop
            user_wrong = input ("You did not get the word. would you like to rescramble? y/n: ").lower() #ask user question would you like to rescramble?
            if user_wrong == ("n"): #if user says no
                break #terminate loop
            elif user_wrong == ("y"): #if user says yes
                display = list(word) #repeat steps that scramble the word
                random.shuffle (display) #repeating the step the scrambles
                scrambled_word = "".join(display) #repeating the step that scrambles
                break #terminate loop
            else: #if neither of these are chosen
                print ("invalid response") #display invalid response
        turns -= 1 #set turns back -1
    games += 1 #add 1 to game
    print (f"You have won {wins} games, out of {games} games!") #display the mesage you have won _ out of _games
    
    while True: #forever loop
        playagain = input ("would you like to play another round? y/n: ").lower() #ask user if they would like to play again
        
        if playagain == ("y"): #if user says yes 
            break #terminate loop
        elif playagain == ("n"): #if user says no
            exit() #exit code
        else: #any other input
            print ("invalid response") #display invalid response

