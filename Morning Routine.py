import time
import datetime
hours = int(input("Enter your hour: "))
minutes = int(input("Enter your minute: "))
seconds = int(input("Enter your second: "))
current_time = datetime.datetime(2024, 10, 21, hours, minutes, seconds)
print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    print("\nYOUR ALRM SOUNDS")
    snooze = input("Snooze? ").lower()

    if snooze == "yes":
        print("Go back to sleep")
        time.sleep(2)
        current_time += datetime.timedelta(minutes=5)  
    elif snooze == "no":
        print ("Get up")
        current_time += datetime.timedelta(minutes=1)
        print (current_time.strftime("%H:%M:%S")) 
        break
    else:
        print ("Invalid Response")
clothes_ready = input ("Are your school clothes ready from last night?").lower()

if clothes_ready == "yes":
        print ("Put on dem clothes")
        current_time += datetime.timedelta(minutes=2)
        print (current_time.strftime("%H:%M:%S")) 
elif clothes_ready == "no":
    while True:
        askalexa = input ("Ask Alexa the weather(hot,cold)").lower()

        if askalexa == "hot":
            print ("put on a sweater and pants")
            current_time += datetime.timedelta(minutes=3)
            print (current_time.strftime("%H:%M:%S")) 
            break        
        elif askalexa == "cold":
            print ("put on a shorts and shortsleeve shirt")
            current_time += datetime.timedelta(minutes=3)
            print (current_time.strftime("%H:%M:%S")) 
            break
        else:
            print ("invalid response")
else:
    print ("Invalid Respnse") 
while True:
    brushteeth = input ("Brush teeth?").lower()

    if brushteeth == "yes":
        print ("Brush and clean retainer")
        time.sleep(1)
        current_time += datetime.timedelta(minutes=2)
        print (current_time.strftime("%H:%M:%S")) 
        break
    elif brushteeth == "no":
        print ("Teeth get yellow and your breath stinks")
        print (current_time.strftime("%H:%M:%S")) 
        break
    else:
        print ("invalid response")
while True:
    hair = input ("Are you gonna style your hair?").lower()

    if hair == "yes":
        print ("use product and style")
        current_time += datetime.timedelta(minutes=2)
        print (current_time.strftime("%H:%M:%S")) 
        break
    elif hair == "no":
        print ("you look like a bozo")
        break
    else:
        print ("invalid response")
while True:
    washface = input ("Wash your face?").lower()

    if washface == "yes":
        print ("use cleanser")
        current_time += datetime.timedelta(minutes=2)
        break
    elif washface == "no":
        print ("obtain ance")
        break
    else:
        print ("invalid response")
while True:
    sportsclothes = input ("Are your sports clothes ready?").lower()
    if sportsclothes == ("yes"):
        print ("Go downstairs and put them in your sports bag")
        current_time += datetime.timedelta(minutes=1)
        print (current_time.strftime("%H:%M:%S")) 
        break
    elif sportsclothes == ("no"):
        print ("Go get em")
        current_time += datetime.timedelta(minutes=2)
        print (current_time.strftime("%H:%M:%S")) 
    else:
        print ("Invalid response")
while True:
    breakfast = input ("Eating breakfast?").lower()
    if breakfast == "yes":
        print ("alright")
        break
    elif breakfast == "no":
        print ("Eat at school")
        break
    else:
        print ("invalid response")
while True:
    breakfastready = input ("Is breakfast ready?").lower()
    if breakfastready == ("yes"):
        print ("consume it")
        current_time += datetime.timedelta(minutes=9)
        break
    elif breakfastready == ("no"):
        print("craft it and consume it")
        current_time += datetime.timedelta(minutes=13)
        break
    else:
        print("invalid response")
print ("You are ready to leave LIL BOY")
print ("The time issss")
print(current_time.strftime("%H:%M:%S"), end='\r')




        

        
     




