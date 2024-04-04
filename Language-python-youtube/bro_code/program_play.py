import random


choices = ["rock","scissors","paper"]

computer = random.choice(choices)
computer.lower()
attemps = input("Select count of attemps: \n")
user_p = 0
computer_p = 0
count = 0
while int(count) < int(attemps):
    user = input("Select option: rock , scissors and paper: \n")

    match user.lower():
        case "rock":
            if computer == "rock":
                user_p = 0
                coputer_p = 0
            elif computer == "paper":
                computer_p += 1
            elif computer == "scissors":
                user_p +=1 

        case "scissors":
            if computer == "rock":
                computer_p += 1
            elif computer == "paper":
                user_p +=1  
            elif computer == "scissors":
                user_p = 0
                computer_p = 0

        case "paper":
            if computer == "rock":
                user_p +=1
            elif computer == "paper":
                user_p = 0
                computer_p =0
            elif computer == "scissors":
                computer_p+=1
        case _:
            print("Error!!!, select correctly")
    count+=1        

if user_p > computer_p:
   print("Congratualitions")
else:
   print("Game over")

