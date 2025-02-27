# basic handcricket game

from random import randint

nl = []

while True:
    try:
        i = int(input("Enter a number ▶️ "))
        
        if not i<1 and not i>10:
            n = randint(1,10)
            
            if i != n:
                nl.append(i)  
                print(f"Lucky!🔥 You are on {sum(nl)}. 💪 \n\tYour number: {i}\n\tBot number: {n}")
            
            else:
                print(f"Out!💀 You were on {sum(nl)}. 😭 Total score\n\tYour number: {i}\n\tBot number: {n}")
                break
            
        else:
            print("Enter a valid number (1-10)")
    
    except ValueError:
        print("Enter a valid number (1-10)")