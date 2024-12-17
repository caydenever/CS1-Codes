import random 
import time
user_name = input ("Hello, what is your name?")
print ("Directions: A scrambled word will be displayed, and you must guess the word. You have 5 guesses before the round is over.")
time.sleep (3)
print (f"good luck, {user_name}")
words = ["computer", "science", "programming", "python", "logic", "board","game","condition"]
games = 0
wins = 0
time.sleep(1)

while True:
    word = random.choice(words)
    display = list(word)
    random.shuffle (display)
    scrambled_word = "".join(display)
    turns = 5
    
    while turns > 0:
        print(f"the scrambled word is: {scrambled_word}")
        user_word = input ("enter your guess for the word here!: ")
        
        if user_word == word:
            print ("good job lil boy, you got it!")
            wins +=1
            break

        while True:
            user_wrong = input ("You did not get the word. would you like to rescramble? y/n: ").lower()
            if user_wrong == ("n"):
                break
            elif user_wrong == ("y"):
                display = list(word)
                random.shuffle (display)
                scrambled_word = "".join(display)
                break
            else:
                print ("invalid response")
        turns -= 1
    games += 1
    print (f"You have won {wins} games, out of {games} games!")
    
    while True:
        playagain = input ("would you like to play another round? y/n: ").lower()
        
        if playagain == ("y"):
            break
        elif playagain == ("n"):
            exit()
        else:
            print ("invalid response")

