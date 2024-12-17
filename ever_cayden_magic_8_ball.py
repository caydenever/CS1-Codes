import random #import random library
import time #import time library

print ("Welcome to the Magic 8 ball!") #display this
#making a response list
responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely","Outlook good", "Yes",  "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again","Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"] 
#making a question starters list
question_starters = ["Will", "Am", "How", "What", "Why", "Where", "When", "Which", "Who", "Whose", "Is"]

while True: #forever loop
    time.sleep(2)  #wait two seconds
    question = str.lower(input("ask me a question! ")) #set quesiton to input 
    first_word = question.split()[0] #split the list into one word and identify that first word
    
    if question.lower() == "quit": #if input = quit
        break #break loop
    elif "?" in question and first_word.capitalize() in question_starters: #if there is a ? and a queso starter
        print("predicting your answer...") #display this
        time.sleep(1) #wait 1 second 
        print(random.choice(responses)) # display the response
    else: #anything else
        print("not a question!") #display this
