# basic rock, paper & scissors game

from random import choice

cl = ["rock", "paper", "scissors"]

while True:
    try:
        i = input("Enter an option (rock, paper or scissors) ▶️ ").lower()
        c = choice(cl)
        
        if i in cl:    
            if i!=c:
                print(f"OMG!🍀 \n\tYour option: {i}\n\tBot option: {c}")
                
            else:
                print(f"Out!💀 \n\tYour option: {i}\n\tBot option: {c}")
                break
    
        else:
            print("Enter a valid option: (rock, paper or scissors) 😵")
    
    except ValueError:
        print("Enter a valid option: (rock, paper or scissors) 😵")