import time #enables me to use time basis
import datetime #allows to enter a date
hours = int(input("Enter your hour: ")) #this sets the input - Enter your hour to an integer
minutes = int(input("Enter your minute: ")) #same thing but sets minutes to integer
seconds = int(input("Enter your second: ")) #sets seconds to integer
current_time = datetime.datetime(2024, 10, 21, hours, minutes, seconds) #sets the date in order for time to function
print(current_time.strftime("%H:%M:%S")) #prints the time as a f string with the variables 

while True: #Forever loop
    print("YOUR ALRM SOUNDS") #display the text
    snooze = input("Snooze? ").lower() #parentheses is displayed and the variable = the user response .lower means doesnt matter if capital letter

    if snooze == "yes": #if the user says yes,
        print("Go back to sleep") #print whats in parentheses
        time.sleep(2) #wait two seconds to run code
        current_time += datetime.timedelta(minutes=5)  #add 5 minutes to the time 
    elif snooze == "no": #if user says no 
        print ("Get up") #display get up
        current_time += datetime.timedelta(minutes=1) #add 1 minute
        print (current_time.strftime("%H:%M:%S")) #print time
        break #break forever loop
    else: #if the user says anything else, 
        print ("Invalid Response") #print invalid response
clothes_ready = input ("Are your school clothes ready from last night?").lower() #clothes ready = user response to parentheses

if clothes_ready == "yes": # if user says yes
        print ("Put on dem clothes") #display this
        current_time += datetime.timedelta(minutes=2) #add 2 minutes to time
        print (current_time.strftime("%H:%M:%S")) #display time
elif clothes_ready == "no": #if user says no
    while True: #create a forever loop
        askalexa = input ("Ask Alexa the weather(hot,cold)").lower() #askalexa = user response

        if askalexa == "hot": #if user says hot
            print ("put on a sweater and pants") #display this
            current_time += datetime.timedelta(minutes=3) #add 3 min
            print (current_time.strftime("%H:%M:%S")) #print time
            break        #break loop
        elif askalexa == "cold": #if user says cold
            print ("put on a shorts and shortsleeve shirt")#display this
            current_time += datetime.timedelta(minutes=3) #add 3 min 
            print (current_time.strftime("%H:%M:%S")) #print time
            break #break loop
        else:#antything else
            print ("invalid response") #display this
else: #anything else in the other forever loop
    print ("Invalid Respnse") #display this
while True: #forever loop
    brushteeth = input ("Brush teeth?").lower() #brushteeth = user response

    if brushteeth == "yes": #if user says yes
        print ("Brush and clean retainer") #display this
        time.sleep(1) #code stops for 1 
        current_time += datetime.timedelta(minutes=2) #time + 2
        print (current_time.strftime("%H:%M:%S")) #display this
        break #break the loop
    elif brushteeth == "no":#if user says no
        print ("Teeth get yellow and your breath stinks") # display this
        print (current_time.strftime("%H:%M:%S")) #display time
        break #break loop
    else: #any other user response
        print ("invalid response") #display this
while True: #loop
    hair = input ("Are you gonna style your hair?").lower() #hair = user resonse to that

    if hair == "yes": #if user says yes
        print ("use product and style") #display this
        current_time += datetime.timedelta(minutes=2) #add 2 minutes
        print (current_time.strftime("%H:%M:%S")) # print current time
        break #break loop
    elif hair == "no": # if user says no
        print ("you look like a bozo") #display this
        break #break loop
    else: #anything else
        print ("invalid response") #display this
while True: # forever loop
    washface = input ("Wash your face?").lower() #washface = user response

    if washface == "yes": #if user says yes
        print ("use cleanser") #display this
        current_time += datetime.timedelta(minutes=2) #add two minutes
        break #break loop
    elif washface == "no": #if user says no
        print ("obtain ance") #display this
        break #break loop
    else: #any other user response
        print ("invalid response") # display this
while True: # forever loop
    sportsclothes = input ("Are your sports clothes ready?").lower() #sportsclothes = user response
    if sportsclothes == ("yes"): #if user says yes
        print ("Go downstairs and put them in your sports bag") #display this
        current_time += datetime.timedelta(minutes=1) #add 1 min to time
        print (current_time.strftime("%H:%M:%S")) # print time
        break #break loop
    elif sportsclothes == ("no"): #if user says no
        print ("Go get em") #display this
        current_time += datetime.timedelta(minutes=2) #add two minutes
        print (current_time.strftime("%H:%M:%S")) #print time
    else:#any other response
        print ("Invalid response") # display this
while True: #forever loop
    breakfast = input ("Eating breakfast?").lower() #breakfast = user response
    if breakfast == "yes":#if user says yes
        print ("alright") #display this
        break #end loop
    elif breakfast == "no": #if user says no
        print ("Eat at school") #display this
        break #end loop
    else: #any other user response
        print ("invalid response") #display this
while True: #forever loop
    breakfastready = input ("Is breakfast ready?").lower() #breakfast ready = user response
    if breakfastready == ("yes"): #if user says yes
        print ("consume it") #display this
        current_time += datetime.timedelta(minutes=9) #add 9 min
        break #end loop
    elif breakfastready == ("no"): #if user says no
        print("craft it and consume it") #print this
        current_time += datetime.timedelta(minutes=13) #add 13 min
        break #end loop
    else: #any other input
        print("invalid response") #display this
print ("You are ready to leave LIL BOY") #display this 
print ("The time issss") #display this
print(current_time.strftime("%H:%M:%S"), end='\r') #print time