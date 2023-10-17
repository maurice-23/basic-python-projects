import random 
userwin = 0
computerwin = 0
draw = 0
options = ["rock", "paper", "scissor"]
while True:
    user_input = input("Type Rock/Paper/Scissor or q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("computer picked ", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissor":
        print("Your choise was ", user_input)
        print ("You win 🎉🎊")
        userwin += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("Your choise was ", user_input)
        print("You win 🎉🎊")
        userwin += 2
    elif user_input == "scissor" and computer_pick == "paper":
        print("Your choise was ", user_input)
        print("You win 🎉🎊")
        userwin += 1
    elif user_input == computer_pick:
        print("Your choise was ", user_input)
        print("Draw 🔁")
        draw += 1
    else:
        print("Lost! try again")
        computerwin += 1
        continue
        
print("You won ", userwin, " times")
print("computer won ", computerwin, " times")
print(draw, "times draw")
print("let's play later!")