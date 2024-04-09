def new_game():
    guesses = []
    correct_guesses = []
    question_num =1 

    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C,D)")    
        guess =  guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num+=1    
    display_score(correct_guesses,guesses)    


def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("INCORRECT")
        return 0
def display_score(correct_guesses,guesses):
    print("RESULTS")
    print("Answers:" end="")
    for i in questions:
        print(questions.get(i), end="")
    print()    

    print("Guesses:",end="")
    for in in guesses:
        print(questions.get(i),end="")
    print()    
    score= int((correct_guesses/len(questions)) * 100)
    print("Your score is: "+ str(score)+"%" )

def play_again():

    response = input("What do you want coninute playing?: ")
    responde.upper()
    if response == "YES":
        return True
    else:
        return False
    
questions = {
    "Who created Python?" : "A",
    "What year was Python created?" : "B",
    "Python is atributed to wich comedy group? ": "C",
    "I sthe Earth round? " : "A"
}

options = [

    ["A. Guido van Rossum","B. Elon Musk","C. Bill Gates","D. Mark Zuckerberg"],
    ["A. 1989","B. 1991","C. 2000","D. 2016"],
    ["A. Lonely Island","B. Smosh","C. Monty Python", "D. SNL"],
    ["A. True","B. False", "C. Sometimes", "D. What'is Earth?"]

]

while play_again():
    new_game()
print("Byeeeeee")    
