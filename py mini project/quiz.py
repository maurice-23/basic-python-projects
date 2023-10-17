print ("Welcome to quiz!")
playing = input ("Do you want to play? Y/N ")
playing = playing.upper()

quest2 = "What Sql stand for?"
ans2 = "structured query language "

quest3 = "What Php stands for? "
ans3 = "hypertext preprocessor "

marks = 0
if playing == "N" :
    quit()
elif playing == "Y" : 
    names = input ("Enter your names to continue: ")
    print ("Welcome",names, " in quiz!")
    ans1 = (input("What does ICT stands for? ")).lower()
    if ans1 == "information communication technology" :
        print("Congz you are correct! :)")
        marks = 5
    else:
        quest2 = input(quest2).lower()
        if quest2 == ans2 :
            print("Congz you are correct! :)")
            marks = 10
            quest3 = (input(quest3)).lower
            if quest3 == ans3 :
                print("Congz you are correct! :)")
                marks = 15
                print("Your marks is ", marks,"/15")
            else: 
                print("Failed :( the true answer was ", ans3)
                print("Your marks is ", marks,"/15")
        else: 
            print("Your marks is ", marks,"/15")
    
else: 
    print("Choose Y for yes and N for No to continue")