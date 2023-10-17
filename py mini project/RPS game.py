import random
ready = (input("Are u ready to play? (y/n) ")).lower()
use = ['rock', 'paper', 'scissor']
Cchoise = use[random.randint(0,3)]

if ready == "y":
    print("welcome Buddy!!")
    player = (input("Are you Rock(R) Paper(P) or Scissor(S)? ")).lower()
    global p, s, r
    
    p = "paper"
    s = "Scissor"
    r = "Rock"
    
    # player choise

    if player == "r" :
        print("You are Rock 🥌")
        player = r
    elif player == "p":
        print("you choose Paper 📃")
        player = p
    elif player == "s":
        print("you choose Scissor ✂")
        player = s
    else:
        print("Choose R/P/S")

    #computer choise
    
    
    if Cchoise == "paper":
        Cchoise = p
    elif Cchoise == "rock":
        Cchoise = r
    elif Cchoise == "scissor":
        Cchoise = s
    else:
        print("error 503")
    
    
    #Processing and answer

    if p and s:
        print(s, "wins")
    elif p and r:
        print(p, "Wins")
    elif r and s:
        print(r, "Wins")
    else:
        print("Internal server error")
    
    #when player not ready
elif ready == "n": 
    print("okay!, May be next time")
    
    #when choise is not available
else:
    input("Choose Y/N next time")

