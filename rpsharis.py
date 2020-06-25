import random

user_score = 0
pc_score = 0

print("pick rock, paper, or scissors")
user_choice = input("User turn:")

choices = ["rock", "paper", "scissors"]

while True:
    
    print("pick rock, paper, or scissors")
    
    user_choice = input("User turn:") .lower()
    pc_choice = choices[random.randint(0,2)]

    print("Computer picks: " + pc_choice)
    
    if user_choice == pc_choice:
        print("WE HAVE A TIE")
        
    elif user_choice == "rock":
         if pc_choice == "scissors":
             print("User wins!")
             user_score = user_score + 1   
             print(user_score)
         else:   
             print("Computer wins!")
             pc_score = pc_score + 1
             print(user_score)
    
    elif user_choice == "paper":
         if pc_choice == "rock":
             print("User wins!")
             user_score = user_score + 1   
             print(user_score)
         else:   
             print("Computer wins!")
             pc_score = pc_score + 1
             print(user_score)

        

    elif user_choice == "scissor":
         if pc_choice == "paper":
             print("User wins!")
             user_score = user_score + 1   
             print(user_score)
         else:   
             print("Computer wins!")
             pc_score = pc_score + 1
             print(user_score)
    if user_score == 3 and pc_score == 3:
        print("It is a tie!")
        quit()
    elif user_score == 3 and pc_score < 3:
        print("You got to three first so you win!!!!")
        quit()
    else:
        print("The computer got to three points first so you lose.")
        quit()
